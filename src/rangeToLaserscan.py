#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3

ranges = []
def change_range_to_laserscan(msg):
  global ranges
  if msg.x<179:
    ranges.append(msg.y)
  else:
    ranges.append(msg.y)  
    laser = LaserScan()
    laser.header.stamp = rospy.Time.now()
    laser.header.frame_id = 'base_link'
    laser.angle_min = -1.5707963
    laser.angle_max = 1.5707963
    laser.angle_increment = 0.015707
    laser.time_increment = 0.001
    laser.range_min = 0.02
    laser.range_max = 4.0
    laser.ranges = ranges.copy()
    pub.publish(laser)

if __name__ == '__main__':

    rospy.init_node('laser_scan_node')
    pub = rospy.Publisher('/laser_scan_data',LaserScan,queue_size=10)
    sub = rospy.Subscriber('/range_data',Vector3,change_range_to_laserscan)
    rospy.spin()
