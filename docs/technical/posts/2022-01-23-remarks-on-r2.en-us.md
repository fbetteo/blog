---
title: Remarks on R2
authors:
  - fbetteo 
date: 2022-01-23
slug: remarks-on-r2.en-us
categories:
  - estadistica
  - statistics
  - machine learning
tags:
  - estadistica
  - statistics
  - Machine Learning
thumbnailImage: https://lh3.googleusercontent.com/Jn2i1YphKhAbS_1w3KSotp7L0BZA3GguSSAEUCCyH9V4g2PtunCuoE0GlY-PkdrsLERb08KiSsNvIMPqpQ=w260-h173-rw
thumbnailImagePosition: left
summary: A few comments to have in mind about R2
---

# Remarks on R2

### R2 depends on the variance on the variance of the predictors


Quoting from Shalizi[^1]
Assuming a true linear model  
$$ Y = aX + \epsilon$$  
and assuming we know $a$ exactly.  
The variance of Y will be $a^2\mathbb{V}[X] + \mathbb{V}[\epsilon]$.  
So $R^2 = \frac{a^2\mathbb{V}[X]}{a^2\mathbb{V}[X] + \mathbb{V}[\epsilon]}$  
This goes to 0 as $\mathbb{V}[X] \rightarrow  0$ and it goes to 1 as  $\mathbb{V}[X] \rightarrow  \infty$. "It thus has little to do with the quality of the fit, and a lot to do with how spread out the predictor variable is. Notice also how easy it is to get a high $R^2$ even when the true model is not linear!"

Below a quick comparison between two linear relationships, one with much higher variance than the other in the predictor.  
Added a different constant for better display in plot.


```r
library(tidyverse)

x1 = rnorm(1000, mean=0, sd=1)
x2 = rnorm(1000, mean=0, sd=10)
error = rnorm(1000, mean=0, sd=0.5)

y1 = x1 + error
y2 = 10 + x2 +  error

df = data.frame(x1,x2,y1,y2)

model1 = lm("y1 ~ x1")
```

```
## Error in eval(predvars, data, env): object 'y1' not found
```

```r
model2 =  lm("y2 ~ x2")
```

```
## Error in eval(predvars, data, env): object 'y2' not found
```



