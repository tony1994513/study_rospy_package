#!/usr/bin/env python

import rospy
import sys
from study_rospy_package.srv import custom_srv, custom_srvRequest


def main():
    rospy.init_node('client', anonymous=True)
    rospy.wait_for_service('test_server',timeout=3)
    try:
        req = custom_srvRequest()
        req.flag = True
        client = rospy.ServiceProxy('test_server', custom_srv)
        res = client(req)
        rospy.loginfo("res is %s", res)
    except rospy.ServiceException, e:
        rospy.loginfo("Service call failed: %s"%e)


if __name__ == '__main__':
    sys.exit(main()) 