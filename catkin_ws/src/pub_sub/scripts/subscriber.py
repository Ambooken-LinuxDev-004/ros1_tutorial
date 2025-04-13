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
    rospy.loginfo(rospy.get_caller_id() + "Welcome to ROS %s", msg.data)

def listener():
    rospy.init_node("string_subscriber_node", anonymous=True)
    rospy.Subscriber("string_topic", String, reply)
    rospy.spin()

if __name__ == '__main__':
    listener()
