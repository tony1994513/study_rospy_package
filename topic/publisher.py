#!/usr/bin/env python
import rospy
import sys
from study_rospy_package.msg import costom_msg

_rate = 10

def main():
    rospy.init_node("test_ros_topic", anonymous=True)
    pub = rospy.Publisher('test_ros_pub', costom_msg, queue_size=10)
    rate = rospy.Rate(_rate)
    
    while not rospy.is_shutdown():
        pub_msg = costom_msg()
        pub_msg.flag = True
        pub_msg.header.stamp = rospy.Time.now()
        # rospy.loginfo(pub_msg)
        pub.publish(pub_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        sys.exit(main())   
    except rospy.ROSInterruptException:
        pass