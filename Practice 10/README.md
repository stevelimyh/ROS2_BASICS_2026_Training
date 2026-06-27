# Introduction to ROS 2 Launch Files

In this practical, you will learn how to create and use ROS 2 launch files to manage the execution of multiple nodes in a robotics system. Specifically, you will create a ROS 2 package that contains a launch file capable of starting all the nodes developed in Practical 9 with a single command. This will demonstrate how launch files simplify workflow by reducing the need for multiple terminals and manual startup steps. By the end of this exercise, you will understand how to organize and automate node execution efficiently using ROS 2’s Python-based launch system.

## Learning Outcomes

By the end of this practical, learners will be able to:

- Understand the purpose and structure of ROS 2 launch files written in Python
- Create and configure launch files to start one or more ROS 2 nodes simultaneously
- Use launch arguments and parameters to control node behavior at runtime
- Organize complex systems by grouping and managing multiple nodes through a single launch interface
- Apply best practices for launch file development and reusability


## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 workspace and ROS 2 packages.

1. **Practice 10A: Creating ROS2 Launch File**

   - [10A.1: Creating a ROS2 launch File](#10a1-creating-a-ros2-launch-file)
   - [10A.2: Verifying your ROS2 Launch File](#10a2-verifying-your-ros2-launch-file)

## 10A.1: Creating a ROS2 launch File

1. Create 2 ROS2 Packages

```bash
	cd ~/training/new_workspace/src/
	ros2 pkg create --build-type ament_python package1 --node-name node1 
	ros2 pkg create --build-type ament_python package2 --node-name node2 
```

Copy this script to `node1`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node1Publisher(Node):
    def __init__(self):
        super().__init__('node1_publisher')
        self.publisher = self.create_publisher(String, '/my_string', 10)
        self.timer = self.create_timer(1.0, self.publish_message)  # publish every 1 second
        self.count = 0
        self.get_logger().info('node1_publisher has started and is publishing to /my_string')

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from Node1! Count: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Node1Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

Copy this script to `node2.py`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node2Publisher(Node):
    def __init__(self):
        super().__init__('node2_publisher')
        self.publisher = self.create_publisher(String, '/my_string', 10)
        self.timer = self.create_timer(1.0, self.publish_message)  # publish every 1 second
        self.count = 0
        self.get_logger().info('node2_publisher has started and is publishing to /my_string')

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from Node2! Count: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Node2Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

Now you have just created 2 packages `package1` and `package2` with `node1` and `node2` respectively.

2. Now go to my_python_package and create a launch directory 

```bash
	cd ~/training/new_workspace/src/my_python_package
	mkdir launch
```

3. create a file named `two_nodes.launch.py`

```bash
	touch two_nodes.launch.py
```

4. Copy over the script below. Save the file and exit

```python 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='package1',
            executable='node1',
            name='node1_name'
        ),
        Node(
            package='package2',
            executable='node2',
            name='node1_name'
        ),
    ])
```

Save the file and exit.

5. Go to `my_python_package's setup.py and copy the code below

```python
from setuptools import find_packages, setup
import os

package_name = 'my_python_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/two_nodes.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='maintainer',
    maintainer_email='maintainer email',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'my_node_executable = my_python_package.my_node:main'
        ],
    },
)
```

6. Go to `new_workspace` workspace directory, and build your new packages. Do not forget to source your workspace!

```bash
	cd ~/training/new_workspace
	colcon build
	source install/setup.bash
```

7. Launch `node1` and `node2` simultaneously using a single command in one terminal!

```bash
	ros2 launch my_python_package two_nodes.launch.py
```

## 10A.2: Verifying your ROS2 Launch File

1. Check if all nodes are running

```bash
	ros2 node list
