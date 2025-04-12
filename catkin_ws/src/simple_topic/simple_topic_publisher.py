#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("simple_topic_publisher_node")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist)
rate = rospy.Rate(2)
speed = Twist()

speed.linear.x = 0
speed.linear.y = 0
speed.linear.z = 0

speed.angular.x = 0
speed.angular.y = 0
speed.angular.z = 0

while not rospy.is_shutdown():
    pub.publish(speed)
    speed.linear.x += 1
    speed.angular.z += 1
    rate.sleep()
