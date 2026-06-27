# Practice 6: ROS 2 Publisher with Custom Message 


Sometimes, we may need to publish our own type of messages when the standard ROS 2 message types do not fully meet the needs of our application. For example, if we want to send a tailored message containing multiple fields, we need to define a custom message. In this exercise, you will learn how to create and define a custom .msg file, configure your ROS 2 package to support custom messages, and build the package accordingly. You will then implement a publisher node that uses this custom message type to publish data to a topic.

## Learning Outcomes
By the end of this practice, learners will be able to:
- Understand the structure and syntax of custom messages in ROS 2.
- Define and create a custom message type using .msg files.
- Configure the ROS 2 package to build and use custom messages.

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 Subscribers.

1. **Practice 6A: Creating a Custom Message Interface**

   - [6A.1: Creating a Custom Message Interface](#6a1-creating-a-custom-message-interface)
   - [6A.2: Verifying Custom Message Interface](#6a2-verifying-custom-message-interface)
   - [6A.3: Creating a ROS2 Publisher using the Custom Message](#6a3-creating-a-ros2-publisher-using-the-custom-message)
   - [6A.4: Verifying your ROS2 Custom Message Publisher](#6a4-verifying-your-ros2-custom-message-publisher)

## 6A.1: Creating a Custom Message Interface

1. Within the same `ros2_ws` where you have done your previous practical at, go into the src folder
2. Create a ROS 2 `ament_cmake` package named `simple_velocity_msg` within the src folder. Must be `ament_cmake` package!
3. Inside the `simple_velocity_msg` package, create a folder named `msg`
4. Inside the `msg` folder , create a message interface named `SimpleVelocity.msg` (Hint: use touch command!)
    - Remember that your interface file should be named in CamelCase, as it is part of the ROS 2 guidelines
    - Your interface file shall contain two `float64` type fields named **linear_velocity** and **angular_velocity** respectively.

5. Inside your CMakelist.txt, include the necessary dependencies below `# find_package(<dependency> REQUIRED)`
```
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/SimpleVelocity.msg"
  DEPENDENCIES
)
```

6. Inside your `package.xml` file , include the following dependecies within the `<package>` element of `package.xml` file.

```
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
7. Make sure that all the files are saved prior to building the `simple_velocity_msg` package.

8. Build `simple_velocity_msg` package.

## 6A.2: Verifying Custom Message Interface

Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

To check if your solution works, go into a new terminal and run the following commands:

``` bash
cd ros2_ws
source install/setup.bash
ros2 interface list

ros2 interface list | grep SimpleVelocity             # to look for the exact message
```
You should be able to see `simple_velocity_msg/msg/SimpleVelocity` as one of the interfaces under `Messages`

## 6A.3: Creating a ROS2 Publisher using the Custom Message

1. Within the `ros2_ws` folder , go inside the src folder
2. Create a ROS 2 python package named `custom_msg_publisher` within the src folder 
3. Create a ROS 2 executable in this package named `simple_velocity_pub_node`
4. You may use the provided code boiler plate below as a starting point

```python
import rclpy
from rclpy.node import Node
#------------------------------------------------
#                    TODO:
#  Import your SimpleVelocity here
#------------------------------------------------
from geometry_msgs.msg import Twist


class SimpleVelPublisherNode(Node):
    def __init__(self):
        super().__init__('simple_vel_publisher')
        #------------------------------------------------
        #                    TODO:
        #  Create your publisher below! Remember that your
        #  publishes SimpleVelocity type message to a topic called
        #  simple_vel
        #------------------------------------------------
        #------------------------------------------------
        #                    TODO:
        #  Create your subscriber below! Remember that your
        #  subscribes to twist type message from the topic
        #  cmd_vel. User listener_callback as its callback function
        #------------------------------------------------
        #------------------------------------------------
        #                    TODO:
        #  Once you have completed creating your publisher,
        #  Initialise a twist message and call it self.msg
        #------------------------------------------------
        #------------------------------------------------
        #                    TODO:
        # Create your timer below and it should be set at
        # 1 seconds, use timer_callback() as its callback function
        #------------------------------------------------
    def listener_callback(self, msg):
        self.msg = msg

    def timer_callback(self):
        #------------------------------------------------
        #                    TODO:
        #  Create a SimpleVelocity Object and name it msg
        #------------------------------------------------
        msg.linear_velocity = self.msg.linear.x
        msg.angular_velocity = self.msg.angular.z
        #------------------------------------------------
        #                    TODO:
        #  Create a line below that publishes the msg object to
        #  the topic 
        #------------------------------------------------
        self.get_logger().info('Publishing linear velocity: "%s" m/s, angular velocity: "%s" rad/s' % (msg.linear_velocity, msg.angular_velocity))

def main(args=None):
    rclpy.init(args=args)
    node = SimpleVelPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

5. Inside the `simple_velocity_pub_node file`, implement the following task.
    1. Import the `SimpleVelocity` Message. 
    2. Create a publisher node that publishes the `SimpleVelocity` messages to the `simple_vel` topic.
    3. Create a subscriber that listens to `Twist` messages on the `cmd_vel` topic.
    4. Initialise a twist message and call it self.msg
    5. Create a timer and it should be set at 1 seconds
    6. Implement a timer callback function that is called every second. 
        - Publish the Velocity message to the simple_vel topic.
    - #### Use the comments in the provided code boiler plate as a guideline


6. Inside your `package.xml` file, include the following dependecies within the `<package>` element of `package.xml` file

```
<exec_depend>simple_velocity_msg</exec_depend>
```

7. Make sure that all the files are saved prior to building the `custom_msg_publisher` package.

## 6A.4: Verifying your ROS2 Custom Message Publisher


Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

### 1. Bringup and initialise the turtlebot **(Optional)**


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

In one terminal:

``` linux
    cd ros2_ws
    source install/setup.bash
    ros2 run custom_msg_publisher simple_velocity_pub_node
```

In another  terminal:

``` linux
ssh ubuntu@<turtlebot ip address>
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Once you see the following output from the terminal, it means that you have successfully completed this pratical. 

```
[INFO] [1714114534.937899659] [SimpleVelPublisherNode]: Publishing linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714114535.931171274] [SimpleVelPublisherNode]: Publishing linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714114536.931050675] [SimpleVelPublisherNode]: Publishing linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714114537.931097800] [SimpleVelPublisherNode]: Publishing linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
[INFO] [1714114538.931091920] [SimpleVelPublisherNode]: Publishing linear velocity: "0.15" m/s, angular velocity: "0.9999999999999999" rad/s
```
