#! /usr/bin/env python
import rospy
import sys
import actionlib
from study_rospy_package.msg import custom_actionGoal, custom_actionAction


def main():
    rospy.init_node('action_client', anonymous=True)
    client = actionlib.SimpleActionClient('custom_do_dishes', custom_actionAction)
    if client.wait_for_server(timeout=rospy.Duration(3)) != True:
        rospy.logerr("action server is not available")
        sys.exit()
    goal = custom_actionGoal()
    goal.dishwasher_id = 1
    client.send_goal(goal)
    
    if client.wait_for_result(rospy.Duration.from_sec(5.0)) != True:
        rospy.logerr("cannot get result")
        sys.exit()
    result = client.get_result()
    rospy.loginfo(result)


if __name__ == '__main__':
    sys.exit(main()) 