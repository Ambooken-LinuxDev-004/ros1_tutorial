#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("control")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 1)

msg = Twist()
msg.linear.x = -1

"""msg.linear.y = 2
msg.linear.z = 3
msg.angular.x = 1
msg.angular.y = 4
msg.angular.z = 9"""

"""while not rospy.is_shutdown():
    pub.publish(msg)
    rospy.sleep(1)"""

for i in range(5):
    pub.publish(msg)
    rospy.sleep(1)

