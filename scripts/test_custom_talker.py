#!/usr/bin/env python
import rospy
from test_package.msg import AIS

def talker():
    pub = rospy.Publisher('custom_AIS', AIS)
    rospy.init_node('custom_AIS_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = AIS()
    msg.MMSI = 100000000
    msg.heading = 40
    msg.speedOverGround = 0.1
    msg.latitude = 50.9
    msg.longitude = -123.3
    msg.lastSeen = rospy.Time(10)

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
