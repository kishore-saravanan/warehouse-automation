#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from std_msgs.msg import String




#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal,ox,oy,oz,ow):

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0
   goal.target_pose.pose.orientation.y = 0
   goal.target_pose.pose.orientation.z = 0
   goal.target_pose.pose.orientation.w = 1

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("You have reached the destination")
           return True

   else:
           rospy.loginfo("The robot failed to reach the destination")
           return False

def navigate(rfid):
     if rfid.data[15]:
          goal = rfid.data[15]
     if goal == "0":
          move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])
     elif goal == "1":
          move_to_goal(entry[0],entry[1],entry[3],entry[4],entry[5],entry[6])
     
     elif goal == "2":
          move_to_goal(exit[0],exit[1],exit[3],exit[4],exit[5],exit[6])
     
     elif goal == '3':
          move_to_goal(goal3[0],goal3[1],goal3[3],goal3[4],goal3[5],goal3[6])
     
     elif goal == '4':
          move_to_goal(goal4[0],goal4[1],goal4[3],goal4[4],goal4[5],goal4[6])
     
     elif goal == '5':
          move_to_goal(goal5[0],goal5[1],goal5[3],goal5[4],goal5[5],goal5[6])
     
     elif goal == '6':
          move_to_goal(goal6[0],goal6[1],goal6[3],goal6[4],goal6[5],goal6[6])

     else:
          print("Waiting for goal")

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   sub = rospy.Subscriber("rfid_string", String, navigate)
   '''x_goal = -2.02880191803
   y_goal = 4.02200937271'''
   home = [8.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0]
   entry = [8.723656877822293,0.5375857569741491,0.0,0.0,0.0,-0.999445627675465,0.03329320231512544]
   exit = [8.810370224696015,-5.894353139585141,0.0,0.0,0.0,-0.9999682018937511,0.007974659953767154]
   goal3 = [-6.6761925693959325,-6.490823899175572,0.0,0.0,0.0,-0.003974783198782483,0.9999921005180604]
   goal4 = [-6.93644542639109,-3.4029701158804118,0.0,0.0,0.0,-0.0015036210202985423,0.9999988695612747]
   goal5 = [-6.951723787441815,-0.11731550426398146,0.0,0.0,0.0,0.0012163458967926978,0.999999260251056]
   goal6 = [-6.937584960029826,3.0563924901340127,0.0,0.0,0.0,0.0007978924792340481,0.9999996816837451]
     
   '''while(1):
     print(' 0 - Home \n 1 - Entry \n 2 - Exit \n 3 - Goal 3 \n 4 - Goal 4  \n 5 - Goal 5 \n 6 - Goal 6 \n')
     goal = int(input("Enter the Goal location:"))
   
     if goal == 0:
               move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])
     elif goal == 1:
          move_to_goal(entry[0],entry[1],entry[3],entry[4],entry[5],entry[6])
     
     elif goal == 2:
          move_to_goal(exit[0],exit[1],exit[3],exit[4],exit[5],exit[6])
     
     elif goal == 3:
          move_to_goal(goal3[0],goal3[1],goal3[3],goal3[4],goal3[5],goal3[6])
     
     elif goal == 4:
          move_to_goal(goal4[0],goal4[1],goal4[3],goal4[4],goal4[5],goal4[6])
     
     elif goal == 5:
          move_to_goal(goal5[0],goal5[1],goal5[3],goal5[4],goal5[5],goal5[6])
     
     elif goal == 6:
          move_to_goal(goal6[0],goal6[1],goal6[3],goal6[4],goal6[5],goal6[6])

     else:
          print("Invalid goal")   
          break '''

   rospy.spin()
