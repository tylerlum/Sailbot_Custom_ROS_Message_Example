#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose2D

import Sailbot
from Sailbot import *

import utilities
from utilities import *

import time

if __name__ == '__main__':
    # Given globalPath from start, assume doesn't change for now
    globalPath = [GPSCoordinates(1,0), GPSCoordinates(10,11), GPSCoordinates(24,10)]

    # Create sailbot ROS object that subscribes to relevant topics
    sailbot = Sailbot()

    # Set current global waypoint
    globalPathIndex = 0
    sailbot.globalWaypoint = globalPath[globalPathIndex]

    # Create ros publisher for the next local waypoint for the controller
    nextLocalWaypointPublisher = rospy.Publisher('nextLocalWaypoint', Pose2D)
    # rospy.init_node('local_pathfinding', anonymous=True)
    publishRate = rospy.Rate(10) # Hz
    nextLocalWaypointMsg = Pose2D()

    # Create first path and track time of updates
    currentState = sailbot.getCurrentState()
    currentLandAndBorderData = getCurrentLandAndBorderData(currentState)
    currentPath = createNewPath(currentState, currentLandAndBorderData)
    lastTimePathCreated = time.time()

    while not rospy.is_shutdown():
        currentState = sailbot.getCurrentState()

        # If next global waypoint reached, update land and border data
        # Update global waypoint in sailbot object
        if nextGlobalWaypointReached(currentState):
            # Update global waypoint and corresponding land+border data
            rospy.loginfo("Updating globalWaypoint")
            if globalPathIndex + 1 < len(globalPath):
                globalPathIndex = globalPathIndex + 1
            else:
                rospy.loginfo("Already at end of globalPath")
            sailbot.globalWaypoint = globalPath[globalPathIndex]
            currentLandAndBorderData = getCurrentLandAndBorderData(currentState)

            # Update local path
            currentPath = createNewPath(currentState, currentLandAndBorderData)
            lastTimePathCreated = time.time()

            # publish 2nd point of new path (not the current position)
            nextLocalWaypointMsg.x = currentPath[1][0]
            nextLocalWaypointMsg.y = currentPath[1][1]

        elif isBad(currentState, currentPath, currentLandAndBorderData) or nextLocalWaypointReached(currentState, nextLocalWaypointMsg) or timeLimitExceeded(lastTimePathCreated):
            rospy.loginfo("Updating currentPath")
            # Update local path
            currentPath = createNewPath(currentState, currentLandAndBorderData)
            lastTimePathCreated = time.time()

            # publish 2nd point of new path (not the current position)
            nextLocalWaypointMsg.x = currentPath[1][0]
            nextLocalWaypointMsg.y = currentPath[1][1]

        rospy.loginfo_throttle(1, "nextLocalWaypointMsg: {0} {1}".format(nextLocalWaypointMsg.x, nextLocalWaypointMsg.y))  # Prints every x seconds
        nextLocalWaypointPublisher.publish(nextLocalWaypointMsg)
        publishRate.sleep()
