---
title: Bias Variance Tradeoff
authors:
  - fbetteo 
date: 2022-01-17
slug: bias-variance-tradeoff.en-us
categories:
  - estadistica
  - matematica
tags:
  - estadistica
  - Machine Learning
thumbnailImage: https://lh3.googleusercontent.com/Jn2i1YphKhAbS_1w3KSotp7L0BZA3GguSSAEUCCyH9V4g2PtunCuoE0GlY-PkdrsLERb08KiSsNvIMPqpQ=w260-h173-rw
thumbnailImagePosition: left
summary: Some details about Bias Variance Tradeoff
---

# Bias Variance Tradeoff

Mean squared error (MSE) is a measure of how far our prediction is from the true values of the dependent variable. It's the expectation of the squared error.

The squared error being:

$$(Y - \hat \mu(x))^2$$ 

where Y is the true value and $\hat \mu(x)$ is the prediction for a given x.

We can decompose it into:

$$(Y - \hat \mu(x))^2 \\
= (Y - \mu(x) + \mu(x) - \hat \mu(x)^2) \\
= (Y - \mu(x))^2 + 2(Y - \mu(x))(\mu(x) - \hat \mu(x)) + (\mu(x) - \hat \mu(x))^2$$

So, that's the squared error. The MSE is the expectation of that.  


The expectation is a linear operator so we can apply it independently to different terms of a summation.  
The expectation of the first term is the variance of the error intrinsic to the DGP.  
The second term goes to 0 because involves $E(Y-\mu(x))$ that is the expectation of the error and that's equal to 0.  
The third term reamins as it is since doesn't involve random variables.  

$$MSE(\hat \mu(x)) = \sigma^2_x + (\mu(x) - \hat \mu(x))^2$$

This is our first bias-variance decomposition. The first term is the intrinsic difficulty of the problem to model, is the variance of the error and can not be reduced, it is what it is.  
The second term is how off our predictions are regarding the true expected value for that particular X.  

This would be fine if we wouldn't need to consider $\hat \mu(x)$ a random variable itself, since it is dependent on the specific dataset we are using. Given another dataset our estimation would be different despite using the same model methodology.  
What we actually want is the MSE of the method used $\hat M$ and not only the result of a particular realization.

$$MSE(\hat M_n(x)) = E[(Y - \hat M_n(X))^2 | X=x] \\
= ... \\
= \sigma^2_x + (\mu(x) -  E[\hat M_n(x)])^2 - V[\hat M_n(x)]
$$

This is our 2nd bias-variance decomposition.  
The first term is still the irreducible error.  
The second term is the bias of using $\hat M_n$ to approximate $\mu(x)$. Is the approximation bias/error.  
The third term is the variance of the estimate of the regression function. If our estimates have high variance we can have large errors despite using an unbiased approximation.  

Flexible methods will be able to approximate $\mu(x)$ closely, however usually using more flexible methods involve increasing the variance of the estimate. That's the **bias-variance tradeoff**. We need to evaluate how to balance that, sometimes including some bias reduce much more the error by decreasing the variance.  
Usually larger N decreases the MSE since it decreases bias and variance error.


#### Reference
Based on 1.4.1 from Advanced data analysis from a elementary point of view.

































