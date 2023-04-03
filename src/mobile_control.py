#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
goal = String()


def entry_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("rfid_string", String, queue_size=10)
    goal.data = 'WAREHOUSE-AUTOM1'
    pub.publish(goal)

def exit_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("rfid_string", String, queue_size=10)
    goal.data = 'WAREHOUSE-AUTOM2'
    pub.publish(goal)

def home_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("rfid_string", String, queue_size=10)
    goal.data = 'WAREHOUSE-AUTOM0'
    pub.publish(goal)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    
    sub_entry = rospy.Subscriber("warehouse_entry", Bool, entry_callback)
    sub_exit = rospy.Subscriber("warehouse_exit", Bool, exit_callback)
    sub_home = rospy.Subscriber("warehouse_home", Bool, home_callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
