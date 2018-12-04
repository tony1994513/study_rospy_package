#!/usr/bin/env python
import rospy
import sys
from study_rospy_package.msg import costom_msg

def callback(data):
    rospy.loginfo(data)

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.wait_for_message('test_ros_pub',costom_msg,timeout=2)
    rospy.Subscriber("test_ros_pub", costom_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    sys.exit(main()) 