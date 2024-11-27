---
title: "Curvas ROC"
authors:
  - fbetteo 
date: 2018-10-28
slug: curvas-roc
thumbnailImage: https://lh3.googleusercontent.com/tLg0Pr_VbROknZC9tfWmkQRxtItwLZEalRMnszkTwnROkVlJDOC4QUsUnJLdfL8s6A1BhuW8UGIOzoLS7Q=w221-h220-rw
tags:
- R
- estadistica
categories:
- estadistica
- R
thumbnailImagePosition: left
summary: Post sobre como curvas ROC y Area bajo la Curva (AUC).
---
# Curvas ROC

La curva ROC y AUC (area bajo la curva) permiten evaluar la eficacia de un modelo clasificador y elegir el mejor umbral de corte donde determinar qué observación es predicha positiva y cual negativa.

Vamos a generar rapidamente un clasificador con regresión logísitca utilizando el dataset *mtcars* ya provisto por R. Solo a modo ilustrativo utilizaremos AM (caja manual o automática) como la variable a predecir y mpg y drat como independientes. No separamos en train y test dadas las pocas observaciones.


```r
library(tidyverse)
library(modelr)
library(pROC)
df <- mtcars %>% select(am, mpg, drat) %>% mutate(am = as.factor(am))
summary(df)
```

```
##  am          mpg             drat      
##  0:19   Min.   :10.40   Min.   :2.760  
##  1:13   1st Qu.:15.43   1st Qu.:3.080  
##         Median :19.20   Median :3.695  
##         Mean   :20.09   Mean   :3.597  
##         3rd Qu.:22.80   3rd Qu.:3.920  
##         Max.   :33.90   Max.   :4.930
```

```r
# Clase dentro de todo balanceada

mdl.log <- glm(formula = am ~., data = df, family = binomial(link="logit"))
fit <- predict(mdl.log, newdata = df, type = "response")


roc(df[,1],  fit , percent=F,   boot.n=1000, ci.alpha=0.9, stratified=FALSE, plot=TRUE, grid=TRUE, show.thres=TRUE, legacy.axes = TRUE, reuse.auc = TRUE,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue", ci=TRUE, ci.type="bars", print.thres.cex = 0.7, main = paste("ROC curve using","(N = ",nrow(df),")") )
```

![Image](./img/2018-10-28-curvas-roc-unnamed-chunk-1-1.png)

```
## 
## Call:
## roc.default(response = df[, 1], predictor = fit, percent = F,     ci = TRUE, plot = TRUE, boot.n = 1000, ci.alpha = 0.9, stratified = FALSE,     grid = TRUE, show.thres = TRUE, legacy.axes = TRUE, reuse.auc = TRUE,     print.auc = TRUE, print.thres.col = "blue", ci.type = "bars",     print.thres.cex = 0.7, main = paste("ROC curve using", "(N = ",         nrow(df), ")"))
## 
## Data: fit in 19 controls (df[, 1] 0) < 13 cases (df[, 1] 1).
## Area under the curve: 0.9433
## 95% CI: 0.8695-1 (DeLong)
```

Básicamente entrenamos un modelo logístico y graficamos la curva ROC prediciendo sobre el mismo dataset con el que fue entrenado. No es lo adecuado pero dadas las pocas observaciones y el propósito explicativo no lo tomamos como un problema.
La curva ROC es la más oscura y como vemos empieza en (0,0) y termina en el (1,1).
El eje X es 1 - Especificidad (Falsos Negativos) y el eje Y es Sensitividad (Verdaderos Positivos) por lo tanto lo deseable es estar lo más arriba a la izquierda posible. El punto (0,1) sería óptimo ya que habría 0 falsos negativos y 100% de verdaderos positivos.

Lo que representa la curva es la combinación de Sensitividad y (1 - especificidad) para varios puntos de corte. Recordemos que la regresión logística devuelve un valor entre 0 y 1 por lo tanto hay que determinar en qué valor empezamos a considerar una predicción como positiva o negativa. En este caso positivo sería tener un valor de 1 en am, por lo tanto tener caja automática. Cada punto de la curva corresponde a algún punto de corte. Como decíamos antes, el mejor debería ser el más "arriba a la izquierda" aunque depende el problema eso puede cambiar, dependiendo del costo de equivocarse en uno u otro sentido.

El peor escenario es que la curva siga a la diagonal, lo que equivaldría a ser iguales a un modelo eligiendo siempre la clase mayoritaria, totalmente inútil. Si estuviera por debajo de la diagonal, sería peor aún, pero bastaría con invertir las predicciones para pasar a estar por encima. Un viejo truco no muy científico.

El área bajo la curva (AUC) es una medida resumen de la curva ROC ya que justamente describe el área entre la curva ROC y la diagonal. Valores mayores se corresponden con curvas ROC más alejadas de la diagonal y por lo tanto que separan mejor a la clase dependiente. Es útil para comparar modelos.

