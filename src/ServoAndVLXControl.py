#!/usr/bin/python3

import VL53L1X
import RPi.GPIO as GPIO
import time
import rospy
from geometry_msgs.msg import Vector3 

# Open and start the VL53L1X sensor.
# If you've previously used change-address.py then you
# should use the new i2c address here.
# If you're using a software i2c bus (ie: HyperPixel4) then
# you should `ls /dev/i2c-*` and use the relevant bus number.
angle = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
servo = GPIO.PWM(13,50)
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()
servo.start(2.5)

# Optionally set an explicit timing budget
# These values are measurement time in microseconds,
# and inter-measurement time in milliseconds.
# If you uncomment the line below to set a budget you
# should use `tof.start_ranging(0)`'
tof.set_timing(50000, 70)
tof.start_ranging(0)
#tof.start_ranging(3)  # Start ranging
                      # 0 = Unchanged
                      # 1 = Short Range
                      # 2 = Medium Range
                      # 3 = Long Range

# Grab the range in mm, this function will block until
# a reading is returned.

rospy.init_node('publish_range_data')
pub = rospy.Publisher('/range_data',Vector3,queue_size=10)
v = Vector3()
while True:

   if angle>200:
      angle=0
   servo.ChangeDutyCycle((angle+2.5)/18)   
   distance_in_mm = tof.get_distance()
   v.x = (angle/200)*180
   v.y = distance_in_mm/1000
   print(distance_in_mm/1000)
   pub.publish(v)
   time.sleep(0.001) 
   angle+=1
#tof.stop_ranging()