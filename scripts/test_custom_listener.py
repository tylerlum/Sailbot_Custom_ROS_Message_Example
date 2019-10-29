#!/usr/bin/env python
import rospy
from test_package.msg import AIS

def callback(data):
    rospy.loginfo(data)

def listener():
    rospy.init_node('custom_AIS_listener', anonymous=True)
    rospy.Subscriber("custom_AIS", AIS, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
