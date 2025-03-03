---
title: "Maxima Verosimilitud y estimacion bayesiana"
authors:
  - fbetteo 
date: 2019-10-31
keywords: tech
slug: maxima-verosimilitud-y-estimacion-bayesiana
tags:
- estadistica
- R
categories:
- estadistica
- R
thumbnailImage: https://lh3.googleusercontent.com/Jn2i1YphKhAbS_1w3KSotp7L0BZA3GguSSAEUCCyH9V4g2PtunCuoE0GlY-PkdrsLERb08KiSsNvIMPqpQ=w260-h173-rw
thumbnailImagePosition: left
summary: Acerca de MLE y Estimadores bayesianos para estimar un parámetro desconocido.
---
# Maxima Verosimilitud y estimacion bayesiana


## Distribucion prior

A falta de una buena traducción usamos este término.

Supongamos que se toman muestras aleatorias de una distribucion con [pdf (funcion de densidad de probabilidad)](https://fbetteo.netlify.com/2019/04/funciones-de-probabilidad-y-distribucion/) $f(x|\theta)$. Por ejemplo podrían provenir de una normal con media = $\mu$ y varianza = 4.  
Nosotros no sabemos el valor de $\mu$ pero podemos tener una idea de qué valores puede tomar y tener en mente una distribución prior de este parámetro $\epsilon(\theta)$. Para el ejemplo sería $\epsilon(\mu)$. Podemos suponer que $\mu$ se distribuye como una uniforme (0,1) por decir algo.  
El concepto radica en tener una distribución prior para los parámetros de la distribución de la cual tomamos muestras aleatorias.

## Distribución Posterior


Volviendo a nuestra muestra $X_1...X_n$ proveniente de $f(x|\theta)$, podemos decir, debido a que son observaciones aleatorias e independientes que su distribución conjunta es $f_n(x_1...X_n|\theta) = f(x_1|\theta)...f(x_n|\theta)$, que lo podemos escribir como $f_n(x|\theta)$.  
Dado que suponemos que $\theta$ proviene de una distribución $\epsilon(\theta)$, la pdf conjunta $f_n(x|\theta)$ tiene que ser vista como la pdf conjunta condicional de$X_1...X_n$ para un valor particular de $\theta$.  
Multiplicando la pdf conjunta condicional por la pdf $\epsilon(\theta)$ obtenemos la (n+1) distribución conjunta de $X_1...X_n$ y $\theta$ bajo la forma $f_n(x|\theta)\epsilon(\theta)$. Sería la pdf de encontrar en simultáneo determinados valores para x y $\theta$. La probabilidad conjunta marginal de $X_1...X_n$ se encuentra integrando la pdf conjunta con $\theta$ para todos los valores de $\theta$. Sería la probabilidad marginal de encontrar determinados valores de x (sabiendo la distribución de $\theta$ pero sin saber el valor puntual que toma).

$g_n(x) = \int_\Omega f_n(x|\theta)\epsilon(\theta) d\theta$

Por teorema de Bayes tenemos que la distribución posterior de $\theta$, es decir, dados los x es:
$$\epsilon(\theta|x) = \frac{f_n(x|\theta)\epsilon(\theta)}{g_n(x)} \text{ para } \theta \in \Omega$$ 
 Se dice que la distribución prior $\epsilon(\theta)$ representa la verosimilitud, antes de ver los valores de $X_1...X_n$, de que el verdadero valor de $\theta$ se encuentre en cada una de las regiones de $\Omega$ y que la pdf de la distribución posterior $\epsilon(\theta|x)$ representa la verosimilitud después que los valores $X_1 = x_1,...,X_n = x_n$ hayan sido observados.
 
 
 ## La funcion de Versoimilitud
 
 El denominador de la distribución posterior es básicamente la integral del numerador para todos los posibles valores de $\theta$. Depende de los valores observados $X_1...X_n$ pero no de $\theta$, por lo que puede considerarse constante en este contexto.  
 Dado que es una constante podemos quitarla de la distribución posterior que vimos y decir que 
 $$\epsilon(\theta|x) \propto f_n(x|\theta)\epsilon(\theta)$$
 
 Cuando se ve $f_n(x|\theta)$ para una muestra aleatoria como función de $\theta$, se la suele llamar función de verosimilitud. En inglés: Likelihood function.
 
Juntando estos términos podemos decir que la pdf posterior de $\theta$ es proporcional al producto de la función de verosimilitud y la pdf prior de $\theta$.  

La idea de ver esta relación de proporcionalidad es para poder calcular la pdf posterior evitando calcular la integral del denomiador $g_n(x)$. Si el numerador tiene la forma de alguna de las distribuciones conocidad (normal, beta, gamma, uniforme, etc) es posible calcular fácilmente el factor constante por el cual multiplicar esa pdf para llegar a la posterior.

## Distribuciones prior Conjugadas

Este concepto refiere a que ciertas distribuciones son particularmente útiles para los cálculos cuando las variables aleatorias observadas provienen de alguna distribución específica.  
Es decir que según la distribución de la que provienen las X puede que haya alguna distribución conjugada tal que al asumirla para la pdf prior $\epsilon(\theta)$ ya sabemos que la distribución posterior también será de esa familia.

Un ejemplo ilustrador:  
  Supongamos que tomamos observaciones $X_1...X_n$ de una distribución Bernoulli de la cual no sabemos el parámetro $\theta$ (que debe estar entre 0 y 1). Supongamos además que la pdf prior de $\theta$ es una distribución beta con algúnos parámetros dados $\alpha \text{ y } \beta$. En este caso sabemos que por ser un caso de distribución conjugada, la pdf posterior de $\theta$ dado $X = x_i (i = 1,...,n)$ es a su vez una distribución beta con parámetros $\alpha + \sum_{i=1}^n x_i \text{ y } \beta + n - \sum_{i=1}^n x_i$.
  
  
Según la distribución de la que provengan las observaciones hay distintas distribuciones conjugadas que son las más convenientes para ese caso.

# Estimación de parámetros

La idea es estimar algún parámetro de la distribución de la cual se obtienen los datos observados. El valor estimado del parámetro va a depender de dos cosas:  

* Del *estimador* que hayamos elegido (es decir, la función de los datos elegida)
* De la muestra. El valor estimado va a depender de los datos aleatorios que tengamos de la distribución.

Como el estimador depende de la muestra podemos verlo a su vez como una variable aleatoria.

## Función de pérdida

Lo que queremos de un estimador es que devuelva un valor estimado "a" para el parámetro lo más cercano posible al verdadero valor de $\theta$. La función de pérdida es una función que cuantifica esto.
$$ L(\theta,a)$$
Hay algunas funciones habituales pero pueden adecuarse según el problema.  
Podemos decir que en general lo que se busca es encontrar una estimación para la cual la esperanza de la pérdida sea un mínimo.

## Estimador bayesiano

Si tenemos una muestra aleatoria y una pdf posterior para $\theta$ entonces el valor esperado de la pérdida para cualquier valor estimado "a" es:
$$E[L(\theta,a)|x] = \int_\Omega L(\theta,a)\epsilon(\theta,x)d\theta$$

Lo que buscamos es encontrar un valor de a cuya pérdida esperada sea mínima. La función que genera un valor de a mínimo para cada posible valor de X será un estimador de $\theta$ y en particular se llamará *Estimador Bayesiano*.  
El estimador bayesiano, que minimiza la pérdida esperada para cualquier set de datos X, va a depender de la función de pérdida que elijamos y de la pdf prior que se elija para $\theta$.

Por ejemplo,para la función de pérdida más utilizada, que es la de error cuadrático
$$L(\theta,a) = (\theta -a)^2$$
está demostrado que la pérdida es mínima cuando $a$ es la media de la distribución posterior $E(\theta|x)$.


Dijimos que el valor del estimador bayesiano va a depender de la distribución prior elegida. Esto es cierto, pero hay que tener en cuenta que para muestras grandes las diferencias empiezan a achicarse y los estimadores bayesianos provenientes de distintos priors empiezan a converger en la mayoría de los casos.

## Estimadores de Máxima Verosimilitud

Los estimadores de máxima verosimilitud (MLE) son muy comunmente usados para estimar parámetros desconocidos ya que más allá de la discusión casi filosófica de "bayesianos vs frecuentistas", sirven para estimar sin tener que definir una función de pérdida ni una distribución prior para los parámetros. Esto último es importante ya que para casos donde se necesita estimar un vector de parámetros, la distribución prior debe ser una multivariada que englobe a todos y eleva la complejidad del proceso bayesiano ampliamente.  
Para muestras chicas MLE suele hacer un trabajo decente y para muestras grandes suele ser excelente por lo que se llega a resultados muy similares a través de un proceso más directo y más sencillo.  

Para estimar mediante MLE lo único que necesitamos es la función de verosimilitud ya definida.
$$f_n(x_1...X_n|\theta)$$
Luego lo único que se hace es buscar el parámetro $\hat \theta$ (estimado) que maximice esa función. Básicamente es buscar qué parámetro hace que la probabilidad conjunta de obtener esos valores de X sea máxima? Ese es nuestro MLE.


Para la gran mayoría de los casos esta metodología funciona pero hay que tener en cuenta que es posible que para algunos problemas no haya un máximo para la función de verosimilitud o que haya más de un punto, en cuyo caso hay que elegir alguno de ellos.


### MLE en Bernoulli

  Supongamos que tomamos observaciones $X_1...X_n$ de una distribución Bernoulli de la cual no sabemos el parámetro $\theta$ (que debe estar entre 0 y 1).
  
Para cualquier vector de observaciones $X_1...X_n$ la función de verosimilitud es:
$$ f_n(x|\theta) = \prod_{i = 1}^n \theta^{x_i}(1-\theta)^{1-x_i}$$
El valor de $\theta$ que maximice la función de verosimilitud es el mismo valor que maximiza $log f_n(x|\theta)$, por lo que es conveniente encontrar tal valor buscando que maximice:
$$L(\theta) = log f_n(x|\theta) = \sum_{i=1}^n[x_i log \theta + (1 - x_i) log(1-\theta)] = (\sum_{i=1}^nx_i)log \theta + (n-\sum_{i=1}^n x_i) log (1-\theta)$$

Si derivamos $dL(\theta) / d\theta$ e igualamos a 0, resolviendo esa ecuando para $\theta$ encontramos que $\theta = \bar x_n$.  
Este valor maximiza el logaritmo de la función de verosimilitud y por ende también de la función de verosimilitud en sí misma. Por lo tanto el MLE de $\theta$ es $\hat \theta = \bar X_n$



```r
# Generamos 100 observaciones de una Bernoulli
set.seed(150)
data = rbinom(100, 1, prob = 0.723)

# Calculamos su promedio, que ya sabemos es la mejor estimación para p dados los datos
mean(data)
```

```
## [1] 0.68
```

```r
# Definimos función de verosimilitud
# Es la pdf de una Bernoulli para cada observación y sumamos sus logaritmos (en negativo porque 
# el optimizador minimiza en vez de maximizar)
LL = function( p){
   R = dbinom(x = data, size = 1, prob = p)
   
   -sum(log(R))  # Negativo porque log de probabilidades es <0.
 }

# Función que busca los parámetros que minimzan el negativo de la log verosimilitud
# Elegimos un valor inicial de p en el medio.
stats4::mle(LL, start = list(p = 0.5) )
```

```
## 
## Call:
## stats4::mle(minuslogl = LL, start = list(p = 0.5))
## 
## Coefficients:
##         p 
## 0.6799996
```
Vemos que la estimación por MLE es *idéntica* a la media. No corresponde con el verdadero valor del parámetro poblacional p debido a la muestra particular que fue seleccionada.


Algunos comentarios finales:

* En algunos casos no es posible encontrar la solución óptima si no es por métodos numéricos.
* Cuando $n \to \infty$ MLE converge en probabilidad al verdadero $\theta$. Por ende cuando $n \to \infty$ el estimador bayesiano (que cumple la misma propiedad) y MLE serán muy parecidos entre sí y al verdadero $\theta$.
* MLE solo depende de las observaciones y no de cómo y en qué orden fueron recolectadas.
