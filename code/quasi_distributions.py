#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:59:58 2019

@author: anecaise
"""


import numpy as np
from matplotlib import pyplot as plt
import chaospy


# Create Fig

fig = plt.figure(figsize=[5,3], num=100)


"""exponential"""
dist = chaospy.Exponential()
x = dist.sample(10, 'S')
axes = fig.add_subplot(3,5, 1)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_ylabel("Exponential")
axes.set_title('N=10')
axes.set_xticks([])
axes.set_yticks([])



x = dist.sample(50, 'S')
axes = fig.add_subplot(3,5, 2)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=50')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(500, 'S')
axes = fig.add_subplot(3,5, 3)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=500')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(1000, 'S')
axes = fig.add_subplot(3,5, 4)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=1000')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(8000, 'S')
axes = fig.add_subplot(3,5, 5)
# axes.set_ylabel('Y Values')
axes.hist(x,bins=7,edgecolor='black')
axes.set_title('N=8000')
axes.set_xticks([])
axes.set_yticks([])



""" Binomial"""
dist = chaospy.Binomial(6, .5)
x = dist.sample(10, 's')
axes = fig.add_subplot(3,5, 6)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_ylabel("Binomial")
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(50, 's')
axes = fig.add_subplot(3,5, 7)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(500, 's')
axes = fig.add_subplot(3,5, 8)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(1000, 's')
axes = fig.add_subplot(3,5, 9)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])

x = dist.sample(8000, 's')
axes = fig.add_subplot(3,5, 10)
# axes.set_ylabel('Y Values')
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])



"""Uniform"""
dist = chaospy.Uniform(1, 4)

x = dist.sample(10, rule = 'S')
axes = fig.add_subplot(3,5,11)
axes.hist(x, bins=7,edgecolor='black')
axes.set_ylabel("Uniform")
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 10/3)


x = dist.sample(50, rule = 'S')
axes = fig.add_subplot(3,5,12)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 50/3)

x = dist.sample(500, rule = 'S')
axes = fig.add_subplot(3,5,13)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 500/3)

x = dist.sample(1000, rule = 'S')
axes = fig.add_subplot(3,5,14)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 1000/3)

x = dist.sample(8000, rule = 'S')
axes = fig.add_subplot(3,5,15)
axes.hist(x, bins=7,edgecolor='black')
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylim(0, 8000/3)


plt.savefig('../images/quasi_dist.png', dpi=300)
plt.show()