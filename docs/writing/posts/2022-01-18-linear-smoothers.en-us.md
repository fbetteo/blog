---
title: Linear Smoothers
authors:
  - fbetteo 
date: 2022-01-18
slug: linear-smoothers.en-us
categories:
  - estadistica
  - machine learning
  - algebra
  - statistics
tags:
  - algebra
  - estadistica
  - Machine Learning
  - statistics
thumbnailImage: https://lh3.googleusercontent.com/Jn2i1YphKhAbS_1w3KSotp7L0BZA3GguSSAEUCCyH9V4g2PtunCuoE0GlY-PkdrsLERb08KiSsNvIMPqpQ=w260-h173-rw
thumbnailImagePosition: left
summary: Some details about OLS as smoothing of the training data. Weighted average of Y by distance of X to the center and variance of X.
---
#Linear Smoothers

### Linear regression as smoothing

Let's assume the DGP (data generating process) is:
$$ Y = \mu(x) + \epsilon$$ where $\mu(x)$ is the mean Y value for that particular x and $\epsilon$ is an error with mean 0.

When running OLS we are trying to approximate $\mu(x)$ with a linear function of the form $\alpha + \beta x$ and trying to retrieve the best $\alpha$ and $\beta$ minimizing the mean-squared error.  

The conclusions don't change but the math gets easier if we assume both X and Y are centered (mean=0).  
With that in mind we can write down the MSE and optimize to get the best parameters.

$$MSE(\alpha, \beta) = \mathbb{E}[(Y - \alpha - \beta X)^2] \\
= \mathbb{E}[\mathbb{E}[(Y - \alpha - \beta X)^2 | X]] \\
= \mathbb{E}[\mathbb{V}[Y|X]] + \mathbb{E}[Y- \alpha - \beta X | X])^2] \\
= \mathbb{E}[\mathbb{V}[Y|X]] + \mathbb{E}[(\mathbb{E}[Y- \alpha - \beta X | X])^2]$$


Deriving with respect to $\alpha$ and $\beta$ for optimization..  
The first term can be dropped since doesn't include any parameter.

$$\frac{\partial MSE}{\partial \alpha} =   \mathbb{E}[2(Y - \alpha - \beta X)(-1)] \\
 \mathbb{E}[Y - a - b X] =  0 \\
 a =  \mathbb{E}[Y] - b  \mathbb{E}[X] = 0
 $$
 when Y and X are centered..
 
 and
 $$\frac{\partial MSE}{\partial \beta} =   \mathbb{E}[2(Y - \alpha - \beta X)(-X)] \\
 \mathbb{E}[XY] - b\mathbb{E}[X^2] = 0 \\
b = \frac{Cov[X,Y]}{\mathbb{V}[X]}
$$

The optimal beta is a function of the covariance between Y and X, and the variance of X.

Putting together $a$ and $b$ we get $\mu(x) = x  \frac{Cov[X,Y]}{\mathbb{V}[X]}$

Replacing with the values from the sampled data we get an estimation of $a$ and $b$.  

Remember they are 0 centered so variance and covariance get simplified.

$$ \hat a = 0 \\
\hat b = \frac{\sum_i y_i x_i}{\sum_i x_i^2}$$


With all this we can see how **OLS is a smoothing of the data**.  
Writing in terms of the data points:  
$$\hat \mu(x) = \hat b x \\
= x  \frac{\sum_i y_i x_i}{\sum_i x_i^2} \\
= \sum_i y_i \frac{x_i}{\sum_j x_j^2} x \\
= \sum_i y_i \frac{x_i}{n \hat \sigma_x^2} x
$$
where $\hat \sigma_x^2$ is the sample variance of X.  
*In words, our prediction is a weighted average of the observed values $y_i$ of the dependent variable, where the weights are proportional to how far $x_i$ is from the center (relative to the variance), and proportional to the magnitude of $x$. If $x_i$ is on the same side of the center as $x$, it gets a positive weight, and if it's on the opposite side it gets a negative weight.* (Shalizi 2017)

If $\mu(x)$ is really a straight line, this is fine, but when it's not, that the weights are proportional to how far they are to the **center** and not the point **to predict** can lead to awful predictions.



### Alternative smoothers
For that, other methods smooth the data in another ways to help mitigate that.

As quick examples, we have *KNN regression* where the smoothing is done using only close observations to the one to predict (and getting quite noisy since depend a lot on the sample points around a small area).  

*Kernel smoothers* are a variant where depending on the kernel selected we get different smoothing. The main idea is that we use a windowd of data with the idea of putting more weight to points close to the one to predict. Could be Gaussian weight around X for example, or uniform around a window. Note this is different than KNN regression since we do not take the average of those points, we get a regression for that area.  
A nice thing about this smoothers (and KNN regression) is that if we want to predict points far from the training data we won't get a linear extrapolation as with OLS but it will be pushed towards the closest data points we had in training.
