#!/usr/bin/python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Int16

ticksleft = 0
ticksright = 0
prevticksleft = 0
prevticksright = 0
last_time = 0

def leftTicksData(msg):
    global ticksleft
    ticksleft = msg.data

def rightTicksData(msg):
    distancepercount = 2*3.14*0.05/90
    global ticksright,ticksleft,prevticksleft,prevticksright,last_time
    ticksright = msg.data
    current_time = rospy.Time.now()
    dt = (current_time - last_time).to_sec()

    if dt>=0.01:
       deltaLeft = ticksleft - prevticksleft
       deltaRight = ticksright - prevticksright

       omega_left = deltaLeft * distancepercount/dt
       omega_right = deltaRight * distancepercount/dt

       omega = (omega_left + omega_right)/2
       
       odom = Odometry()

       odom.header.stamp = current_time
       odom.header.frame_id = "odom"
       odom.child_frame_id = "base_link"
       odom.twist.twist.linear.x = omega
       pub.publish(odom)
       last_time = current_time
       prevticksleft = ticksleft
       prevticksright = ticksright





if __name__=='__main__':
    rospy.init_node('ticks_to_odom')
    last_time = rospy.Time.now()
    sub1 = rospy.Subscriber('/left_ticks',Int16,leftTicksData)
    sub2 = rospy.Subscriber('/right_ticks',Int16,rightTicksData)
    pub = rospy.Publisher('/ticks_odom',Odometry,queue_size=10)
    rospy.spin()