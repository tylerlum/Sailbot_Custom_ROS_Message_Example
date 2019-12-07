#!/usr/bin/env python

import Sailbot
from Sailbot import *

import utilities
from utilities import *

import time

if __name__ == '__main__':
    # Given globalPath from start. Assume doesn't change for now
    globalPath = [[1,0], [10,11],[24,10]]

    # Create sailbot ROS object that subscribes to relevant topics
    sailbot = Sailbot()

    # Set current global waypoint
    globalPathIndex = 0
    sailbot.globalWaypoint = globalPath[globalPathIndex]

    # Create first path and track time of updates
    currentState = sailbot.getCurrentState()
    currentLandAndBorderData = getCurrentLandAndBorderData(currentState)
    currentPath = createNewPath(currentState, currentLandAndBorderData)
    lastTimePathCreated = time.time()

    while True:
        print("LOOP. Time is {}".format(time.time()))

        currentState = sailbot.getCurrentState()

        # If next global waypoint reached, update land and border data
        # Update global waypoint in sailbot object
        if nextGlobalWaypointReached(currentState):
            # Update global waypoint and corresponding land+border data
            globalPathIndex = globalPathIndex + 1
            sailbot.globalWaypoint = globalPath[globalPathIndex]
            currentLandAndBorderData = getCurrentLandAndBorderData(currentState)

            # Update local path
            currentPath = createNewPath(currentState, currentLandAndBorderData)
            lastTimePathCreated = time.time()

            # publish 2nd point of new path (not the current position)


        elif isBad(currentPath) or nextLocalWaypointReached(currentState) or timeLimitExceeded(lastTimePathCreated):
            # Update local path
            currentPath = createNewPath(currentState, currentLandAndBorderData)
            lastTimePathCreated = time.now()

            # publish 2nd point of new path (not the current position)
