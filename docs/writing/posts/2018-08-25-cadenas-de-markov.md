---
title: Cadenas de Markov
authors:
  - fbetteo
date: 2018-08-25
slug: cadenas-de-markov
categories: 
- matematica
tags: 
- r
- matematica
- cadenas de Markov
thumbnailImage: https://lh3.googleusercontent.com/s7OEWbiAksJIlBfh1h3Lv5qu3yjL8hfM3d_-INh41ZYLC5I4Q3ti9UbjZp7BlYElBd4NXc_3bloR2Z9Bog=w447-h220-rw
thumbnailImagePosition: bottom
summary: Introducción a las cadenas de Markov. Ejemplo ilustrativo para ver su gran potencial.
---

# Cadenas de Markov

Las cadenas de Markov son herramientas muy útiles para modelar transiciones entre estados. Imaginemos un escenario sencillo con dos posibles estados: día de lluvia o día soleado. En el momento **t** el estado supongamos que es "día soleado". ¿Cuál será el estado en **t+1** ? Dadas las probabilidades de transición de un estado a otro podemos simular escenarios tras el paso del tiempo. Mismo en algunos casos puede ser útil entender si en el largo plazo esta simulación converge hacia algún resultado estable en el tiempo.

Mostraremos ejemplos sencillos, pero la metodología es escalable a procesos complejos como pueden usarse en meteorología, aplicaciones financieras, etc. El [algoritmo de búsqueda de Google](http://blog.kleinproject.org/?p=1605&lang=es) está basado en cadenas de Markov, para que vean la utilidad. [^1]

Lo que necesitamos para este ejercicio son las probabilidades de transición de un estado a otro y los valores iniciales en cada estado.

Supongamos una clase de estadística con n estudiantes, en la que dos estados son posibles. 
Estado A : El alumno está atento.
Estado B : El alumno está aburrido.

* Las probablidades son las siguientes: 
    + En t+1 el 80% de A sigue en A (y por lo tanto el 20% de A pasa a B)
    + En t+1 el 25% de B pasa a A (y por lo tanto el 75% de B queda en B)
    
La matriz que representa esa probabilidades la vamos a llamar * Matriz de Transición *.


```r
tmatrix <-  as.matrix(c(0.8,0.25))  
# 80% de A sigue en A, 25% de B pasa a A en t+1

tmatrix <- t(tmatrix) 
# trasponemos porque necesitamos esta información en la primera fila.

tmatrix <- rbind(tmatrix, 1 - tmatrix[1,]) 
# Agregamos la segunda fila, que es 1 menos la primera.

tmatrix # Matriz de transción
```

```
##      [,1] [,2]
## [1,]  0.8 0.25
## [2,]  0.2 0.75
```

La matriz de valores iniciales es la siguiente:
En un primero momento (t), el 10% de los alumnos está atento y el 90% aburrido.


```r
smatrix <- as.matrix(c(0.1,0.9)) # Matriz inicial, 10% Atento, 90% aburridos
```


Ya tenemos toda la información necesaria para hacer nuestras primeras simulaciones.
Supongamos que cada período de tiempo son 10 minutos, por lo tanto si t es el momento 0, t+1 es a los 10 de minutos de empezada la clase, t+2 a los 20 y así sucesivamente.

Para evaluar el porcentaje de alumnos concentrados en determinado momento de la clase lo que debemos hacer es multiplicar la matriz de estado inicial por la matriz de transición tantas veces como momentos a futuro querramos simular.

Por ejemplo si queremos ver que pasará con nuestros alumnos luego de 20 minutos de clase debemos multiplicar smatrix * tmatrix 2 veces.


```r
for (i in 1:2){            # Loopeamos 2 veces. %*% es la multiplicacion matricial.
  smatrix = tmatrix %*% smatrix  
# smatrix va tomando nuevos valores en cada iteracion, 
# reflejando el movimiento de un estado a otro
}

smatrix  # Despues de 2 iteraciones -> A 42% , B 58%
```

```
##         [,1]
## [1,] 0.41775
## [2,] 0.58225
```

Vemos que luego de 2 transiciones el estado A está compuesto por casi 42% de alumnos (concentrados) y 58% no atentos. Son movimientos bastante rápidos de un estado a otro.

Veamos qué pasa luego de 10 iteraciones.



```r
smatrix <- as.matrix(c(0.1,0.9)) # Reseteamos smatrix a su estado inicial

for (i in 1:10){           
# Loopeamos 10 veces. %*% es la multiplicacion matricial.
  smatrix = tmatrix %*% smatrix   
# smatrix va tomando nuevos valores en cada iteracion, 
# reflejando el movimiento de un estado a otro
}

smatrix  # Despues de 10 iteraciones -> A 55% , B 45%
```

```
##           [,1]
## [1,] 0.5544017
## [2,] 0.4455983
```

Luego de 10 movimientos, A pasa a tener el 55% de los alumnos dejando a 45% en B (no atentos). En este ejemplo con el paso del tiempo los alumnos se concentran más y más en la clase. Pero es este un proceso continuo e infinito? Llega un momento en que dada la matriz de transción todos los alumnos pasan a estar en el estado A, es decir, atentos?

Para analizar esto podemos ver qué sucede luego de 1000 iteraciones (sería una clase muy muy larga...)



```r
smatrix <- as.matrix(c(0.1,0.9)) # Reseteamos smatrix a su estado inicial

for (i in 1:1000){  # Loopeamos 10 veces. %*% es la multiplicacion matricial.
  smatrix = tmatrix %*% smatrix  
# smatrix va tomando nuevos valores en cada iteracion,
# reflejando el movimiento de un estado a otro
}

smatrix  # Despues de 1000 iteraciones -> A 55% , B 45%
```

```
##           [,1]
## [1,] 0.5555556
## [2,] 0.4444444
```

El resultado es casi idéntico luego de 1000 iteraciones al intento de tan solo 10 iteraciones. Por lo tanto podemos ver que esta cadena de Markov converge rápidamente a 55% en A y 45% en B. Es un estado estacionario del cual no podemos movernos dada la matriz de transición que tenemos.

Este ejemplo sencillo permite ver la intuición detrás de esta potente herramienta en unos pocos pasos. Obviamente como comentamos antes se puede utilizar para procesos mucho más complejos y de muy diversas areas. 
Queríamos mostrar los fundamentos con una aplicación rápida y que se comprenda que lo que se requiere es una matriz de transición y un estado inicial.

[^1]: Para una explicación gráfica y muy didáctica dejamos el siguiente [link en inglés.](http://setosa.io/ev/markov-chains/)
