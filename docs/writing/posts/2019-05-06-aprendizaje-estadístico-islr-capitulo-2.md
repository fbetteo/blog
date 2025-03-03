---
title: Aprendizaje Estadístico - ISLR Capitulo 2
authors:
  - fbetteo 
date: 2019-05-06
slug: aprendizaje-estadistico-islr-capitulo-2
categories:
  - estadistica
tags:
  - estadistica
  - ISLR
  - Introduction Statistical Learning
summary: Resumen y notas del famoso libro Introduction to Statistical Learning de Hastie, Tibshirani et al. Capítulo 2. Aprendizaje Estadístico
thumbnailImage: https://lh3.googleusercontent.com/QUaX5TXvmk8N-uml7F_cponp-S1krhmSkhZJOVGJgj0bIAy-ZxcOHwwAX_eO3IYH1juyezDhDda9XFMlVw=w146-h220-rw
thumbnailImagePosition: left
---

# Aprendizaje Estadístico - ISLR Capitulo 2

Suponemos que las variables que encontramos en un set de datos son generadas a través de un proceso generador de datos (DGP por sus siglas en inglés) cuya expresión es: 
$$ Y = f(X) + \epsilon $$

Donde Y es la variable, en este caso la dependiente o la que queremos explicar. f(X) es una función respecto a otra/s variable/s X (independientes) y $\epsilon$ es el error irreducible, es decir un valor aleatorio con media 0 pero que no depende de otras variables, es al azar. Puede referir a errores de medición, cambios inmesurables en las situaciones del experimento o simplemente azar en la generación real de los datos. Cabe destacar que f(X) es desconocida para nosotros y justamente lo que queremos explorar con el análisis estadístico. Puede tenerse suposiciones o conocimiento de la forma funcional (lineal, no lineal, etc) pero en principio no tenemos mayores certezas y esperamos aprender a partir de la muestra que analizamos.

### Por qué estimar f(X)?

Los dos principales motivos para interesarse en f(X) son *predicción* (de Y) e *inferencia* de los parámetros de f(X).

#### Predicción

Queremos predecir valores de Y para nuevos datos X. Como $\epsilon$ en promedio es 0 podemos aproximar Y de la forma: 
$$ \hat Y = \hat f(X)$$
La precisión de $\hat Y$ va a depender del **error reducible** y del **error irreducible**. El primero depende de qué tan bien nos aproximemos a la verdadera f(X) y puede ser potencialmente reducido si utilizamos las técnicas más adecuadas para el caso. El segundo error es justamente irreducible y es porque nuestra aproximación no puede tener en cuenta a $\epsilon$. El término aleatorio introducido por esa variable no lo podemos estimar para cada observación y por lo tanto debemos convivir con ese margen de error.

Suponiendo que tenemos una estimación $\hat f$ y un set de datos X puede probarse que:
$$ E(Y - \hat Y)^2 = E[f(X) + \epsilon - \hat f(X)]^2$$
                   $$   \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \     = \underbrace{[f(X) - \hat f(X)]^2}_\text{Reducible} + \underbrace{Var(\epsilon)}_\text{Irreducible}$$
                   
Donde $E(Y-\hat Y)^2$ es el promedio o valor esperado de la diferencia al cuadrado del valor real de Y y de la predicción correspondiente.
$Var(\epsilon)$ es la varianza del término de error $\epsilon$.

#### Inferencia

Este enfoque se basa en entender la relación entre las variables de X y la dependiente. Es necesario entender bien la f(X) elegida para poder interpretar sus coeficientes y poder ver qué variables están asociadas con Y, cómo es esa relación, cuál es la forma de la función f(X), etc para poder actuar sobre las variables X o comprender su efecto aunque no siendo tan exigentes con el poder de predicción de nuestro modelo.

### Como Estimar f(X)?

#### Métodos Paramétricos

Los métodos paramétricos se conforman por dos etapas.  
La primera es asumir o suponer la forma funcional de f(X). Podes definir por ejemplo que f(X) es una función lineal de la forma
$$ f(X) = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_pX_p$$  

