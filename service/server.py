#!/usr/bin/env python
import rospy
import sys
from study_rospy_package.srv import custom_srv, custom_srvResponse

def cb(req):
    res = custom_srvResponse()
    if req.flag == true:
        res.name = "you got me"
    return res

def main():
    rospy.init_node('server', anonymous=True)
    s = rospy.Service('test_server', custom_srv, cb)
    rospy.spin()


if __name__ == '__main__':
    sys.exit(main()) 