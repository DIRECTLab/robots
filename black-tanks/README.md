# Black XiaoR Geek Tanks
Inventory as of 10/18/22:
- All 3 should be working correctly.


## Capabilities
- (x, y) navigation
- Manipulation
- Camera


## How to Use
- These robots use the ROS framework. See the user manual for details.
1. Turn the robot on and connect to `XiaoRGEEK_*` WiFi.
2. SSH into `xrrobot`, e.g. `ssh xrrobot@192.168.1.1`.
3. Many basic controls can be found under `~/catkin_ws/src/basic_navigation/src` and `~/catkin_ws/src/my_camera/src`.

For running the movement:
run:
`roslaunch xrrobot bringup.launch`
This will begin the subscribers necessary for movement

To see camera output in realtime from black robots:
First, start the launch file as follows:
`roslaunch xrrobot camera.launch`
Then, run
`rosrun rqt_image_view rqt_image_view`

To save images:
`rosrun image_view image_saver image:=/camera/rgb/image_raw_filename_format:=image%04i.png`
