---
title: Tipos de Variables
authors:
  - fbetteo 
date: 2018-08-25
slug: tipos-de-variables
categories:
- estadistica
tags: 
- estadistica
thumbnailImage: https://lh3.googleusercontent.com/AmqQCEfpjp8gRRtsLEwVZH3txNfRwEkRUKAWTgFEcNRnRtwl5z3m2hO7G4ByW_LwtTzEHMoGY7kPaHIBZg=w391-h220-rw
thumbnailImagePosition: left
summary: Tipos de variables más comunes en los datasets y ejemplos sencillos de ellos.
---

# Tipos de Variables


Las características de las variables que podemos encontrar en un dataset son muy diversas, pero general se pueden clasificar bajo alguno de los siguientes formatos.

**Categóricas** o **Cualitativas**

Corresponden a variables con *etiquetas* o valores pero que no siguen un orden específico o no tienen jerarquía.
Por ejemplo: color de ojos, género, sabor (dulce, salado, amargo), etc.
Para estas variables, que una observación corresponda a un valor u a otro no revela mayor importancia o mejor ponderación  sobre otra observación, son simplemente distintas.


```r
df <- as.data.frame(matrix(c("Persona1","Persona2","Persona3","Verde","Marron",
      "Azul",      1.8,1.87,1.65,"Secundario Completo", "Universitario Completo",
      "Sin estudios",3,2,1),nrow = 3, ncol = 5))
names(df) <- c("ID","Ojos","Altura","Estudios","Hijos")

df$Ojos
```

```
## [1] "Verde"  "Marron" "Azul"
```

Simulamos una tabla muy básica con 4 columnas por observación. Como ejemplo de variable categórica tomamos el color de ojos de estas personas. Y vemos que puede tomar los valores azul, marrón o verde. Más allá de los gustos personales, en principio estas etiquetas no revelan ningún orden, simplemente valores distintos según el individuo.

**Ordinales**

Corresponden a variables con *etiquetas* pero que en este caso sí tienen un orden establecido o jerarquía. Es decir que una etiqueta es "mejor" o tiene un valor más elevado. Por otra parte, en esta jerarquía o escala no podemos determinar cuánto mejor es una etiqueta por sobre otra, solo sabemos cómo se ordenan.

Volvemos al ejemplo de nuestra tabla. Este caso tomamos la columna Nivel de estudios.


```r
df$Estudios
```

```
## [1] "Secundario Completo"    "Universitario Completo" "Sin estudios"
```

Vemos que en nuestra tabla se pueden encontrar los valores "Sin estudios", "Secundario Completo" y "Universitario Completo". Podemos decir que esta columna presenta un orden lógico entre las distintas etiquetas y que Universitario completo es más deseable que Secundario Completo y este último a su vez más deseable que Sin Estudios. 
Por otra parte, no podemos definir concretamente cuánto más deseable una categoría sobre la otra. Es universitario Completo 2 veces mejor que Secundario completo? 1? 3?. Y esa "distancia", es la misma entre Secundario completo y Sin Estudios? No es clara amplitud.

**Cuantitativas Discretas**

Corresponden a variables numéricas que son *numerables*, es decir que podemos contar cuantos valores intermedios hay entre 2 valores cualquiera. Entre cada valor no hay infinitos posibles.
Siguiendo nuestra tabla, el ejemplo a tener en cuenta es el de número de hijos.


```r
df$Hijos
```

```
## [1] "3" "2" "1"
```

Cada persona puede tener entre 0 y digamos... 10 hijos para no ser tan extremistas. A su vez, no se pueden tener fracciones de hijo. Por lo tanto, entre 6 y 8 hijos, solo se pueden tener 7. No 7.4, ni 6.2. En ese sentido decimos que entre dos valores cualquiera podemos numerar los intermedios.

**Cuantitativas Continuas**

Corresponden a variables numéricas no numerables, es decir que entre 2 valores cualquiera, hay infinitos intermedios.
En nuestro ejemplo, podemos tomar la columna Altura para ilustrarlo.


```r
df$Altura
```

```
## [1] "1.8"  "1.87" "1.65"
```

En nuestro caso tenemos valores redondeados pero si tuviéramos valores más precisos, hay inifinitas posibilidades entre 1.7 y 1.8.
Este tipo de variables son muy comunes y se encuentran por todos lados. Temperatura, longitudes, etc.

