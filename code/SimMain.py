#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:47:18 2019

@author: anecaise
"""


# Import
from pedestrian import pedestrian
from escalator_step import escalator_step
from LowerPlate import LowerPlate
from UpperPlate import UpperPlate
from escalator import escalator


def main():

    # Create Basic Obects
    esca = escalator(36, 1, 300, 10)
    entry = LowerPlate()
    LPexit = UpperPlate()

    # Creat Steps
    steps = []

    for i in range(0, esca.numSteps):
        steps.append(escalator_step(position=i))

    # Add people
    ppl = []

    for i in range(0, entry.waiters):
        ppl.append(pedestrian())

    # create temp person just to demonstrate working class
    tim = pedestrian()

    print("People Waiting : {}\nPeople Done : {}".format(entry.waiters, LPexit.totalComplete))
    print("Tim has been waiting {} secs".format(tim.time))
    print("Escalator is set to {} m/s".format(esca.spd))


if __name__ == "__main__":
    main()
