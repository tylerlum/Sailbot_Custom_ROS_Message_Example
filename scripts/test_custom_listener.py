#!/usr/bin/env python
import rospy
from Sailbot_Custom_ROS_Message_Example.msg import AIS
from geometry_msgs.msg import Pose2D

msg = Pose2D()
msg.x = 0
msg.y = 0
msg.theta = 0

def callback(data):
    rospy.loginfo(data)
    msg.x = data.latitude
    msg.y = data.longitude

def listener():
    rospy.init_node('custom_AIS_listener', anonymous=True)
    rospy.Subscriber("custom_AIS", AIS, callback)
    pub = rospy.Publisher("path", Pose2D)
    r = rospy.Rate(10) #10hz

    while not rospy.is_shutdown():
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    listener()
