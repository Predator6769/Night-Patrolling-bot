#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Imu
import tf
import math

def change_data(msg):
    odom = Imu()
    odom.header.stamp = rospy.Time.now()
    odom.header.frame_id = "base_link"
    quat = tf.transformations.quaternion_from_euler(0.0,0.0,math.radians(msg.x))
    
    odom.orientation.x = quat[0]
    odom.orientation.y = quat[1]
    odom.orientation.z = quat[2]
    odom.orientation.w = quat[3]

    odom.angular_velocity.z = msg.y
    odom.linear_acceleration.x = msg.z

    pub.publish(odom)

if __name__ == '__main__':
    rospy.init_node('imu_to_ticks')
    pub = rospy.Publisher('/imu_odom_data',Imu,queue_size=10)
    sub  = rospy.Subscriber('/imu_data',Vector3,change_data)
    rospy.spin()
    