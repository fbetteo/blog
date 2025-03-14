---
title: Esencia del Algebra Lineal
authors:
  - fbetteo 
date: 2019-04-20
slug: esencia-del-algebra-lineal
categories:
  - matematica
  - algebra
tags:
  - estadistica
  - matematica
  - algebra
keywords:
  - tech
thumbnailImage: https://lh3.googleusercontent.com/sWpCiFddZKPHyUrzNS4TasP1fsyr_hLxm_s7Jzr61YjYl02Dt77DvrlFxS4FBsv6NqNjo5rCDtMh2irTgg=w300-h168-rw
thumbnailImagePosition: left
summary: Notas a modo de resumen de la serie de videos Essence Of Lineal Algebra.
---

# Esencia del Algebra Lineal

El álgebra lineal está por todas partes en estadística y data science. Matrices, vectores y transformaciones son términos que se escuchan seguido y están detrás de muchos de los métodos y algoritmos que se usan hoy por hoy. Aunque no sea necesario saber del tema para correr un modelo empaquetado en una librería de R, es muy útil entender lo que hacemos realmente ya que nos permite ver a los modelos como algo lógico y no una caja negra mágica.

Hay una serie de videos excelente en inglés que mediante visualizaciones y animaciones permite entender la intuición de muchos de los conceptos básicos, que solo con un libro puede ser medio críptico o poco imaginable.
Para el que le interese: [ESSENCE OF LINEAR ALGEBRA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) por 3Blue1Brown.

Este post, aunque quizás medio desordenado y sin mucha prolijidad, es una recopilación de algunas notas. Puede que queden términos en inglés intercalados.

## Matrices y vectores

* Vector vive en *n* dimensiones.
* Suma de vectores es combinación lineal
* En $R^{2}$ $\hat \imath = \left< 1, 0 \right> \text{y} \hat \jmath = \left< 0, 1 \right>$ forman una base. Cualquier punto es una combinación lineal de ellos.     
* Span es el espacio que pueden generar x vectores. $R^{2}$ es el span de  $\left< 1, 0 \right> \left< 0, 1 \right>$
* Vector puede ser pensado como una flecha desde el origen (0,0) a las coordenadas que lo identifican. O como un punto directo en las coordenadas..
* Matriz es una transformación. Lleva un vector a otro punto. Si transformamos cada posible vector de un espacio por la matriz podemos ver como el espacio es transformado. Ej: rotar, invertir, estirar.
* Si transformamos una base, cada punto nuevo puede generarse transformando la nueva base.   
Por ej: $z = \left< 3, 2 \right> \text{es } 3\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 2\begin{bmatrix} 0 \\ 1 \end{bmatrix} = 3\hat \imath + 2\hat \jmath$  
Aplicando la transformación de la matriz A = $\begin{pmatrix} A & B \\ C & D \end{pmatrix} \text{obtenemos los nuevos vectores base } \hat \imath^{*} \text{y } \hat \jmath^{*}$  
$z^{*} = 3\hat \imath^{*} + 2\hat \jmath^{*}$ 
* Multiplicar 2 matrices es transformar un espacio con la primera matriz ( desde la derecha) y luego transformar el resultado por la segunda matriz. Ej: Rotar un espacio y luego invertirlo.
* AB != BA -> El orden de las transformaciones importa y se lee de derecha a izquierda.
* La matriz (transformación) ya dice como van a ser las nuevas bases.  
Si la matriz es $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$, el nuevo $\hat \imath^{*}$ es $\begin{bmatrix} A \\ C \end{bmatrix}$ y $\hat \jmath^{*}$ es $\begin{bmatrix} B \\ D \end{bmatrix}$  
Ej: $z = \left< 3, 2 \right>  z^{*} =  \begin{bmatrix} A & B \\ C & D \end{bmatrix}\begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 3A + 2B \\ 3C + 2D \end{bmatrix}$  
Se puede ver también como:  $$z = 3\hat \imath + 2\hat \jmath \text{  }  z^{*} = 3\hat \imath^{*} + 2\hat \jmath^{*} = 3\begin{bmatrix} A \\ C \end{bmatrix} + 2\begin{bmatrix} B \\ D \end{bmatrix} = \begin{bmatrix} 3A + 2B \\ 3C + 2D \end{bmatrix}$$
&nbsp;

