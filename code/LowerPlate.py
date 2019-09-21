#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:35:03 2019

@author: anecaise
"""


class LowerPlate:
    def __init__(self):
        self.waiters = 0

    def newRiders(self, change):
        self.waiters = self.waiters + change
