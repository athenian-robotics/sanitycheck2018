import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import time
def settupGetState(system,type):
    listener(system,type)
returned = ""
def getStateSimple(system,type):
    # TODO Return the value sent by the health check topic and the time sense it was received
    return returned
def getStateDetailed(system):
    # TODO Get the logfile and print it
    return "this functionality is not yet implimented"

def callback(data):
    global returned
    returned = str(data) + " | " + str(time.time())


def listener(system):
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('healthcheckbackend')

    rospy.Subscriber(system, String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()