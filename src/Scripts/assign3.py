#!/usr/bin/env python

import rospy
from turtlesim.msg import *
from turtlesim.srv import *
from geometry_msgs.msg import Twist
from std_srvs.srv import *
import random
from time import time
from math import atan2,pi, sqrt, pow
import sys

if __name__ == '__main__':
    try:
        global pub, pubrunner, rate, motion
        rospy.init_node('turtleNav', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	pubrunner = rospy.Publisher('/runner/cmd_vel', Twist, queue_size = 10)
        rospy.Subscriber("/turtle1/pose", Pose, hunterPose)

#rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 1.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}'


    except rospy.ROSInterruptException:
        pass