Una vez definida la forma del modelo la segunda etapa consiste en estimar los parámetros con algún método, a partir de los datos de entrenamiento. En este caso sería estimar todos los $\beta$. Por ejemplo para las funciones lineales se suele utilizar el método de *mínimos cuadrados ordinario*.  
La ventaja de definir una forma funcional es que luego es más sencillo estimar sus parámetro y el problema se reduce a eso finalmente. Por el otro lado, posiblemente la forma que elijamos no sea exactamente igual a la real (DGP) y tengamos que aceptar que va a haber errores debido a eso. Si estamos muy lejos de la forma real esos errores serán groseros. Existen modelos flexibles que permiten ajustar modelos con diferentes formas de f(X) pero en general requieren estimar más parámetros  y son más propensos a sufrir sobreajuste/overfitting que básicamente es ajustarse mucho al ruido o error ($\epsilon$) en los datos de entrenamiento y luego ajustar mal en testeo.  

#### Métodos No Paramétricos

Los métodos no paramétricos no requieren definir explícitamente una forma funcional de f. Buscan un f que sea lo más cercano posible a los datos sin ser demasiado estricto o flexible. Al no asumir una forma puede cubrir potencialmente un rango mucho mayor. El problema es que al no reducir el problema a estimar parámetros necesitan muchas más observaciones para estimar f de forma medianamente precisa. En general uno tiene que decidir el nivel de "suavidad" del modelo, lo cual afecta que tan variable termina siendo la estimación. Sirve para encontrar el punto de fleixibilidad/rigidez del modelo que queremos para que no sobreajuste (ni falle demasiado).

### Predicción vs Interpretabilidad

Uno puede elegir entre modelos flexibles o más rígidos. Con pocas observaciones a veces uno no puede alejarse mucho de los rígidos pero suponiendo que uno tiene muchos datos, a veces puede igualmente elegir rígidez frente a modelos flexibles que permiten ajustar varias formas de f. 
El motivo es que generalmente los modelos restrictivos son más fáciles de interpretar y se le puede dar un significado claro a sus coeficientes mientras que con formas muy flexibles no es sencillo entender el impacto de las variables de manera individual. La elección va a depender del objetivo del análisis y de qué tan bien o mal nuestros modelos ajustan a los datos.

### Modelos Supervisados vs No Supervisados

Nuestros datos pueden tener una variable dependiente que queremos explicar o predecir en base a un set de variables independientes, con algún modelo a definir. Los casos de este estilo son llamados *supervisados* porque sabemos la "respuesta" (nuestra variable Y) y podemos validar nuestros modelos contra la realidad.  
Si los datos no tienen una variable dependiente lo que se puede hacer es un análisis no supervisado donde por ejemplo lo que se puede hacer es agrupar las observaciones en clusters o grupos. Es decir segmentar en distintas clasificaciones y descubrir patrones. El desafío es que no hay en los datos nada contra qué validarlo, aunque sí contra el conocimiento del dominio o de la temática.


### Regresión vs Clasificación

En los modelos supervisados, nuestra variable dependiente puede ser *cuantitativa* o *cualitativa*.  
En el primer caso la variable toma valores númericos, como por ejemplo la altura de una persona, el precio de una propiedad, etc. Son problemas de regresión.    
En el segundo caso la variable dependiente puede tomar el valor de una clase o categoría. Por ejemplo, género de una persona, si paga o no paga su deuda, etc. Son problemas de clasificación.

### Midiendo el ajuste del modelo

#### Regresión

Para problemas de regresión una de las medidas más utilizadas es el Error Cuadrático Medio (MSE por sus siglas en inglés).
$$ MSE = \frac{1}{n} \sum_{i=1}^n(y_i - \hat f(x_i))^2 $$

Es básicamente la diferencia promedio entre la realidad y lo que predice nuestro modelo elevado al cuadrado. Esto último es para que los errores sean siempre positivos aunque subestimemos o sobreestimemos (y por su comodidad para cálculos matemáticos).

En primero lugar se calcula este valor con los datos de entrenamiento sin embargo lo que realmente importa es como performa el modelo en datos de testeo, es decir en datos que no fueron utilizados para estimar f(X). Podemos decir que cada modelo debería tener un MSE de entrenamiento y un MSE de testeo. Debido a la posibilidad de sobreajuste y a las diferencias en muestras nada garantiza que el modelo que estimemos con menor MSE en entrenamiento también sea el de menor MSE en testeo. 

A medida que aumentamos la flexibilidad de un modelo (sus grados de libertad) el MSE en entrenamiento va a disminuir, ya que tiene más herramientas para ajustarse a los datos pero puede que sobreajuste y por lo tanto no se traduzca en un menor MSE en testeo.

### El tradeoff entre Sesgo y Varianza 

