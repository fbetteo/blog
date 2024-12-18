---
title: "Teorema Central del Limite"
authors:
  - fbetteo 
date: 2019-10-13
slug: teorema-central-del-limite
tags:
- estadistica
- r
- simulacion
categories:
- estadistica
- R
thumbnailImage: https://lh3.googleusercontent.com/YlPH-JgW51OVbX0o9qQQviaUy0syk9-xDk7NuTwNa1ySUWtfFERNJtmPsO2SHUGymvNUS9byNhHwt8M6tw=w260-h173
thumbnailImagePosition: left
summary: Explicación y diferencias de dos versiones del teorema central del Límite.
---

# Teorema Central del Limite

El [teorema central del límite (TCL)](https://es.wikipedia.org/wiki/Teorema_del_l%C3%ADmite_central) 
es fundamental en el desarrollo de la estadística y ha obtenido
distintas variantes a lo largo de la historia. Veremos dos de las versiones más conocidas.

### Teorema Central del Límite para Media Muestral (Lindeberg - Lévy)

> Si las varaibles $X_1 ... X_n$ forman una muestra aleatoria de tamaño n proveniente de una 
distribución con media $\mu$ y varianza $\sigma^2$ (0 < $\sigma^2$ < $\infty$), entonces  para 
cualquier número fijo x.
$$  \lim_{n\to \infty} Pr\Big[\frac{n^{1/2}(\bar X_n - \mu)}{\sigma} <= x\Big] = \Phi (x)$$


Donde $\Phi (x)$ es la función de distribución de una Normal Estándar.

El por qué de la convergencia del teorema no será probado acá pero no es díficil de encontrar.
Por ejemplo [ACÁ](https://www.uv.es/ceaces/tex1t/2%20conver/levi.htm)

Básicamente lo que dice el teorema, es que tomando una muestra grande de una población con media $\mu$ y 
varianza $\sigma^2$ definidas, entonces $\frac{n^{1/2}(\bar X_n - \mu)}{\sigma}$ va a tender a una normal estándar. Como consecuencia de eso podemos decir que $\bar X_n$ va a distribuirse 
aproximandamete como $N(\mu, \sigma^2/n)$.

El TCL nos dice cómo se distribuye la media muestral si tenemos una muestra grande.

Análogamente, también podemos decir que $\sum_{i=1}^n X_i$ va a ser aproximadamente una normal
$N(n\mu, n\sigma^2)$

#### Ejemplo. Lanzar una moneda

Si lanzamos una moneda 900 veces. Cuál es la probabilidad  de obtener más de 495 caras?

$X_i$ = 1 si sale cara en el lanzamiento i, y 0 si sale cruz.  
E($X_i$) = 1/2 y Var($X_i$) = 1/4. Esto se deduce de ser un experimento con distribución Bernouilli.

Para llevarlo a los términos del TCL, tenemos una muestra de tamaño n = 900, con $\mu$ = 1/2 y
$\sigma^2$ = 1/4.

Por TCL tenemos que la distribución de la suma del número total de caras $\sum_{i=1}^{900} X_i$ se
distribuye aproximádamente como una normal con media = 900 * (1/2) = 450,
varianza = 900 * (1/4) = 225 y desvío estándar 225^(1/2) = 15.

Por lo tanto la variable $Z = \frac{H - 450}{15}$ se dsitribuye aproximadamente como una normal 
estándar.
$$Pr( H > 495) = Pr(\frac{H - 450}{15} > \frac{495 - 450}{15}) = Pr(Z>3) = 1 - \Phi(3) = 0.0013$$

Podemos comparar contra el resultado que obtenemos al hacer el mismo ejercicio pero mirando 
directamente la distribución binomial (que es la que realmente genera el proceso de datos)


```r
pbinom(495,900, 0.5, lower.tail = FALSE)
```

```
## [1] 0.001200108
```

Vemos que los resultados son muy similares.

### Teorema Central del Límite para Suma de Variables Aleatorias Independientes (Liapunov)

Este TCL aplica a una secuencia de variables aleatorias independientes pero que no necesariamente
tienen que provenir de una misma distribución. Todas deben tener una media y varianza definidas.

La variable $$Y_n = \frac{\sum_{i=1}^n X_i - \sum_{i=1}^2 \mu_i}{(\sum_{i=1}^n\sigma_i^2)^{1/2}}$$

Entonces $E(Y_n) = 0$ y $Var(Y_n)$ = 1

Siendo un poco más precisos veamos el teorema:

> Suponiendo que las variables aleatorias $X_1. X_2, ...$  son independientes y que
$E(|X_i - \mu_i|^3) < \infty$ para 1,2,...
Y suponidendo que $$\lim_{n\to \infty} \frac{\sum_{i=1}^n E(|X_i - \mu_i|^3)}{(\sum_{i=1}^n \sigma^2_i)^{3/2}} = 0$$
Entonces, utilizando la variable Y definida previamente tenemos que $$\lim_{n \to \infty} Pr(Y_n <= x) = \Phi(x)$$

La interpretacaión del teorema es que si se cumple la condición de los 3eros momentos, entonces para valores grandes de n la distribución de $\sum_{i=1}^n X_i$ será aproximadamente normal con media $\sum_{i=1}^n \mu_i$ y varianza $\sum_{i=1}^n \sigma^2_i$.


### Diferencias entre Lindeberg-Lévy y Liapunov

El teorema de Lindeberg-Lévy aplica para secuencias de variables aleatorias iid y solo requiere que la varianza de estas variables sea finita. En cambio el teorema de Liapunov aplica a secuencias de variables aleatorias independientes pero que no necesariamente provienen de una misma distribución. Requiere que el tercer momento de cada variable existe y cumple con la ecuación del teorema.

### Efecto de TCL

Más allá de la utilidad para aproximar distribuciones y medias mediante una normal, el TCL aporta una posible explicación a por qué tantas variables se distribuyen aproximadamante como normales. Si muchas de las variables a medir pueden pensarse como sumas de otras variables es lógico que tiendan a verse como normales aunque las variables que se suman para darle origen provengan de distintas distribuciones.
