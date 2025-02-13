---
title: "De R a Python 1"
authors:
  - fbetteo 
date: 2020-07-11
output:
  html_document:
    df_print: paged
slug: de-r-a-python-1
tags:
- R
- Python
categories:
- R
- Python
thumbnailImage: https://lh3.googleusercontent.com/nfHMd9voBvXDKziowr-dYKDIPTQwb0og9vQ3GUdbEyIt95UTfag3ajjsGJcoB-HCC2tt683hiZ8Xo2vVEw=w328-h153-rw
thumbnailImagePosition: left
summary: Aprendizajes y recordatorios de la transicion de R a Python.
---


# De R a Python 1

Serie que documenta cuestiones prácticas que voy descubriendo a medida que empiezo a incursionar en Python un poco más enserio.
Son más que nada recordatorios para el futuro de mecánicas que hoy entiendo, pero me voy a olvidar.


Muchos de los objetos no van a tener relación entre sí o no se puede correr el código directo 
ya que son copy/paste random de scripts.

### Usar objetos de otros scripts

Si uno genera modelos, dataframes, etc en otro script por prolijidad y quiere utilizarlos en 
el principal (o cualquiera en realidad) lo aconsejable es exportarlo como objeto pickle (algo 
asi como los RDS en R.)



```r
library(reticulate)
```



```python
import pickle
import pandas as pd

# exportar. Objeto, archivo, permisos
pickle.dump(OBJETO, open("working/qualifying.p", "wb"))

# importar
leer = pd.read_pickle('archivo.p')
```

### Seleccionar columas de dataframe por patrón en el nombre

Para seleccionar columnas basados en si contiene determinado string en su nombre y no solo por nombre
completo o por índice. 


```python
# Recordemos que iloc selecciona por índice
# Función Lambda  que convierte el indice de columna en strings y devuelve mascara (True/false)
# si contiene determinado patrón. Creo que puede ponerse cualquier Regex
df2 = df.iloc[:, lambda df:df.columns.str.contains('_points')] # select column based on name
```

Si queremos combinar esto con otras columnas con otro patrón no encontré manera más sencilla por
el momento que combinar por separado. Quizás es muy tedioso si son muchas.


```python
# Notar que en point_vars le pasamos la máscara al listado de columnas nuevamente
# para quedarnos con el nombre real y poder sumarlo a las otras listas
# luego lo convertimos en lista porque el objeto es de tipo índice si no.
target = ['position']
qualy_vars = ['grid', 'dif_to_min_perc']
point_vars = list(results.columns[results.columns.str.contains('_points')])

vars_keep = target + qualy_vars + point_vars
```

### Juntar dataframes por indice

Los DF vienen por default con un índice. Si uno trabaja con una copia del DF original para generar nuevas columnas el índice se mantiene (si no lo reseteamos claro). También útil si se tienen varias tablas con mismo índice.

Esto permite juntar tablas sin tener que hacer un merge explicito por determinadas columnas si no
tenemos esos keys.


```python
results = results.join(driver_points_merge) # join by index (no need to merge with column)
```

### Ifelse

El equivalente de IFELSE en R para rapidamente crear una columna basado en otras, fila por fila.


```python
import numpy as np
#               = condicion, valor si True, valor si False
df['position'] = np.where(df['position'] > 1, 0, 1)
```

### Dropear columna de DF

Útil para asegurar que sacan el target de las X...

```python
X = df.drop(columns="position")
```


### Remplazar determinado valor por NaN (u otro)

df.replace

```python
qualifying = qualifying.replace('\\N', np.nan)
```


### APPLY. Aplicar funciones a cada fila o columna

Permite aplicar una función por fila o columna.La funcion se aplica sobre la serie (la fila o columna)
La serie mantiene los indices. Si usamos apply con axis = 1 que cada serie es una fila entera, 
podemos llamar a la celda correspondiente usando ['columna']


Apply es como las distintas versiones de apply de R y/o MAP del tidyverse cuando se aplica a un DF.


```python
import pandas as pd
rectangles = [
    { 'height': 40, 'width': 10 },
    { 'height': 20, 'width': 9 },
    { 'height': 3.4, 'width': 4 }
]

rectangles_df = pd.DataFrame(rectangles)
rectangles_df


# Suma de todas las celdas ("filas") por columna
```

```
##    height  width
## 0    40.0     10
## 1    20.0      9
## 2     3.4      4
```

```python
suma_por_columna = rectangles_df.apply(sum)
print(suma_por_columna)

# Suma de todas las celdas ("columnas") por filas
```

```
## height    63.4
## width     23.0
## dtype: float64
```

```python
suma_por_fila = rectangles_df.apply(sum, axis = 1)
print(suma_por_fila)
```

```
## 0    50.0
## 1    29.0
## 2     7.4
## dtype: float64
```
### Apply Lambda para pasar funciones custom en el momento



```python
import pandas as pd
rectangles = [
    { 'height': 40, 'width': 10 },
    { 'height': 20, 'width': 9 },
    { 'height': 3.4, 'width': 4 }
]

rectangles_df = pd.DataFrame(rectangles)

def multiplicar_2(x):
   return x*2

# Caso donde paso una funcion propia predefinida
rectangles_df.apply(multiplicar_2)


# Lo mismo pero definido en el momento
```

```
##    height  width
## 0    80.0     20
## 1    40.0     18
## 2     6.8      8
```

```python
rectangles_df.apply(lambda x: x*2)
```

```
##    height  width
## 0    80.0     20
## 1    40.0     18
## 2     6.8      8
```


### Calculos by group

Como el bygroup de tidyverse.


```python
# Equivalente a  groupby(raceid) %>% summarise(newcol = min(best_qualy_ms))
min_qualy_by_race = qualifying.groupby('raceId')['best_qualy_ms'].min()
```

### By Group más complejo, con calculo acumulado en determinada ventana de obs. por cada fila

```python
# suma acumulada de los ultimos 4 periodos (rolling)
# luego el gorupby(level = 0).shift() es para lagearlo por grupo
# el ultimo reset_index es para quitar el indice de este ultimo agrupado
driver_points.groupby('driverId')['points'].rolling(4, min_periods = 4).sum().groupby(level = 0).shift().fillna(0).reset_index(level = 0)['points']
```

