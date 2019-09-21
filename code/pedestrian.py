#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:04:27 2019

@author: anecaise
"""


class pedestrian:

    """ pedestrian class represents a subway rider and will be used to track
        transit time and escalator capacity """

    def __init__(self):
        self.time = 0
        self.position = 0

    def addTime(self, timeStep):
        # time step defined based on escalator speed
        self.time = self.time + timeStep

    def updatePos(self, update):
        # track rider location
        self.position = update
