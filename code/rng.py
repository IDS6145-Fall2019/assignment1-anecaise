#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:35:39 2019

@author: anecaise
"""


# import
import sobol_seq as sob
import numpy as np
from matplotlib import pyplot as plt
from sobol_seq import i4_sobol_generate as qng



def getsob(n):
    return qng(2, n)
    

N = 10
fig = plt.figure(figsize=[5,2])


x = np.random.rand(N)
y = np.random.rand(N)

axes = fig.add_subplot(2,5, 1)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2 , c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylabel("Pseudo")
axes.set_title('N = 10')

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
axes = fig.add_subplot(2,5, 2)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2, c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_title('N = 50')

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
axes = fig.add_subplot(2,5, 3)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2, c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_title('N = 100')

N = 200
x = np.random.rand(N)
y = np.random.rand(N)
axes = fig.add_subplot(2,5, 4)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2, c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_title('N = 200')

N = 500
x = np.random.rand(N)
y = np.random.rand(N)
axes = fig.add_subplot(2,5, 5)
# axes.set_ylabel('Y Values')
axes.scatter(x, y,s=2, c='black' )
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_title('N = 500')
   


"""Quasi"""
N = 10
x = getsob(N)[:,0]
y = getsob(N)[:,1]
axes = fig.add_subplot(2,5, 6)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2, c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])
axes.set_ylabel("Quasi")

N = 50
x = getsob(N)[:,0]
y = getsob(N)[:,1]
axes = fig.add_subplot(2,5, 7)
# axes.set_ylabel('Y Values')
axes.scatter(x, y,s=2, c='black' )
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])

N = 100
x = getsob(N)[:,0]
y = getsob(N)[:,1]
axes = fig.add_subplot(2,5, 8)
# axes.set_ylabel('Y Values')
axes.scatter(x, y,s=2, c='black' )
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])

N = 200
x = getsob(N)[:,0]
y = getsob(N)[:,1]
axes = fig.add_subplot(2,5, 9)
# axes.set_ylabel('Y Values')
axes.scatter(x, y, s=2, c='black')
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])

N = 500
x = getsob(N)[:,0]
y = getsob(N)[:,1]
axes = fig.add_subplot(2,5, 10)
# axes.set_ylabel('Y Values')
axes.scatter(x, y,s=2, c='black' )
axes.set_xlim(0,1)
axes.set_ylim(0,1)
axes.set_aspect(1*1)
axes.set_xticks([])
axes.set_yticks([])

plt.savefig("../images/random_numbers.png", dpi=300)
plt.show()



