---
title: "Simulación de Monty Hall"
authors:
  - fbetteo 
date: 2018-08-25
slug: simulacion-de-monty-hall
tags: 
- R 
- simulacion
categories: 
- R
thumbnailImage: https://lh3.googleusercontent.com/D-QmS4wFc2c3gXqiGF1L4_xxptUgOAUbAUGaRoFEnt-DrtsnHbWUODROqIk1xfus8YwTi5wujcn57MoLAA=w396-h220-rw
thumbnailImagePosition: left
summary: Simulación en R del famoso problema de Monty Hall. Ejemplo útil para ver el potencial de R y todo de manera sencilla.
---

# Simulación de Monty Hall

Vamos a ver en un corto y sencillo ejemplo cómo hacer una simulación en R. El caso a utilizar es el "famoso" [problema de Monty Hall](https://es.wikipedia.org/wiki/Problema_de_Monty_Hall), asociado a un programa televisivo de Estados Unidos. 

  En breve, el problema consiste en que un concursante debe elegir una entre 3 puertas (A,B y C). Detrás de una hay un premio (en general un automóvil) y tras las otras dos no hay nada (o una cabra en algunos ejemplos, lo cual no me parece tan malo en realidad..).
Una vez que el concursante eligió una puerta, el organizador del programa, que sabe qué puerta oculta el premio y cuáles no, abre una de las dos puertas restantes, tras la cual no hay premio (recuerden que sabe qué hay detrás de cada puerta).
Ante el nuevo escenario, el concursante debe elegir si mantiene su elección original o decide cambiar por la puerta restante, es decir, la que no eligió ni la que abrió el organizador.

* Qué conviene hacer ante tal incertidumbre? 
    + Cambiar? 
    + Mantenerse fiel a la decisión original sin caer en los juegos psicológicos del programa? 
    + Es indistinto? 50/50 entre las dos puertas.
  
La simulación deberíaa darnos una respuesta acertada. Comencemos.


Generamos las puertas y un vector donde vamos a guardar el resultado de la simulación.


```r
puertas <- c("A","B","C")
xdata   <- c()
```

Ahora lo que vamos a hacer es simular 10000 escenarios distintos emulando la lógica del problema. En cada uno vamos a asignarle a una puerta al azar el premio (con el comando "sample"). Luego elegiremos, como si fueramos el concursante, una puerta al azar. Descartaremos una de las puertas sin premio y por último y más importante, vamos a analizar en cada escenario qué hubiera pasado si nos quedabamos con la puerta elegida originalmente y qué hubiera pasado si cambiábamos. 
Si no hay diferencia entre cambiar y no cambiar, luego de 10000 simulaciones deberíamos haber ganado 5000 veces al cambiar y 5000 al no cambiar (con algún margen de error). En caso contrario, alguna de las dos estrategias es superadora.



```r
set.seed(10)
for (i in 1:10000) {  # 10000 iteraciones
  premio <- sample(puertas)[1] # Asignar al premio una puerta al azar
  eleccion <- sample(puertas)[1] # Concursante elige una puerta al azar
  abrir <- sample(puertas[which(puertas != eleccion 
  & puertas != premio)])[1]
  # "Abren" una que no es la que elegiste ni la que tiene premio
  cambiarsi <- puertas[which(puertas != eleccion 
  & puertas != abrir)] # Situacion si cambiaras. 
  if(eleccion == premio) (xdata = c(xdata,"nocambiargana")) 
  # Caso en que eleccion original ganara y guardas resultado
  if(cambiarsi == premio)(xdata = c(xdata, "cambiargana"))
  # Caso en que cambiar ganara y guardas resultado
}
```

LLegado este punto tenemos un vector xdata que tiene para cada una de las 10000 iteraciones, qué estategia hubiera ganado. Si cambiar de puerta o no cambiar.
Ahora simplemente contamos cuántas hay de cada una y analizamos el resultado.


```r
length(which(xdata == "cambiargana")) # Cantidad que hubieran ganado si cambiabas
```

```
## [1] 6623
```

```r
length(which(xdata == "nocambiargana")) 
```

```
## [1] 3377
```

```r
# Cantidad que hubieran ganado si no cambiabas

table(xdata)
```

```
## xdata
##   cambiargana nocambiargana 
##          6623          3377
```

Para sorpresa o no de ustedes, la elección parece obvia. Cambiar de puerta nos hace elegir el premio un 66% de las veces y no cambiar tan solo un 33%.  

Entender por qué es interesante.  

Al elegir inicialmente una puerta entre las 3 opciones, la probabilidad de acertarle al premio es 1/3. De ahí que la estrategia de no cambiar de puerta es efectiva solo un 33% de las veces. Es simplemente quedarse con la elección inicial que tenia 1/3 de chances de ser correcta, independientemente de la puerta que abra el organizador.

Ahora, supongamos que en la elección inicial elegimos una puerta que no contiene el premio ( 66% de probabilidades). La estrategia de no cambiar de puerta nos hace perder indiscutidamente.

Si juntamos las dos proposiciones obtenemos que no cambiar de puerta nos hace ganar 1/3 de las veces, cuando elegimos bien por azar la puerta del premio inicialmente, y nos va a hacer perder el resto de las veces - 2/3 de las veces - que es cuando elegimos una puerta sin premio al principio.

Otro razonamiento equivalente es que cambiar de puerta nos hacer perder siempre y cuando hayamos elegido la puerta del premio originalmente (1/3) pero nos va a hacer ganar siempre que hayamos elegido una sin premio (2/3) porque la nueva puerta si o sí tendrá el premio, ya que la tercera es la que abre el organizador y no tiene premio.

En caso de que la rápida intuición nos hiciera creer que la elección entre cambiar y no cambiar era indistinto y ambas tenían 50% de chances de garantizarnos el premio, el ejercicio de simulación nos hubiera hecho elegir correctamente.

En este caso razonar el problema es posible ya que involucra pocas opciones pero en situaciones más complejas la simulación puede ayudar enormemente a la toma de decisiones.


