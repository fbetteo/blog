---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-01-06
description: Entropy and information theory
draft: false
slug: entropy
tags:
- Machine Learning
---
# Entropy and information

Term that comes from information theory.
The most intuitive way to think about _information_ of a variable is to relate to the **degree of surprise** on learning the value of the variable X.  
This definition was mentioned both in [Deep Learning, Bishop](https://www.bishopbook.com/) and in [Hamming](https://worrydream.com/refs/Hamming_1997_-_The_Art_of_Doing_Science_and_Engineering.pdf), and the former is the text I was just reading before starting this note.

So, having a variable X with `p(x)`, what's `h(x)` , the information of observing X? This quantity `h(x)` should be a monotonic function of `p(x)`. Remember, information is tied to the surprise, observing an almost sure event, high p(x), reveals less information than an unexpected event,low p(x). In the extreme, observing a known value, gives 0 information.

How to define the information mathematically comes (in some way intuitively) by the definition that, observing two independent variables `x` and `y` should provide an amount of information equal to the sum of the individual informations.

$$h(x,y) = h(x) + h(y)$$

We know that for independent events $p(x, y) = p(x)*p(y)$  

It can be derived then that  

$$h(x) = - \log_2 p(x)$$ 

The log provides the summation part coming from a multiplication. The negative ensure 0 or positive values. Remember that we are taking the log of a value between 0 and 1.

Now, there is another important term, **entropy**.
It summarizes the average amount of information that is transmitted *if a sender wishes to transmit the value of a random variable to a receiver*. 
The entropy is the expectation of the information, with respect to the distribution p(x).  

$$H[x] = - \sum_x p(x) \log_2 p(x)$$

For p(x) = 0, where the log would bring problem, we consider $p(x) \log p(x)$=0

Classical information theory uses $\log_2$ because it relates to bits and the amount of bits required to send a message but the book changes to $\ln$ because is much more used in ML and it's just a different unit to measure entropy. 
