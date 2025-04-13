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


def talker():
    rospy.init_node("string_publisher_node", anonymous=True)
    pub = rospy.Publisher("string_topic", String, queue_size=10)
    rate = rospy.Rate(10)
    msg = String()
    msg.data = str
    while rospy.is_shutdown():
        msg = "Hello %s" % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rospy.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass