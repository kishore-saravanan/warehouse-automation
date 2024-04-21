# Warehouse Automation using Autonomous Mobile Robot and RFID

Hardware used: Arduino UNO, RC522 RFID Module, MIFARE 1KB passive RFID card

Software used: ROS Noetic, Gazebo, ARduino IDE

Steps to run the project:
1. Clone this repository into the src folder of your ROS workspace
2. Install the depenencies using rosdep
3. Build the workspace with catkin_make from the root of your workspace
4. Connect the hardware system to the PC i.e, Arduino UNO
5. Start the sytem by running roslaunch warehouse_automation warehouse2_gazebo.launch
