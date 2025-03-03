---
title: "Hola MAP. Chau Apply."
authors:
  - fbetteo
date: 2018-09-01
output:
  blogdown::html_page:
    toc: true
    depth: 3
slug: hola-map-chau-apply
tags:
- tidyverse
- R
categories:
- R
coverImage: https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/images/649694main_pia15417-43_full.jpg
thumbnailImage: https://lh3.googleusercontent.com/LMR8eyUF0ocCRmnCsqfcD_z2JM1YH78BZkkh-Rza3-S3irCmThYSMC_n3wTbyTenXn74_AOSnZJjS5INCg=w191-h220-rw
thumbnailImagePosition: left
summary: "La idea de este post es introducirlos a la familia de funciones **MAP**, propias de [tidyverse](https://www.tidyverse.org/)."
---

# Hola MAP. Chau Apply

## Introducción

La idea de este post es introducirlos a la familia de funciones **MAP**, propias de [tidyverse](https://www.tidyverse.org/).
A grandes rasgos son un remplazo MUY útil a la familia de funciones **APPLY**, propias de R base. Estas últimas se suelen enseñar en todos los cursos introductorios de R, como la manera correcta de aplicar funciones a listas o columnas de dataframes. 
No es que no sirvan, pero dado el surgimiento de tantas librerías que facilitan el manejo de la data, no tiene sentido seguir insistiendo con ellas dado que hay nuevas con mayor flexibilidad, muy sencillas de utilizar y mucho más amenas.

* Lo mejor que tienen las funciones MAP es:
    + Consistencia en los inputs.
    + Flexibilidad del output.
    + Integración con todo el universo tidyverse y prolijidad.

Empecemos.


```r
library(purrr) # MAP está contenida acá
library(dplyr)
```

```
## Warning: package 'dplyr' was built under R version 4.0.5
```

Como regla general, MAP aplica funciones a elementos de una lista o de un vector.
Su output es otra lista. Muy similar a lapply().


```r
l1 <- list( a= c(100,200), b = c(8,10))
map(l1, max)
```

```
## $a
## [1] 200
## 
## $b
## [1] 10
```
A cada lista le calcula el máximo y devuelve una lista con cada elemento siendo el resultado de la función.


Tenemos la flexibilidad para pasarle funciones anónimas..


```r
map(l1, function(x) max(x))
```

```
## $a
## [1] 200
## 
## $b
## [1] 10
```

Aplicando funciones a elementos de un vector.
Cada numero de 1 a 5 es usado como primer input de la funcion *rnorm*, sd y n son otros parámetros de rnorm.
El resultado de nuevo es una lista.

```r
set.seed(1)
1:5 %>% map(., rnorm,sd =2, n=5)
```

```
## [[1]]
## [1] -0.2529076  1.3672866 -0.6712572  4.1905616  1.6590155
## 
## [[2]]
## [1] 0.3590632 2.9748581 3.4766494 3.1515627 1.3892232
## 
## [[3]]
## [1]  6.023562  3.779686  1.757519 -1.429400  5.249862
## 
## [[4]]
## [1] 3.910133 3.967619 5.887672 5.642442 5.187803
## 
## [[5]]
## [1] 6.837955 6.564273 5.149130 1.021297 6.239651
```

  
## Consistencia entre variantes

Por ahora solo vimos la versión de lapply en MAP, pero esta familia tiene varios integrantes.

## map_if

Ejecuta la función solo si el elemento cumple determinada condición.
Devuelve una lista.


```r
l2 <- list(a = 213, b = "string", c = c(1,2))
map_if(l2, is.numeric, function(x) x*2)
```

```
## $a
## [1] 426
## 
## $b
## [1] "string"
## 
## $c
## [1] 2 4
```
El output es la lista original con los elementos correspondientes transformados. Vemos que no hubo ningún problema con
"string" ya que fue omitido.


## map_at

Ejecuta la función solo en los elementos que seleccionemos. No hace falta que cumplan alguna condición.
Misma función de antes pero solo aplicada al tercer elemento. Devuelve una lista.


```r
map_at(l2, c(3), function(x) x*2)
```

```
## $a
## [1] 213
## 
## $b
## [1] "string"
## 
## $c
## [1] 2 4
```

Variantes súper útiles que permiten no utilizar loops y que dan mucho control de manera sencilla sobre las funciones a ejecutar. Por otra parte, en términos de consistencia, la estructura es siempre la misma. El primer argumento es x= y luego viene la función a aplicar. En el caso de map_if y map_at entre medio surge el condicionante.
Si recuerdan, la familia apply cambia el orden de los inputs según si es apply, lapply, mapply, sapply...

# Flexibilidad del output

Por el momento vimos que todos los outputs eran listas. Lo interesante es que podemos controlar eso y cambiar el formato del resultado, ahorrándonos conversiones molestas con *unlist* y etc.


```r
l3 <- list(c(1,2,4), c(100,200), c(5000,6000))
map_dbl(l3, max)
```

```
## [1]    4  200 6000
```

Nos devuelve un vector con los resultados de aplicar la función max a cada elemento!

De este mismo tipo esta.

* map_chr # vector caracter
* map_int # vector de integers
* map_lgl # vector de booleanos






