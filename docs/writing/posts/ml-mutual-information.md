---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-01-28
description: Mutual information
draft: false
slug: mutual-information
tags:
- Machine Learning
---

# Mutual Information


> When two variables $x$ and $y$ are independent, their joint distribution will factorize into the product of their marginals $p(x,y) = p(x)p(y)$. If the variables are not independent, we can gain some idea of whether they are "close" to being independent by considering the [KL Divergence](https://fbetteo.github.io/blog/writing/2025/01/28/kullback-leibler-divergence/) between the joint distribution and the product of the marginals, given by:

$$I[x,y] = KL(p(x,y)||p(x)p(y))$$

$$=  - \int \int p(x,y) \ln (\frac{p(x)p(y)}{p(x,y)}) $$

which is called the _mutual information_ between $x$ and $y$.

Thus, the mutual information represents the reduction in uncertainty about $x$ by virtue of being told the value of $y$ (or vice versa)

> From a Bayesian perspective, we can view $p(x)$ as the prior distribution for $x$ and $p(x|y)$ as the posterior distribution after we have observed new data $y$. The mutual information therefore represents the reduction in uncertainty about $x$ as a consequence of the new observation $y$.