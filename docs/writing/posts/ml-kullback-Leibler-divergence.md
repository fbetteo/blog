---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-01-28
description: Kullback-Leibler divergence
draft: false
slug: kullback-leibler-divergence
tags:
- Machine Learning
---
# Kullback-Leibler divergence

To understand KL divergence we need to first understand [Entropy](https://fbetteo.github.io/blog/writing/2025/01/06/entropy/). The most important thing to have in mind though is that entropy can be thought as a measure of "information", but what I like the most, as a measure of _expected surprise_ that one gets for every observed value of the distribution.

For a highly dense distribution, you will almost sure get a value from the dense region and the expected surprise will be really low (but you are highly surprised when you see a value off that region!)

### Relative entropy

How this relates to KL? Well, Kullback-Leibler is a divergence but is also called _relative entropy_. This means, how that measure of entropy differs between two distributions. I find that easier to grasp.

Usually we have a true distribution $p(x)$ and an estimated distribution $q(x)$ that we use to approximate $p(x)$. KL divergence can help us understand how good it does the  job.

If entropy is: 

$H[x] = - \sum_x p(x) \ln p(x)$  
(originally $\log_2$ but $\ln$ works too and it's used everywhere )

$$KL(p||q) = - \int{p(x) \ln q(x)dx} - (-\int{p(x) \ln p(x)dx})$$

$$ = - \int{p(x) \ln \frac{q(x)}{p(x)}dx}$$

The first row is clear, is just the difference in entropies. 
This is relative entropy between p(x) and q(x).

**Important**: KL divergence is not symmetrical. $KL(p||q) \neq KL(q||p)$
So, KL is not a metric of distance (but can be thought as if). It's actually a divergence.

### Why it's not symmetrical?
I think about it this way. This is a dissimilarity between one distribution and how we approximate it. Think about two totally different distributions (awful approximations):

* one highly centered around one specific value 
* the other with a uniform-ish shape, highly dispersed.

The difference in "surprise" you get from both ways approximation is not the same.

If you are approximating the highly dense distribution with the uniform one, you are approximating it with a distribution that surprises you  in general $\ln q(x)$, let's say _moderately high_ everywhere, even for the specific dense region.

But the other way, if you approximate the dispersed distribution with the dense one, you are using a distribution with high surprise in most of the region of the dispersed distribution and really low surprise in one specific value.

This term $\int{p(x) \ln q(x)dx}$ behaves differently in both scenarios and there is no guarantee or need that they should match.

#### References
 [Deep Learning, Bishop](https://www.bishopbook.com/)  
 [Wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)