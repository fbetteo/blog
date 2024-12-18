---
title: Funciones de Probabilidad y Distribucion
authors:
  - fbetteo 
date: 2019-04-03
slug: funciones-de-probabilidad-y-distribucion
categories:
  - estadistica
  - R
tags:
  - estadistica
  - R
thumbnailImage: https://lh3.googleusercontent.com/5h93ms-7zsiAIgfCwUz2BKGQ1YoLgrvd-IegYZOmqZeVA6hy4RBnP8lc_CEgQLNdWwwT-a60CwwiW2RJ6A=w287-h176-rw
thumbnailImagePosition: left
summary: Acerca de variables aleatorias y sus distribuciones.
---

# Funciones de Probabilidad y Distribucion

## Variables Aleatorias

Consideremos un experimento cuyo espacio muestral denominaremos ` S `.   
Una funcion valuada en el dominio de los reales definida en `S` es una variable aleatoria. 

En otras palabras es una función que asigna a cada resultado posible de un experimento un valor real.

Por ejemplo:

>  Si el experimento es lanzar una moneda 10 veces hay 2^10^ combinaciones posibles de caras (o) y cruz (x).  
>  Si definimos la variable aleatoria X como cantidad de caras entonces X(s) será la cantidad de caras del experimento.  
>  Si s resulta ser la secuencia `ooxxxoxxxo` entonces X(s) = 4.


## Distribucion de una variable aleatoria

Si tenemos la distribución de probabilidad del espacio muestral del experimento podemos determinar la distribución de probabilidad de cualquier variable aleatoria válida.

Volviendo al ejemplo de la moneda. Dijimos que hay 2^10^ combinaciones de cara o cruz.
La cantidad de combinaciones de X caras en 10 lanzamientos es $P(X = x) = \binom{n}{x} \frac{1}{2^{10}}$  para $x = 0,1,2,..,10$

## Distribuciones Discretas

Una variable aleatoria tiene una distribución discreta si solo puede tomar valores de una secuencia (generalmente finita pero puede no serlo). 

* La función de probabilidad le otorga una probabilidad puntual a cada valor de esa secuencia.
* Los valores por fuera de la secuencia tienen probabilidad  = 0
* La suma de todas las probabilidades tiene que ser 1

### Distribución Uniforme

En el caso de la dsitribución uniforme, supongamos que la variable puede tomar valores de 1 a k.
La función de probabilidad será $f(x) = \frac{1}{k}$ para x = 1,2,...,k. 
Y 0 para todos los otros valores.

> si k = 10  
> Los valores de la variable serán cualquier entero entre 1 y 10  
> Cada valor tendrá probabilidad $\frac{1}{10}$


### Distribución Binomial

En el caso de la dsitribución binomial se asumen dos posibles resultados, uno con probabilidad *p* y su contraparte con probabilidad *1-p*.  
Por ejemplo la probabilidad p de que una máquina genere un producto defectuoso y 1-p de que sea no defectuoso.  
Si una máquina produce *n* productos va a generar X productos defectuosos. La variable aleatoria X tendrá una distribución discreta y sus posibles valores irán de 0 a n.  
Para cualquier valor de x (entre 0 y n), la probabilidad de que la máquina genere x productos defectuosos entre los n producidos (de una secuencia particular) es $p^{x}q^{(n-x)}$  
Como existen $\binom{n}{x}$ distintas secuencias posibles con x defectuosos entre los n productos tenemos que:  
$Pr(X = x) = \binom{n}{x}p^{x}q^{(n-x)}$  
La función de probabilidad será $f(x) = \binom{n}{x}p^{x}q^{(n-x)}$ para x = 0,1,2,...,n. 
Y 0 para todos los otros valores.

Para usar esta distribución en R tenemos los siguientes comandos:

* Para generar *n* escenarios al azar donde se producen *size* productos con probabilidad *p* de ser defectuosos.
El resultado es la variable x por escenario. Es decir la cantidad de defectuosos.  
En el primer escenario x = 0, en el segundo x = 1 y así.

```r
set.seed(1)
rbinom(n = 10, size = 5, p = 0.2 )
```

```
##  [1] 0 1 1 2 0 2 3 1 1 0
```

```r
# random binomial
```

* Para saber la probabilidad de obtener *x* productos defectuosos si una máquina produce *size* productos y la probabilidad de que produzca un defectuoso es *prob*.  
Hay probabilidad de 0.0264 de obtener 5 defectuosos si producimos 10 con probabilidad 0.2.


```r
dbinom(x = 5, size = 10, prob = 0.2)
```

```
## [1] 0.02642412
```

* Para saber la probabilidad acumulada de obtener *q* **o menos** productos defectuosos si la máquina fabrica *size* objetos, con probabilidad de defecto *prob*.
Hay probabiliad de 0.879 de obtener 3 o menos defectuosos si la máquina produce 10 objetos con probabilidad 0.2 de defecto.
Es decir, es la suma de obtener exactamanete 0 defectuosos, más exactamente 1 defectuoso, más exactamnente 2 defectuosos, más exactamente 3 defectuosos.

```r
pbinom(q = 3, size = 10, prob = 0.2)
```

```
## [1] 0.8791261
```

## Distribuciones Continuas

Una variable aleatoria X tiene una distribución continua si existe una función `f` definida en los reales tal que para algún intervalo A  
$Pr(X \in A) = \int_{A} f(x)$  

La función `f` es la *función de densidad de probabilidad*. PDF por sus siglas en inglés.  
La probabilidad de que X tome algún valor en un intervalo se encuentra integrando `f` en ese rango.


Por ejemplo para la distribución uniforme en un intervalo *(a,b)* podemos ver que su pdf (o función de densidad de probabilidad) es  
$f(x) = \begin{cases}\frac{1}{b-a} & \text{para } a \leq x \leq b \\ 0 & \text{resto}\\  \end{cases}$

### Distribución Normal

Para la distribución Normal tenemos los siguientes comandos:  

* Para obtener *n* variables aleatorias provenientes de una normal con media *mean* y desvío *sd*

```r
set.seed(1)
rnorm(n = 5, mean = 10, sd = 2)
```

```
## [1]  8.747092 10.367287  8.328743 13.190562 10.659016
```

* Para obtener el valor de la pdf de la normal para algún valor de X en particular.
Recuerden que no es una probabilidad, solo es el valor de la función. Las probabilidad se encuentra integrando la función en el intervalo deseado.  
Si graficáramos los valores de dnorm para el intervalo -3,3 obtendríamos la forma típica de la normal.

```r
dnorm(0.5, mean = 0, sd = 1)
```

```
## [1] 0.3520653
```

* Para obtener la probabilidad acumulada hasta determinado punto. También conocido como *Función de Distribución* o *Función de Distribución Acumulada* **C.D.F. por sus siglas en ingles**
Por ejemplo, cual es la probabilidad de obtener un valor igual o menos a 1.5 si tomamos una muestra de una normal estándar 

$N \sim (0,1)$

```r
pnorm(q = 1.5, mean = 0, sd = 1)
```

```
## [1] 0.9331928
```

Hay 93.31% de chances de obtener un valor inferior a 1.5 si tomamos una muestra al azar de una normal con media 0 y desvío 1.

* La inversa también se puede calcular facilmente en R. Que valor debe tomar la variable aleatoria normal si deseo tenes un 93.31% de chances de obtener un valor menor o igual a ese?


```r
qnorm(p = 0.9331, mean = 0, sd = 1)
```

```
## [1] 1.499284
```
La diferencia respecto al código anterior es porque redondeamos la probabilidad.

 

 
