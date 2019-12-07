#!/usr/bin/env python
import time
from random import random

def getCurrentLandAndBorderData(currentState):
    return None

def createNewPath(currentState, currentLandAndBorderData):
    return [ [random(), random()], [random(), random()], [random(), random()] ]

def nextGlobalWaypointReached(currentState):
    return None

def isBad(currentPath):
    return None

def nextLocalWaypointReached(currentState):
    return None

def timeLimitExceeded(lastTimePathCreated):
    secondsLimit = 5
    return time.time() - lastTimePathCreated > secondsLimit
