---
title: Distribucion Dirichlet como prior de Multinomial
authors:
  - fbetteo 
date: 2020-07-18
output: pdf_document
slug: disitrbucion-dirichlet-como-prior-de-mulitnomial
tags:
- estadistica
- binomial
- multinomial
- dirichlet
categories:
- estadistica
- R
thumbnailImage: https://lh3.googleusercontent.com/Jn2i1YphKhAbS_1w3KSotp7L0BZA3GguSSAEUCCyH9V4g2PtunCuoE0GlY-PkdrsLERb08KiSsNvIMPqpQ=w260-h173-rw
thumbnailImagePosition: left
summary: Utilizando priors para una distribución multinomial, partiendo de una Dirichlet. Cómo actualizar nuestras estimaciones a partir de los datos.
---

# Distribucion Dirichlet como prior de Multinomial

Basado en:  
http://www.mas.ncl.ac.uk/~nmf16/teaching/mas3301/week6.pdf  
http://www.inf.ed.ac.uk/teaching/courses/mlpr/assignments/multinomial.pdf

La distribución Dirichlet es una distribución multivariada para un conjunto de cantidades $\theta_i,...,\theta_m$ donde $\theta_i >= 0$ y $\sum_{i=1}^m \theta_i = 1$. Esto la hace una candidata útil para modelar un conjunto de probabilidades de una partición (un un conjunto de eventos mutuamente excluyentes). Es decir, un grupo de probabilides de eventos excluyentes, que sumen 1.  
Podemos remplazar los $\theta$ por $p$ si es más claro que hablamos de probabilidades luego.

La PDF es:

$$f(\theta_i,...,\theta_m; \alpha_i.., \alpha_m) =   \frac{\Gamma(\sum_i{\alpha_i})}{\prod_{i=1}^m \Gamma(\alpha_i)}\prod_{i = 1}^m \theta_i^{(\alpha_1-1)}$$

Donde la función $\Gamma$ es $\Gamma(\alpha) = (\alpha -1)!$. Para más detalles ver [acá](https://en.wikipedia.org/wiki/Gamma_function).  
Los $\alpha_i$ son parámetros de la distribución y deben ser mayores a 0.  
Cuando m = 2, obtenemos una función $beta(\alpha_1, \alpha_2)$ como caso particular de la Dirichlet.


### Dirichtlet en Inferencia Bayesiana.

De la misma manera que la distribución Beta suele usarse como prior de la Distribución Binomial ya que es una distribución conjugada para ese caso, la distribución Dirichlet suele usarse para distribuciones **Multinomiales**, es decir donde hay más de 2 categorías posibles (más de 2 $p_i$). También es distribución conjugada. Es simplemente la versión multinomial de la beta.  



La distribución multinomial es la siguiente:

$$\frac{n!}{\prod_{i = 1}^m x_i!}\prod_{i=1}^m p_i^{x_i}$$

Cuando m = 2, es la distribución binomial.

Si tuvieramos un experimento que se puede modelar como una multinomial y queremos estimar los $p_i$ podemos utilizar los estimadores de máxima verosimilitud (frecuentista) o ir por el camino de bayesiano donde comenzamos con un prior para cada p, que modelaremos con la Dirichlet. El prior de cada $p_i$ va a ser definido con la elección de los $\alpha$.

Yendo por el camino bayesiano vamos a tener nuestra distribución posterior:
$$ P(p | x) \propto P(x|p) * P(p)$$
donde $P(x|p)$ no es otra cosa que la distribución multinomial y $P(p)$ es nuestro prior de $p$ dado por la Dirichlet. Omitimos el denominador que es normalizador ya que es una constante.

Multiplicamos entonces la PDF multinomial por la Dirichlet y obtenemos:

*Importante notar que efectivamente cambiamos $\theta$ por $p$ en la Dirichlet para que sea consistente con la multinomial.*

$$\frac{n!}{\prod_{i = 1}^m x_i!}\prod_{i=1}^m p_i^{x_i} * \frac{\Gamma(\sum_i{\alpha_i})}{\prod_{i=1}^m \Gamma(\alpha_i)}\prod_{i = 1}^m p_i^{(\alpha_1-1)} \\ \propto \prod_i p_i^{\alpha_i + x_i -1}$$

Para la proporcionalidad, quitamos todo lo que es factorial (y $\Gamma$) ya que es constante y combinamos los exponentes de base $p_i$.

Vemos entonces que nuestra distribución posterior es propocional a ese término, que si vemos, es una Dirichlet para la cual nos falta el término constante! Por eso se dice que es una prior conjugada, ya que la posterior es de la misma familia que la prior (con otros valores claro.)  
Es entonces una Dirichlet con parámetros $\alpha_i + x_i$ y podemos completar el término faltante obteniendo: 
$$ \frac{\Gamma(\sum_i{\alpha_i + x_i})}{\prod_{i=1}^m \Gamma(\alpha_i + x_i)}\prod_{i=1}^m p_i^{(\alpha_i + x_i-1)}$$

He ahí nuestra distribución posterior para los valores de $p$ de la multinomial.

Para calcular rápidamente la esperanza de cada $p_i$ hacemos simplemente:
$$E(p_i) = \frac{\alpha_i + x_i}{\sum (\alpha_i +  x_i)}$$

Si obtenemos nueva información podemos repetir el proceso, pero nuestra nueva prior debería ser la posterior previamente calculada. Y así vamos agregando información a medida que se recolecta y actualizando nuestra inferencia acerca de $p_i$


**Aclaración**: La proporción de cada $\alpha_i$ iniciales en la Dirichlet prior sobre la suma de todos los $\alpha_i$ es nuestro prior de $p_i$. A mayores valores absolutos, mayor peso al prior respecto a los datos, ya que nuestro nuevo $p_i$ es función del $\alpha_i$ y $x_i$. Revisar bien como ajustar los $alpha$ según la magnitud de $x$, si es que hay que hacerlo.

### Ejemplo

Queremos modelar la compra de remeras de basquet en una tienda. Entra un cliente al azar y tiene determinadas probabilidades de comprar una remera de los Lakers, una de los Celtics, una de San Antonio o cualquier otro equipo.  

En un primer momento no sabemos las proporciones y empezamos con unos priors $\alpha_1 : \alpha_4 = [8,6,4,2]$ que corresponde a 40%, 30%, 20% y 10% respectivamente.

Recolectamos los datos de 100 clientes y vemos que las ventas fueron las siguientes:  
Lakers : 45  
Celtics: 22  
Spurs: 27  
Otros: 6  

Calculando rapidamente con la fórmula de la Esperanza las probabildades que se derivan de nuestra posterior obtenemos:

Lakers = 0.442  
Celtic = 0.233  
Spurs  = 0.258  
Otro   = 0.067  

Para ser más prolijos habría que agregar la varianza de cada $p$. A agregar en un futuro..

Si hubieramos calculado los p  de máxima verosimilitud no sería más que la proporción de cada equipo en los datos, sin tener en cuenta nuestro prior. Vemos que acá están obviamente cercanos a la proporción en los datos pero se inclinan hacia el prior. Recordar que el peso de los priors va a verse afectar por los $\alpha$ elegidos y por la cantidad de datos recolectados.


En ML es bastante útil para el caso donde una nueva categoría aparece en el test set. Si no fue vista en el training le va a dar probabilidad 0 mientras que con un prior podemos salvar ese problema.  
En NLP es bastante habitual usar la distribución Dirichlet como prior. Investigar por ese lado.
