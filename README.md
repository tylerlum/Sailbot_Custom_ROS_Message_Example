# Sailbot_Custom_ROS_Message_Example

The purpose of this repository is to show example Python and C++ code for Sailbot Custom ROS messages.

## Quick Start Instructions

1. Install ROS Melodic on a Ubuntu 18.04 (or similar). http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

2. Find the location that you want to create a ROS workspace (eg. `cd ~`)

3. Type the commands `mkdir -p catkin_ws/src` `cd catkin_ws` `catkin_make`.

4. Clone the repository in the src folder: `cd src` `git clone https://github.com/tylerlum/Sailbot_Custom_ROS_Message_Example.git`. 

5. Go back to catkin_ws and build and source. `cd ..` `cd ..` `catkin_make` `source devel/setup.zsh`.

6. Create a roscore, then run the listener and publisher. `roscore` => open new terminal `source devel/setup.zsh` `rosrun Sailbot_Custom_ROS_Message_Example test_custom_listener` => open new terminal `source devel/setup.zsh` `rosrun Sailbot_Custom_ROS_Message_Example test_custom_talker`.

7. Check what is being sent: open new terminal `rostopic list` `rostopic echo /path` or `rostopic echo /custom_AIS`.

If there are any issues running the code as described above, please let me know and I will try my best to help out. If you are missing packages, you may need to run `sudo apt-get install ros-melodic-XXXX`, eg. `sudo apt-get install ros-melodic-geometry-msgs`. 

## References

Setting up ROS workspace and package

* http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

* http://wiki.ros.org/ROS/Tutorials/CreatingPackage

* http://wiki.ros.org/ROS/Tutorials/BuildingPackages

Creating custom message and setting up CMakeLists and package.xml

* http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_msg

Creating a publisher and subscriber for a custom message

* http://wiki.ros.org/ROS/Tutorials/CustomMessagePublisherSubscriber%28python%29

Debugging Help

* https://answers.ros.org/question/114806/tutorial-116-importerror-no-module-named-beginner_tutorialssrv-with-catkin-system-build/


## Other Message Types

TODO: investigate which message types are best to use for Sailbot

Message Classes

* http://wiki.ros.org/geometry_msgs - Look at Pose, Pose2D, Vector3, Quaternion, Twist

* http://wiki.ros.org/nav_msgs - Look at Path, Occupancy Grid

* http://wiki.ros.org/std_msgs - Lots! Mostly String, Int arrays, time, float arrays

* http://wiki.ros.org/geographic_msgs - GeoPoint, GeoPointStamped, GeographicMap