* !!!. Las transformaciones afectan el area (en R2, el volumen en R3..) de las figuras en el espacio (todas por igual). El *DETERMINANTE* de una matriz mide ese cambio.
* Si el determinante **es 0** significa que se perdió una dimensión o que todo se comprimió. Pasa de $R^{2}$ a una recta (o a un punto!)
* Si el determinante ** es < 0** significa que el espacio se invirtió (en sentido.. como dar vuelta una hoja) pero |DET| siguen siendo el cambio en el area.
* A^-1^A = I -> una transformación que no hace nada.
* Si DET(A) = 0 no existe la matriz inversa. Ej. $R^{2}$ -> si det(A) = 0 la transformación lleva el espacio a una recta. No hay función que lleve cada vector de la recta a un punto en $R{2}$. No hay vuelta atrás.
&nbsp;
&nbsp;

* Si una transformación lleva todos los puntos a una recta tiene rango 1, si lleva a un plano rango 2, y así.. **RANGO** es el número de dimensiones del output. Rango completo es cuando mantiene las dimensiones del input.
* El conjunto de posibles outputs de $A\vec v$ es el Column Space = Span de las columnas
* Cuando perdés dimensiones por la transformación todo un conjunto de vectores pasa a ser (0,0). Eso se llama **Null Space** o **Kernel**
* Matrices no cuadradas cambian la dimensión del espacio.  
$$ \begin{bmatrix} A & D \\ B & E \\ C & F \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} A + D \\ B + E \\ C + F \end{bmatrix} $$ 
Quedan todos los puntos de $R^{2}$ en un plano en el espacio $R^{3}$. De acá viene la restricción para multiplicar matrices. La cantidad de columnas de la transformación tiene que ser igual a la dimensión del input

### DOT PRODUCT o PRODUCTO INTERNO

* Dot product entre dos vectores equivale a proyectar uno en el otro y multiplicar sus largos. $\vec A \cdot \vec B = |A^{*}| * |B|$  
$A^{*}$ es el vector A proyectado en B.
* $\vec B$ es un vector 2D pero también se lo puede ver como una matriz 1x2 que lleva del 2D a la recta.  
$\vec B \cdot \vec A = B \vec A \text{que sería llevar A al espacio transformado por B.}$  
$B = \begin{bmatrix} B_x & B_y \end{bmatrix}$ tiene en sus columnas donde queda $\hat \imath \text{y } \hat \jmath$ (los vectores unitarios) al ser transformados o algun valor escalado de esto.  
$\vec A \cdot \vec B$ es el valor de A en la recta a la que te lleva la transformación B.
* Es equivalente proyecto B en A.
* Si Dot Product > 0, tienen dirección similar.
* Si Dot Product = 0, son ortogonales - proyección que cae en el origen.
* Si Dot Product < 0, tienen direcciones opuestas.

&nbsp;
&nbsp;

### CROSS PRODUCT

