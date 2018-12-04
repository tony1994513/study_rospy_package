#! /usr/bin/env python
import rospy
import sys
import actionlib
import numpy as np
from study_rospy_package.msg import custom_actionResult,custom_actionAction, custom_actionFeedback

num_list = [0.1,0.5,1]

class DoDishesServer():
    _feedback = custom_actionFeedback()
    _result = custom_actionResult()

    def __init__(self):
        self.server = actionlib.SimpleActionServer('custom_do_dishes', custom_actionAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        if self.server.is_active():
            print "action server activated"  
        r = rospy.Rate(1)
        success = True   # check if preempted called 

        for i in num_list:
            if self.server.is_preempt_requested():
                rospy.loginfo('Action Preempted')
                self.server.set_preempted()
                success = False
                break

            self._feedback.percent_complete = i
            self.server.publish_feedback(self._feedback)
            r.sleep()
        
        if success:
            self._result.total_dishes_cleaned = 1
            self.server.set_succeeded(self._result)
        
def main():
    rospy.init_node('action_server', anonymous=True)
    server = DoDishesServer()
    rospy.spin()

if __name__ == '__main__':
    sys.exit(main()) 