#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:00:11 2019

@author: anecaise
"""


import numpy as np
from matplotlib import pyplot as plt
import chaospy

    # f1igsize=[5,3]

fig = plt.figure(figsize=[5,3], num=100)

"""Poisson"""


x = np.random.poisson(1,10)
axes = fig.add_subplot(3,5, 1)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_ylabel("Poisson")
axes.set_title('N=10')
axes.set_xticks([])
axes.set_yticks([])



x = np.random.poisson(1,50)
axes = fig.add_subplot(3,5, 2)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=50')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.poisson(1,500)
axes = fig.add_subplot(3,5, 3)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=500')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.poisson(1,1000)
axes = fig.add_subplot(3,5, 4)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=1000')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.poisson(lam=1, size=(10000,1))
axes = fig.add_subplot(3,5, 5)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=8000')
axes.set_xticks([])
axes.set_yticks([])



""" Binomial"""
x = np.random.binomial(6, .50, 10)
axes = fig.add_subplot(3,5, 6)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_ylabel("Binomial")
axes.set_xticks([])
axes.set_yticks([])

x = np.random.binomial(6, .50, 50)
axes = fig.add_subplot(3,5, 7)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.binomial(6, .50, 500)
axes = fig.add_subplot(3,5, 8)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.binomial(6, .50, 1000)
axes = fig.add_subplot(3,5, 9)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = np.random.binomial(6, .50, 8000)
axes = fig.add_subplot(3,5, 10)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])



"""Uniform"""
x = np.random.uniform(size=10)
axes = fig.add_subplot(3,5,11)
axes.hist(x, bins=7,edgecolor='black')
axes.set_ylabel("Uniform")
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 10/3)


x = np.random.uniform(size=50)
axes = fig.add_subplot(3,5,12)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 50/3)

x = np.random.uniform(size=500)
axes = fig.add_subplot(3,5,13)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 500/3)

x = np.random.uniform(size=1000)
axes = fig.add_subplot(3,5,14)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 1000/3)

x = np.random.uniform(size=8000)
axes = fig.add_subplot(3,5,15)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 8000/3)

plt.savefig('../images/pseudo_dist.png', dpi=100)
plt.show()


