# Practice 3: Create your own ROS 2 Publisher Node 

In this practice, you will learn how to create and use ROS 2 publisher nodes to send data to a Turtlebot3. You’ll start by building a simple publisher in Python and observing how it communicates by publishing messages to a topic. Then, you’ll apply this knowledge in a more practical context by controlling a TurtleBot3 using teleoperation commands.

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 Publishers.

1. **Practice 3A: Creating a Simple ROS2 Publisher**

   - [3A.1: Creating a Simple Publisher](#3a1-creating-a-simple-publisher)
   - [3A.2: Listening to ROS2 Topic Messages](#3a2-listening-to-ros2-topic-messages) 

2. **Practice 3B: Application of ROS2 Publishers with Turtlebot3**

   - [3B.1: Creating a Turtlebot3 Teleoperation Module](#3b1-creating-a-turtlebot3-teleoperation-module)
   - [3B.2: Verification of Turtlebot3 Teleoperation Module](#3b2-verification-of-turtlebot3-teleoperation-module)
   - [3B.3: Controlling a Simulated Turtlebot3](#3b3-controlling-a-simulated-turtlebot3)
   - [3B.4: Controlling a Physical Turtlebot3](#3b4-controlling-a-physical-turtlebot3)

## Learning Outcomes

By the end of this exercise, you will be able to:

- Understand the role of publishers in the ROS 2 communication system.
- Create and configure a simple ROS 2 publisher node in Python.
- Publish messages to a topic and verify communication using ROS 2 CLI tools.
- Monitor topic activity and debug message flow in a ROS 2 system.
- Apply publisher concepts in real-world scenarios, such as controlling a TurtleBot3 in both simulation and physical environments.

You will be using a **ROS2 Publisher** to publish some messages to the topic named `/cmd_vel`, which is used to control the actual turtlebot hardware.

## 3A.1: Creating a Simple Publisher

Note: Make sure that the my_python_package from the previous practice still exists and that its executable is properly set up and accessible.

1. Open the my_node.py file you created in the previous exercise using Visual Studio Code by running the following command in your terminal:

```bash
code ~/training/new_workspace/src/my_python_package/my_python_package/my_node.py
```

2. Copy the Python script below into `my_node.py`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyExampleNode(Node):
    def __init__(self):
        super().__init__('my_example_node')
        self.counter = 0
        self.publisher_ = self.create_publisher(String, '/my_string', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('my_example_node has started.')

    def timer_callback(self):
        self.counter += 1
        msg = String()
        msg.data = f'Publishing message number {self.counter}'
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyExampleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**Explanation**
- `from std_msgs.msg import String` : Imports the ROS2 String message type from the std_msgs ROS2 package, which is used to publish text messages.
- `self.counter = 0` : A counter variable is initialized to keep track of how many messages have been published.
- `self.publisher_ = self.create_publisher(String, '/my_string', 10)` : Creates a publisher that sends String (Not Python native string type!) messages to the /my_string topic with a queue size of 10.
- `self.timer = self.create_timer(1.0, self.timer_callback)` : Sets up a timer to call the timer_callback method every 1 second.
- `def timer_callback(self)` : Defines the callback function that gets triggered by the timer.
- `self.counter += 1` : Increments the counter each time the timer callback is executed.
- `msg = String()` : Creates a new String message object.
- `msg.data = f'Publishing message number {self.counter}'` : Assigns a string message with the current count.
- `self.publisher_.publish(msg)`: Publishes the message to the /my_string topic.

3. Build `my_python_package`. Ensure that you are in the correct directory!

```bash
cd ~/training/new_workspace
colcon build --packages-select my_python_package
```

4. Run the executable. (Note: It is not needed to source the workspace since we are editing a script that was built before!)

```bash
ros2 run my_python_package my_node_executable
```

## 3A.2: Listening to ROS2 Topic Messages

1. Open another terminal, execute the following command to display all the available topics

```bash
ros2 topic list
```

You should see /my_string if your node is running and publishing.

2. Query information about the topic `/my_string`

```bash
ros2 topic info /my_string
```

This command shows details about the topic, including its message type, publishers, and subscribers.

3. Listen to messages published to `/my_string` topic

```bash
ros2 topic echo /my_string
```
Subscribes to the topic and prints the messages being published in real time.

You should be able to see the following output from your terminal.
```linux
johnaa@johnaa-aftershock:~/training/new_workspace$ ros2 topic list
/my_string
/parameter_events
/rosout

johnaa@johnaa-aftershock:~/training/new_workspace$  ros2 topic info /my_string
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0

johnaa@johnaa-aftershock:~/training/new_workspace$   ros2 topic echo /my_string
data: Sent from my_example_node 14
---
data: Sent from my_example_node 15
---
data: Sent from my_example_node 16
---
data: Sent from my_example_node 17

```

## 3B.1: Creating a Turtlebot3 Teleoperation Module

Now that we know how to create a ROS 2 publisher, let's use that knowledge to build a TurtleBot3 teleoperation module. This module will allow us to publish velocity commands to the robot, enabling basic keyboard-controlled movement by sending messages to the appropriate topic `/cmd_vel`. This is a practical example of how publishers are used to control robots in ROS 2.

In this exercise, you will be able to create a package that allows you to control a simulated and physical Turtlebot with your keyboard. 

The method to control the turtlebot should behave as follows:

```bash
Control your TurtleBot3!
---------------------------
Moving around:
        w    
   a    s    d
        x    

w/x : increase/decrease linear velocity 
a/d : increase/decrease angular velocity 
s : stop
```
**Technical Requirements**

1. Create a **workspace** named `ros2_ws`  

2. Within the `ros2_ws` folder, create a `src` folder  

3. Create a ROS 2 **Python package** named `teleop_keyboard`

4. Create a ROS 2 **executable** in this package named `teleop_node`

    - You may use the provided code boiler plate below. **Complete the missing `TODO` sections in the script** — create the publisher and publish the `Twist` velocity command based on the keyboard input.

```python
import os
import select
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

INSTRUCTIONS = """
Control your TurtleBot3!
---------------------------
Moving around:
        w    
   a    s    d
        x    

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
s : stop

CTRL-C to quit
"""

def get_key(settings):
    if os.name == 'nt':
        return msvcrt.getch().decode('utf-8')
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    key = sys.stdin.read(1) if rlist else ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class TeleopKeyboard(Node):
    def __init__(self):
        super().__init__('teleop_keyboard')
        self.get_logger().info("TeleopKeyboard node has started.")

        #------------------------------------------------
        #                    TODO:
        #  Create your publisher here! Remember to check
        #  what is the publisher type you need.
        #  Once you have completed creating your publisher,
        #  Initialise a twist message and call it self.cmd_msg
        #------------------------------------------------

        #-------- A Timer is created here every 0.1s, the timer_callback() function will be called. ---------
        self.timer = self.create_timer(
            0.1, self.timer_callback
        )

        print(INSTRUCTIONS)

    def timer_callback(self):
        settings = termios.tcgetattr(sys.stdin) if os.name != 'nt' else None
        key = get_key(settings)

        if key == 'w':
            self.cmd_msg.linear.x += 0.1
            self.get_logger().info(f"Moving forward | Linear: {self.cmd_msg.linear.x:.2f} Angular: {self.cmd_msg.angular.z:.2f}")
        elif key == 'x':
            self.cmd_msg.linear.x -= 0.1
            self.get_logger().info(f"Moving backward | Linear: {self.cmd_msg.linear.x:.2f} Angular: {self.cmd_msg.angular.z:.2f}")
        elif key == 'a':
            self.cmd_msg.angular.z += 0.1
            self.get_logger().info(f"Turning left | Linear: {self.cmd_msg.linear.x:.2f} Angular: {self.cmd_msg.angular.z:.2f}")
        elif key == 'd':
            self.cmd_msg.angular.z -= 0.1
            self.get_logger().info(f"Turning right | Linear: {self.cmd_msg.linear.x:.2f} Angular: {self.cmd_msg.angular.z:.2f}")
        elif key == 's':
            self.cmd_msg.linear.x = 0.0
            self.cmd_msg.angular.z = 0.0
            self.get_logger().info("Stopping robot.")

        #-------------------------------------------------
        #                    TODO:
        #          Write your code here!
        #          Now you have the keyboard input from the 
        #          User, what do you do with it?
        #-------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    node = TeleopKeyboard()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting gracefully...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**Explanation**

- `settings = termios.tcgetattr(sys.stdin) if os.name != 'nt' else None `: Gets the current terminal settings on Ubuntu (or other Unix systems) so they can be restored later after reading a key. It's skipped on Windows.
- `key = get_key(settings)` : calls the `get_key()` function to read a single key press from the user and stores it in the variable key.

5. Finish the Implementation!

This exercise, you are given a partially completed ROS 2 node that will allow you to control a TurtleBot3 using your keyboard.
Your task is to complete the missing parts of the code so the node can read keyboard input and publish movement commands to the /cmd_vel topic using a Twist message.

## 3B.2: Verification of Turtlebot3 Teleoperation Module

1. Build the `teleop_keyboard` package by running the following command, and ensure that it compiles successfully:

```linux
colcon build --packages-select teleop_keyboard
```

2. Source your workspace! Run the `teleop_keyboard`'s executable, `teleop_node`

```linux
ros2 run teleop_keyboard teleop_node
```

3. Open another terminal (separate terminal for easy access) and listen to '/cmd_vel' topic

```linux
ros2 topic echo /cmd_vel
```

4. Press any key 'W', 'A', 'S', or 'D' on the previous terminal (where teleop_keyboard executable is running) observe the changes in value. 

```bash
---
    linear:
    x: -0.09999999999999998
    y: 0.0
    z: 0.0
    angular:
    x: 0.0
    y: 0.0
    z: 0.19999999999999998
    ---
    linear:
    x: -0.09999999999999998
    y: 0.0
    z: 0.0
    angular:
    x: 0.0
    y: 0.0
    z: 0.19999999999999998
```

When you press the keys:

- **W**: Increases linear.x by 0.1 each time — the robot moves forward faster.
- **X**: Decreases linear.x by 0.1 each time — the robot moves backward faster.
- **A**: Increases angular.z by 0.1 — the robot turns more sharply to the left.
- **D**: Decreases angular.z by 0.1 — the robot turns more sharply to the right.
- **S**: Sets both linear.x and angular.z to 0.0 — the robot stops moving.

## 3B.3: Controlling a Simulated Turtlebot3

1. To check if your solution works in robot simulation, open a **new** terminal and run the following:

```bash
export TURTLEBOT3_MODEL=burger
cd ~/ros2basics_ws
source install/setup.bash
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

2. Control the simulated Turtlebot3 using WASD keys and watch the Turtlebot3 move!

## 3B.4: Controlling a Physical Turtlebot3

1. Open a new terminal to bringup and initialise the Turtlebot3. the IP address is specific to TurtleBot3.

```bash
    ssh ubuntu@<ip_address>
    ros2 launch turtlebot3_bringup robot.launch.py 
```

Once you see the following output from the terminal, it means that you have successfully bringup the Turtlebot3.
```linux
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

2. Open another terminal, and set ROS_DOMAIN_ID of the Turtlebot3, according to the Turtlebot Number. (Only one user need to do this)

For example, if your assigned Turtlebot is Turtlebot05 uses `ROS_DOMAIN_ID=5`, run:

```bash
echo "export ROS_DOMAIN_ID=5" >> ~/.bashrc
```

Next, source the bashrc file.

```bash
source ~/.bashrc
```

4. On your Personal Computer (Virtual Machine), check if Turtlebot3 topics are visible.

```bash
ros2 topic list
```
You should be able to see the Turtlebot3's ROS2 topics below:

```bash
johnaa@johnaa-aftershock:~/ros2_ws$ ros2 topic list
/camera_info
/clock
/cmd_vel
/image_raw
/imu
/joint_states
/odom
/parameter_events
/performance_metrics
/robot_description
/rosout
/scan
/tf
/tf_static
```

If the topics listed above are not visible, make sure your `ROS_DOMAIN_ID` matches the one used by the TurtleBot3. You can do this by checking your PCs `ROS_DOMAIN_ID value`:

```bash
echo $ROS_DOMAIN_ID
```

To change ROS_DOMAIN_ID value for the current terminal, execute the following command:

```bash
export ROS_DOMAIN_ID=<TARGET_ROS_DOMAIN_ID>

(e.g export ROS_DOMAIN_ID=5) # assuming Turtlebot3's ROS_DOMAIN_ID is 5
```

To make this setting permanent for future terminals, add it to your .bashrc file:

```bash
echo "export ROS_DOMAIN_ID=<TARGET_ROS_DOMAIN_ID>" >> ~/.bashrc
source ~/.bashrc
```

For example:

```bash
echo "export ROS_DOMAIN_ID=5" >> ~/.bashrc
source ~/.bashrc
```

Rerun your executable and try again.

4. Verification

Warning!!!!!
- Put down the Turtlebot3 from the table. 
- Make sure Turtlebot3 have ample space to move around.
- Do not hold WASD button as Turtlebot3 will accelerate really fast! 

5. Run your teleoperation module. Control the Physical Turtlebot3 using WASD keys and watch the Turtlebot3 move!

## Troubleshooting

1. When running the turtlebot simulation, it may fail to start because an instance of the Gazebo server is still running in the background (usually left over from a previous run that did not shut down cleanly).

Solution: An instance of the gazebo server is still running somewhere. We need to kill it
```bash
killall -e gzserver
```