* Está definido para vectores en $R^{3}$
* El cross product $\vec u \times \vec v$ es el area del paralelograma que se puede imaginar con las paralelas de los vectores (imaginandolo en $R^{2}$. El signo depende de la orientación de los vectores. El vector de la "derecha" tiene que estar primero para que el cross product sea > 0.
* En realidad el paralelograma formado por dos vectores en R^3^ tiene area equivalente al **Largo** del vector output de su cross product. Ese vector es ortogonal al paralelograma.

&nbsp;
&nbsp;

### CAMBIO DE BASE

* Distintos sistemas de coordenadas definen $\hat \imath = \left< 1, 0 \right>, \hat \jmath \left< 0, 1 \right>$ como algo distinto. **NO** hay una sola "grilla" válida. El espacio no tiene grilla predeterminada.
* Un mismo vector tiene distintas coordenadas según el sistema de bases desde donde se lo mire.
* Para pasar de una base a otra se aplica una transformación lineal.  
Si $\vec v$ es un vector que queremos pasar de una base a otra, lo transformamos por la nueva base.  
Y $\hat \imath^{*} =  \left< \hat \imath^{*}_1, \hat \imath^{*}_2 \right>, \hat \jmath^{*} =  \left< \hat \jmath^{*}_1, \hat \jmath^{*}_2 \right>$
Entonces:
$$\begin{bmatrix} \hat \imath^{*}_1 & \hat \jmath^{*}_1 \\ \hat \imath^{*}_2 & \hat \jmath^{*}_2 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} v^{*}_1 \\ v^{*}_2 \end{bmatrix}$$  
Donde $\begin{bmatrix} v^{*}_1 \\ v^{*}_2 \end{bmatrix}$ es el vector en la nueva base, es decir, serían las coordenadas del vector $\vec v$ en el nuevo sistema de coordenadas y representando ese punto bajo el sistema de coordenadas original. -> Como se vería $\vec v$ en la nueva base? desde un punto de vista de la base original.  
La matriz transforma un vector siguiendo en el lenguaje de la base original.  
Ej: Si $\vec v$ es (1,2) en el sistema cartesiano típico y aplicamos la matriz de cambio de base, un vector (1,2) bajo otros ejes se ubicaría en otro punto del espacio. Qué punto es ese bajo el sistema cartesiano? Es (1,2) en el nuevo, pero queremos saber su equivalente en el sistema original.
* Por otra parte si queremos saber que coordenadas tomaría el vector $\vec v$ bajo otra base debemos multiplicar por la inversa de la transformación. Transforma el vector al lenguaje de la nueva base.
Responde a la pregunta. Qué coordenadas toma el punto V_1, V_2 del espacio en el sistema nuevo?
&nbsp;
* Para aplicar una transformación a otra base conviene llevar el vector a transformar a la base original, transformar y reconvertir a la nueva base.
$$ [A]^{-1}[T][A]\vec v = \vec v^{*}$$  
A lo expresa en términos de la base original, luego se le aplica la transformación T y luego se lo devuelve al lenguaje de la nueva transformación.

&nbsp;
&nbsp;

### Eigenvalues y Eigenvectors (autovalores y autovectores)

* !!! Al aplicar una transformación lineal a un espacio algunos vectores no cambian de dirección, solo se estiran o contraen pero sobre la misma recta. El resto sí se mueve. Los que se mantienen son los eigenvectors, y su factor de expansión o contracción es su eigenvalue.  
Si A es la matriz de transformación, $\vec v$ es un eigenvector y $\lambda$ su eigenvalue.
$$ A\vec v = \lambda \vec v$$  
* Si una transformación es una matriz diagonal, lo único que hace es estirar $\hat \imath \text{y } \hat \jmath$ por lo tanto los vectores base son eigenvectors y la diagonal son los eigenvalues.
* Si cambiamos la base a una formada por los eigenvectors (que spanean el espacio) de la matriz podemos aplicar la transformación (la matriz original de donde salieron los eigenvectors) a esta nueva base y solo la va a estirar, por lo tanto es una transformación diagonal, que permite calculos mucho más fácil. Después habría que volver a la base original.  
A -> Matriz de transformación
E -> Matriz de autovectores que forman la nueva base $\begin{bmatrix} e_11 & e_21 \\ e_12 & e_22 \end{bmatrix}$
D -> Matriz Diagonal cuyos valores son los eigenvalues
$$ E^{-1}AE=D$$

E cambia la base a eigenvectors (expresado en la base original), A aplica transformación y E^-1^ lo lleva al lenguaje de la nueva base (queda expresado en las nuevas coordenadas)
&nbsp;
&nbsp;
### Espacios Vectoriales Abstractos

* !!! Ver *funciones* como un tipo especial de vectores.
* Las funciones se pueden sumar y escalar $f(x) + g(x) \text{y } 2f(x)$
* Existen transformaciones lineales de funciones, convierten una función en otra. También conocidas como "operadores"
* Para que una transformación sea lineal tiene que cumplir aditividad y mulitplicación por escalar  
$$ L(\vec v + \vec  w) = L(\vec v) + L(\vec w)$$
$$ L(c\vec v) = cL(\vec v)$$
* En general cualquier espacio que cumpla los axiomas los espacios vectoriales puede ser considerado uno.
