#! /usr/bin/env python3

"""
import rospy
from std_msgs.msg import Int64

# Node + Topic initialization
rospy.init_node("publisher_node")
pub = rospy.Publisher("topic", Int64, queue_size=1)


# Looping
while not rospy.is_shutdown():
    pub.publish(1)
    rospy.sleep(1)

"""

import rospy
from std_msgs.msg import String

rospy.init_node("string_publisher_node")
pub = rospy.Publisher("string_topic", String, queue_size=10)
msg = String()
msg.data = "Joe"

while rospy.is_shutdown():
    pub.publish(msg.data)
    rospy.sleep(1)