No está demostrado en el libro pero es posible descomponer el MSE esperado de una observación de testeo en sesgo de $\hat f(x_0)$, varianza de $\hat f(x_0)$ y varianza del error irreducible $\epsilon$.

$$ E(y_0 - \hat f(x_0))^2 = Var(\hat f(x_0)) + [Sesgo(\hat f(x_0))]^2 + Var(\epsilon)$$

El lado izquierdo de la ecuación es el MSE esperado y coresponde MSE de testeo promedio que obtendríamos si estimaramos f utilizando una gran cantidad de sets de entrenamiento y testearamos cada uno en $x_0$.

Algunas observaciones:

* El MSE nunca puede ser menor que la varianza de $\epsilon$. Es un término fijo y por eso se lo llama error irreducible.
* La varianza es cuanto cambiar $\hat f$ si utilizamos otro set de entrenamiento. Siempre va a cambiar con otro set pero idealmente ese cambio no debería ser grande. Modelos muy flexibles tienden a cambiar más frente a distintos sets y son más inestables.
* Sesgo es el error provocado por la diferencia entre el modelo elegido y el verdadero proceso generador de los datos. En general modelos más flexibles tienen menor sesgo ya que pueden ajustar mayor variedad de formas funcionales.
* Al aumentar la flexibilidad de un modelo en general reducimos el sesgo pero aumentamos la varianza. En general en un primer momento el sesgo suele disminuir a mayor velocidad de lo que aumenta la varianza y por lo tanto el MSE esperado se reduce. Sin embargo llega un punto donde mayor flexibilidad reduce menos el sesgo que lo que aumenta la varianza y el MSE empieza a aumentar. Es el primer indicio de sobreajuste. Por eso se habla de tradeoff o "balance".
* En la realidad donde la verdadera f del DGP es inobservable no suele ser posible calcular explícitamente el MSE de testeo, el sesgo o la varianza de un método estadístico pero el proceso de fondo aplica y siempre debemos tener en mente el tradeoff.

#### Clasificación

Para problemas de clasificación uno de los enfoques más frecuentes para cuantificar la precisión de una función estimada $\hat f$ se suele usar el porcentaje de error en los datos de entrenamiento.

$$ \frac{1}{n} \sum_{i=1}^nI(y_i \neq \hat y_i) $$
Básicamente es el porcentaje de observaciones clasificadas erroneamente.
Al igual que con MSE es de gran importance el porcentaje de error en los datos de testeo.

#### Clasificador de Bayes

No lo demuestra en el libro pero la mejor manera de reducir el porcentaje de error en test es asignar a cada observación la clase con mayor probabilidad (según el DGP ). Es un concepto muy sencillo, dado X, asignar la clase cuya chance de acierto sea mayor.

$$ Pr(Y = j | X = x_0) $$
El porcentaje de error de Bayes (es decir el error luego de clasificar siguiendo esa regla) es análogo al Error Irreducible de regresión.
Hay que tener en cuenta que la distribución condicional de Y dado X no lo sabemos en los casos aplicados en la vida real, sería como saber la función f(X) o el DGP y por lo tanto no lo podemos calcular.

#### K vecinos más cercanos (KNN en inglés)

Idealmente uno querría aplicar el clasificador de Bayes pero es imposible ya que no sabemos la distribución real de los datos (es justamente lo que queremos estimar). KNN intenta aproximarse a la distribución condicional para clasificar las observaciones. Lo que hace este método es, dado un valor de K que elegimos nosotros, clasificar cada nueva observación según la clase mayoritaria entre las K observaciones más cercanas a esta.

$$ Pr(Y = j | X = x_0) = \frac{1}{K} \sum_{i \in N_0} I(y_i = j) $$
El valor que seleccionemos de K afecta en gran medida las predicciones del modelo. Un K menor hace más variable el modelo ya que selecciona menos observaciones y por lo tanto pocos cambios en el set de entrenamiento cambian la clasificación. Suele reducir el sesgo pero ser mas variable. Es análogo a hacer más flexible un modelo en regresión. Valores de K más grandes seleccionan puntos en un entorno más abarcativo y por lo tanto suele ser más constante pero con sesgo superior.  
Al igual que en regresión hay que tener cuidado con el sobreajuste. Reducir K garantiza menos errores en los datos de entrenamiento pero pasado un umbral la varianza aumenta en mayor medida y el porcentaje de error en test se incrementa.

**Conclusión**: Tanto en Clasificación como en Regresión la elección del nivel de flexibilidad  es central en el éxito de método de aprendizaje estadístico.
