import time
import rospy
import dataVault
from std_msgs.msg import String

def callback(data):
    pass

def listener(system):
    rospy.init_node('healthcheckbackend')

    rospy.Subscriber(system, String, callback)
    rospy.spin()