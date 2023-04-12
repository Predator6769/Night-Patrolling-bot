#!/usr/bin/python3

import rospy
from ros_npr.msg import robotDirection
from geometry_msgs.msg import Twist

def send_direction(msg):
    direction1 = robotDirection()
    if msg.linear.x > 0:
        direction1.direction = 1
    elif msg.linear.x<0:
        direction1.direction = 2
    elif msg.angular.z>0:
        direction1.direction = 3         
    elif msg.angular.z<0:
        direction1.direction = 4
    else:
        direction1.direction = 0 

    pub.publish(direction1)


if __name__ == '__main__':
    rospy.init_node('robot_direction')
    sub = rospy.Subscriber('/cmd_vel',Twist,send_direction)
    pub = rospy.Publisher('/robotDirection',robotDirection,queue_size=10)
    rospy.spin()

