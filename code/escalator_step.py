#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:19:26 2019

@author: anecaise
"""


class escalator_step:
    """ represents single step in system. Will allow us to set height of
        escalator, and load 1-2 people per step randomly """

    def __init__(self, position=0):
        self.pos = position
        self.riders = 0

    def getRiders(self):
        if self.pos == 1:
            self.riders = 2

    def resetStep(self):
        self.riders = 0

    def updatePos(self, change):
        self.pos = change
