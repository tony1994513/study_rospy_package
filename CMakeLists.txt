cmake_minimum_required(VERSION 2.8.3)
project(study_rospy_package)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  message_generation # add msg need
  actionlib_msgs
  actionlib
)

# find_package(Boost REQUIRED COMPONENTS system)
# catkin_python_setup()

add_message_files(
  FILES
  costom_msg.msg
)
add_service_files(
  FILES
  custom_srv.srv
)

add_action_files(
  FILES
  custom_action.action
)

generate_messages(
  DEPENDENCIES
  std_msgs  
  actionlib_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES study_rospy_package
 CATKIN_DEPENDS rospy roscpp std_msgs message_runtime actionlib actionlib_msgs
#  DEPENDS system_lib
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