```

## 10B.1: Creating ROS2 Launch file for camera_service and object_spawner

1. Create a launch folder in the `object_spawner` package

2. Create a launch file, `demo.launch.py` in the `launch` folder

    You may use the provided boiler plate code below as a starting point for your code. This file contains:
    1. All libraries to be imported for the launch file

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import yaml
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


"""
This load_yaml function returns a .yaml file content, given the ROS2 Package name and
relative filepath to that package.
"""

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, "r") as file:
            return yaml.safe_load(file)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None

def generate_launch_description():

    launch_description = LaunchDescription()

    """
    TODO: Add a `Node` for the aruco detection node to the `launch_description`
		- Package Name: Refer to Pratical 8B
		- Executable Name: Refer to Pratical 8B
		- Node Name: `"aruco_detection_node"`
		- Ouput: log

        use the launch_description.add_action(node_variable) to add this node to the LaunchDescription object
    """
    aruco_detection = Node(
        package="camera_service",
        executable="aruco_detection_node",
        name="aruco_detection_node",
        output="log"
    )
    # Using this example, create the rest of the laumch node yourself. 

    launch_description.add_action(aruco_detection)

    """
   TODO: Add a `Node` for the object spawner node to the `launch_description`
		- Package Name: Refer to Practical 9A
		- Executable Name: Refer to Practical 9A
		- Node Name: `"object_spawner_node"`
		- Ouput: log

        use the launch_description.add_action(node_variable) to add this node to the LaunchDescription object
    """

    """
    TODO:   We want the rviz configuration from pratical 9. In order to do that we the link to share the directory 
            of the object to do that 

            - We need to create a variable `rviz_config_dir ` using the `os.path.join` and `get_package_share_directory ('package_name'),'folder name' , 'your_rviz_config_file' ` functions.
    """

    """
    TODO: Add a `Node` for the rviz2 node to the `launch_description`
    
		- Package Name: `"rviz2"`
		- Executable Name: `"rviz2"`
		- Node Name: `"rviz2_node"`
		- Ouput: log
		- Arguments: `rviz_config_dir`

        use the launch_description.add_action(node_variable) to add this node to the LaunchDescription object
    """

    return launch_description
```

3. Copy over the `practical_9.rviz` file to the same `launch` folder.
	- The RViz file is a configuration file that allows you to launch pre-defined settings. This means you dont need to add the Marker 	Plugin to the RViz GUI from `practical 9` everytime to run the demo

4. Populate the launch file with the following 

	- Add a `Node` for the aruco detection node to the `launch_description`
		- Package Name: Refer to Practical 8B
		- Executable Name: Refer to Practical 8B
		- Node Name: `"aruco_detection_node"`
		- Ouput: log

	- Add a `Node` for the object spawner node to the `launch_description`
		- Package Name: Refer to Practical 9A
		- Executable Name: Refer to Practical 9A
		- Node Name: `"object_spawner_node"`
		- Ouput: log


	- Create a variable `rviz_config_dir ` using the `os.path.join` and `get_package_share_directory` functions

	- A Add a `Node` for the rviz2 node to the `launch_description`
    
		- Package Name: `"rviz2"`
		- Executable Name: `"rviz2"`
		- Node Name: `"rviz2_node"`
		- Ouput: log
		- Arguments: `rviz_config_dir`


5. Edit your `setup.py` file to install the launch and rviz files 
	- Remember to add the following libraries into the `setup.py` file
	```python
	import os
	from glob import glob
	from setuptools import setup, find_packages
	```
	- As a hint, you will be able to install the `practical_9.rviz` file by adding this line in the `data_files` array in your `setup.py` file
	```python
		(os.path.join('share', package_name,'launch'), glob('launch/*.rviz'))
	```
	- Do the same for the launch file in the `launch` folder.

## 10A.2: Verifying your ROS2 Launch File

Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

To check if your solution works, run the following 

### 1. Run the camera driver on the turtlebot3

Before running the camera driver, ensure that you have **CONNECTED TO THE SAME NETWORK AS YOUR TURTLEBOT AND EXPORTED THE `ROS_DOMAIN_ID` IN YOUR ENVIRONMENT**

```bash
ssh ubuntu@<ip_address>

ros2 launch usb_cam demo_launch.py

```

### 2. Run your demo

In another terminal within your VM, ensure that you have **SOURCED YOUR ROS DISTRO AND YOUR WORKSPACE AND EXPORTED THE `ROS_DOMAIN_ID` IN YOUR ENVIRONMENT**, then run the following command:

```bash
ros2 launch object_spawner demo.launch.py

```
With this one launch file, you should launch everything that you created in `Practical 8` and `Practical 9`
