# Practice 7: ROS 2 Subscriber with Custom Message 

In many ROS 2 applications, subscribing to custom message types is essential for handling structured or application-specific data. This exercise will involve participants writing a subscriber node that listens to a topic publishing custom messages such as those created in the previous practice. Through this, learners will understand how to work with non-standard ROS2 message types, extract and process data from custom fields, and test message flow within a ROS 2 system.

## Learning Outcomes
By the end of this practice, learners will be able to:
- Understand how to subscribe to topics that use custom message types in ROS 2.
- Implement a ROS 2 Subscriber node that correctly interprets and processes custom message data.
- Use ROS 2 CLI tools to inspect message types and verify message structure.
- Demonstrate the ability to integrate and test custom message-based communication within a ROS 2 system.

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 Subscribers.

1. **Practice 7A: Creating a Custom Message Interface**

   - [7A.1: Creating a ROS2 Subscriber using Custom Message](#7a1-creating-a-ros2-subscriber-using-custom-message)
   - [7A.2: Verifying your ROS2 Custom Message Subscriber](#7a2-verifying-your-ros2-custom-message-subscriber)

## 7A.1: Creating a ROS2 Subscriber using Custom Message

**Technical Requirements**

1. Within the same `ros2_ws` where you have done your previous pratical at, go into the src folder
2. Create a ROS 2 python package named `custom_msg_subscriber` within the src folder 
3. Create a ROS 2 excutable in this package named `simple_velocity_sub_node`
4. You may use the provided code boiler plate below as a starting point
5. Inside the `simple_velocity_sub_node` file , implement the following task.

    - Create a subscriber node that listens to the `SimpleVelocity` messages that is published on the `/simple_vel` topic.
    - Create a callback function that logs the linear and angular velocity from the received messages.
    - Remeber to import your `SimpleVelocity` message in order to run this pratical
    - Use the comments in the provided code boiler plate as a guideline

```python

import rclpy
from rclpy.node import Node
#------------------------------------------------
#                    TODO:
#  Import your SimpleVelocity here
#------------------------------------------------
class MySubscriber(Node):

    def __init__(self):
        super().__init__('MySubscriber')
        #------------------------------------------------
        #                    TODO:
        #  Create your subscriber below! Remember that your
        #  subscribes to SimpleVelocity type message from the 
        #  topic simple_vel
        #------------------------------------------------
    #------------------------------------------------
    #                    TODO:
    #  Create a callback function for your subscriber
    #  Inside this function create a line that logs
    #  the message

    #------------------------------------------------
def main(args=None):
    rclpy.init(args=args)
    my_subscriber = MySubscriber()
    rclpy.spin(my_subscriber)
    my_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
6. Inside your `package.xml` file, include the following dependecies within the <package> element of `package.xml` file

```
 <exec_depend>simple_velocity_msg</exec_depend>
```

7. Make sure that all the files are saved prior to building the `custom_msg_subscriber` package.

## 7A.2: Verifying your ROS2 Custom Message Subscriber

Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

1. Bringup and initialise the turtlebot **(Optional)**

Check that you have **CONNECTED TO THE SAME NETWORK AS YOUR TURTLEBOT**.

In a new terminal, run the following commands:

```bash
ssh ubuntu@<ip_address>
ros2 launch turtlebot3_bringup robot.launch.py 
```
Once you see the following output from the terminal, it means that you have successfully bringup the turtlebot.

```bash
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2019-08-19-01-24-19-009803-ubuntu-15310
[INFO] [launch]: Default logging verbosity is set to INFO
urdf_file_name : turtlebot3_burger.urdf
[INFO] [robot_state_publisher-1]: process started with pid [15320]
[INFO] [hlds_laser_publisher-2]: process started with pid [15321]
[INFO] [turtlebot3_ros-3]: process started with pid [15322]
[robot_state_publisher-1] Initialize urdf model from file: /home/ubuntu/turtlebot_ws/install/turtlebot3_description/share/turtlebot3_description/urdf/turtlebot3_burger.urdf
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link base_link had 5 children
[robot_state_publisher-1] Link caster_back_link had 0 children
[robot_state_publisher-1] Link imu_link had 0 children
[robot_state_publisher-1] Link base_scan had 0 children
[robot_state_publisher-1] Link wheel_left_link had 0 children
[robot_state_publisher-1] Link wheel_right_link had 0 children
[robot_state_publisher-1] got segment base_footprint
[robot_state_publisher-1] got segment base_link
[robot_state_publisher-1] got segment base_scan
[robot_state_publisher-1] got segment caster_back_link
[robot_state_publisher-1] got segment imu_link
[robot_state_publisher-1] got segment wheel_left_link
[robot_state_publisher-1] got segment wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init TurtleBot3 Node Main
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init DynamixelSDKWrapper
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to open the port(/dev/ttyACM0)!
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to change the baudrate!
[robot_state_publisher-1] Adding fixed segment from base_footprint to base_link
[robot_state_publisher-1] Adding fixed segment from base_link to caster_back_link
[robot_state_publisher-1] Adding fixed segment from base_link to imu_link
[robot_state_publisher-1] Adding fixed segment from base_link to base_scan
[robot_state_publisher-1] Adding moving segment from base_link to wheel_left_link
[robot_state_publisher-1] Adding moving segment from base_link to wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Start Calibration of Gyro
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Calibration End
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Motors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Wheels
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Sensors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create battery state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create imu publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sensor state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create joint state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Devices
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create motor power server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create reset server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sound server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Run!
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Init Odometry
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Run!
```

2. To check if your solution works, go into a new terminal and run the following commands:

Run your `simple_velocity_pub_node` from Practical 6's `custom_msg_publisher` package

``` linux
cd ros2_ws
source install/setup.bash
ros2 run custom_msg_publisher simple_velocity_pub_node
```
Run your `simple_velocity_sub_node` node
 Enter this command in your terminal:

``` linux
cd ros2_ws
source install/setup.bash
ros2 run custom_msg_subscriber simple_velocity_sub_node
```

In another terminal:

``` linux
ssh ubuntu@<turtlebot ip address>
ros2 run turtlebot3_teleop teleop_keyboard
```

Once you see the following output from the terminal, it means that you have successfully completed this pratical. 

```
[INFO] [1714115107.187829907] [MySubscriber]: Received linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714115108.183861835] [MySubscriber]: Received linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714115109.183653317] [MySubscriber]: Received linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714115110.183785031] [MySubscriber]: Received linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714115111.183750838] [MySubscriber]: Received linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
```
