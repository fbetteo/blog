---
title: Softmax vs sigmoid
authors:
  - fbetteo 
date: 2021-01-18
slug: softmax-vs-sigmoid.en-us
categories:
  - estadistica
  - Python
  - machine learning
tags:
  - estadistica
  - Python
  - AI
  - Machine Learning
thumbnailImage: https://lh3.googleusercontent.com/nfHMd9voBvXDKziowr-dYKDIPTQwb0og9vQ3GUdbEyIt95UTfag3ajjsGJcoB-HCC2tt683hiZ8Xo2vVEw=w328-h153-rw
thumbnailImagePosition: left
summary: Softmax vs Sigmoid. How weights are updated in the last layer.
---

# Softmax vs sigmoid

When using Neural Nets for a multiclass classification problem it's standard to have a softmax layer at the end to normalize the probabilities for each class. This means that the output of our net is a vector of probabilities (one for each class) that sums to 1. If there isn't a softmax layer at the end, then the net will output a value in each of the last cells (one for each class) but without a delimited range.  
Just a set of numbers where usually the highest is the one with the most probable class but it's not obvious how to value the differences between them.

So, you have a ordered set of numbers, you know which one is the most probable but you want to transform that into clear probabilities. You use the softmax layer. 

You could use a sigmoid activation function in the last cell to have *individual* probabilities. For each class, it transforms the output of the net into a probability. However the sum of those probabilities is not guaranteed to sum 1, actually it won't in practice. It's a simple proxy but you can get better intuitions with softmax.

We will compare how these two approaches affect the last group of weights by inspecting the gradient after calculating the loss for an observation.

>>> I'm using the *reticulate* package in R to include Python code in Rmarkdown. Pretty nice.




```r
library(reticulate)
```

We import pytorch to handle tensors and neural net functions.

```python
import numpy as np
import torch
import torch.nn.functional as F
```


```python
torch.manual_seed(99)
```

```
## <torch._C.Generator object at 0x00000262714CF730>
```

* 1 obs  
* 5 features (X)  
* 3 possible classes (index 1 = class 2)  
* W. 3 output cells, each one with 5 weights (one per feature)  
* W1 = W2 because we run it twice (two scenarios) and we can't re use the same weights because of the gradient calculated


```python
X = torch.randn(5)
W1 = torch.randn(3,5)
W2 = W1.detach().clone() 
y = torch.tensor([1]) 
```

We transform everything to positives to make it cleaner and we add the requires_grad_() characteristic
that tells pytorch that those tensors need the gradient backpropagated during training

```python
X = X.abs()
W1 = W1.abs().requires_grad_()
W2 = W2.abs().requires_grad_()
```


We define both losses (softmax and sigmoid).  

*Softmax*  

* Weights * input: cell value
* we change dimension of output to use it as input of softmax
* We calculate the softmax (probabilities of each class that sum 1)
* Apply log because we will use the negative log likelihood
* We calculate the loss (log of softmax probabilities vs actual class)

*Sigmoid*  

* Weights * input: cell value
* we change dimension of output to use it as input of sigmoid
* We calculate the sigmoid (probabilities of each class individually)
* Apply log because we will use the negative log likelihood
* We calculate the loss (log of sigmoid probabilities vs actual class)


```python
# funcion con softmax al final
def softmax_loss(W):
    z = W @ X
    z = z.unsqueeze(0)
    z = torch.softmax(z, dim=1)
    z = torch.log(z)
    return F.nll_loss(z, y)

# funcion con una sigmoidea por activacion
def sigmoid_loss(W):
    z = W @ X
    z = z.unsqueeze(0)
    z = torch.sigmoid(z)
    z = torch.log(z)
    return F.nll_loss(z, y)
```


We run the forward pass and calculate the loss for the sigmoid first. Then we look for the gradient.  
As we can see in the results, only the weights that go to the correct class' output cell are modified. Classes one and three rest untouched. This is because the sigmoid activation just has the individual weights (and cross entropy only look to the correct class)

```python
out_sigmoid = sigmoid_loss(W1)
out_sigmoid.backward()
W1.grad
```

```
## tensor([[ 0.0000,  0.0000,  0.0000,  0.0000,  0.0000],
##         [-0.0452, -0.0867, -0.0564, -0.0492, -0.0549],
##         [ 0.0000,  0.0000,  0.0000,  0.0000,  0.0000]])
```
On the contrary, when running the same net but with softmax layer we see that all the weights are updated. The correct class has gradient with the same sign that for the sigmoid example but the other two classes have in this case opposite sign gradients (which makes sense since you want them to go in the other direction).  
This happens because the softmax includes the other classes in each cell since they are needed to normalize and return probabilities that sum up to 1.


```python
out_softmax = softmax_loss(W2)
out_softmax.backward()
W2.grad
```

```
## tensor([[ 0.5393,  1.0346,  0.6731,  0.5868,  0.6552],
##         [-0.5576, -1.0697, -0.6959, -0.6066, -0.6775],
##         [ 0.0183,  0.0351,  0.0228,  0.0199,  0.0222]])
```
This is a simple case with just one layer of weights so we can clearly see this. If you had a fully connected net with more layers, this is valid just for the last one because the gradient is backpropagated and the weights from "other paths" still affect the cell that corresponds to the second class.  

### Conclusion

The net should evolve during training in a similar way with both last layer activations but the way they do it is different and we try to show in here why. In the end, the sigmoid still reflects the preference for one of the classes and during each epoch it will go through the desired path but just updating some of the weights and not all at the same time.
