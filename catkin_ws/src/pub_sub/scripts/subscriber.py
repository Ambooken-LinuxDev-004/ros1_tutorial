#!/usr/bin/env python3

"""
import rospy
from std_msgs.msg import Int64

# Callback function
def callback(msg):
    print(msg)

# Node + Subscriber initialization
rospy.init_node("subscriber_node")
rospy.Subscriber("topic", Int64, callback)

# Spinning
rospy.spin()

"""

import rospy
from std_msgs.msg import String

def reply(msg):
    print("Hello " + msg + ", Welcome to ROS!!...")

rospy.init_node("string_subscriber_node")
rospy.Subscriber("string_topic", String, reply)

rospy.spin()
