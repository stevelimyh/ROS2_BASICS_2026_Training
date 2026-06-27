# Practice 4: Create your own ROS 2 Subscriber Node 

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 Subscribers.

1. **Practice 4A: Creating a Simple ROS2 Subscriber**

   - [4A.1: Creating a Simple Subscriber](#4a1-creating-a-simple-subscriber)

1. **Practice 4B: Application of ROS2 Subscribers with Turtlebot3**

   - [4B.1: Viewing Camera Feed from Turtlebot3](#4b1-viewing-camera-feed-from-turtlebot3)
   - [4B.2: Verification of Turtlebot3 Image Viewer Module](#4b2-verification-of-image-viewer-module)
   

## Learning Outcomes

- Understand the purpose and function of ROS 2 Subscribers.
- Create a subscriber node that listens to a topic and processes incoming messages.
- Subscribe to image data published on /image_raw and visualize it using ROS tools.
- Apply subscriber concepts in real-world applications such as viewing the TurtleBot3 camera feed.

## 4A.1: Creating a Simple Subscriber

A Subscriber is a component that listens to data being published on a specific topic. It allows your node to receive and react to messages sent by other nodes in the system.

1. Open the my_node.py file you created in the previous exercise using Visual Studio Code by running the following command in your terminal:

```bash
code ~/training/new_workspace/src/my_python_package/my_python_package/my_node.py
```
2. Copy the Python script below into `my_node.py`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySubscriberNode(Node):
    def __init__(self):
        super().__init__('my_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            '/my_string',
            self.listener_callback,
            10
        )
        self.get_logger().info('my_subscriber_node has started and is listening to /my_string')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = MySubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
**Explanation**

- `from std_msgs.msg import String` : Imports the ROS 2 String message type from the std_msgs package, used for receiving text messages.
- `self.subscription = self.create_subscription(...)` : Creates a subscriber that listens to the /`my_string` topic with message type `String` and a queue size of 10.
- `self.listener_callback` : This is the function that will be called whenever a message is received on the topic.
- def `listener_callback(self, msg)` : Defines the callback function that is triggered when a message is received.
- `self.get_logger().info(f'Received: "{msg.data}"')` : Logs the content of the received message to the terminal.


3. Build the `my_python_package`

```bash
cd ~/training/new_workspace
colcon build --packages-select my_python_package
```
4. Run the executable. (Note: Do not forget to source your workspace!)

```bash
ros2 run my_python_package my_node_executable
```
Your subscriber node is now active and listening for messages published on the /my_string topic.

You may notice that the /my_string topic does not show up right away when you run:

```bash
ros2 topic list
```
In ROS 2, a topic only becomes visible if at least one publisher is actively publishing to it. If your subscriber is running but no publisher is currently sending messages to /my_string, the topic won’t appear in the list.

5. Let's publish a string message to the /my_string topic to verify that our subscriber is working correctly.

Run the following command in a new terminal:

```bash
    ros2 topic pub /my_string std_msgs/msg/String "data: 'Test message from CLI'"
```

You should be able to see the following output in the terminal where your subscriber is running:

```bash
    johnaa@johnaa-aftershock:~/training/new_workspace$ ros2 run my_python_package my_node_executable
	[INFO] [1751810623.115706542] [my_subscriber_node]: my_subscriber_node has started and is listening to /my_string
	[INFO] [1751810645.995015156] [my_subscriber_node]: Received: "Test message from CLI"
	[INFO] [1751810646.996243451] [my_subscriber_node]: Received: "Test message from CLI"
	[INFO] [1751810647.995969241] [my_subscriber_node]: Received: "Test message from CLI"
```

## 4B.1: Viewing Camera Feed from Turtlebot3

1. Within the same `ros2_ws` created in Practice 3, go into the src folder

2. Create a ROS 2 package named `image_viewer` within the `src` folder

3. Create a ROS 2 executable within this package named `view_image`

	- You may use the provided code boiler plate below:

```python
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ViewImage(Node):
    def __init__(self):
        super().__init__('image_processing_node')
        self.bridge = CvBridge()
        self.image_window = cv2.namedWindow("Camera Output")

        #------------------------------------------------
        #                    TODO:
        #  Create your subscriber here! Remember to check
        #  what is the type of message you are receiving.
        #  It should subscribe to the /image_raw topic and use
        #  your callback function below to process each incoming image.
        #  Tip: the last argument is the QoS - pass a queue size like 10,
        #  or the imported qos_profile_sensor_data (better for camera streams).
        #------------------------------------------------

    #-------------------------------------------------
    #                    TODO:
    #          Create a callback for your subscriber!
    #-------------------------------------------------

    def view_image(self, img_msg):
        cv_image = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding='bgr8')
        cv2.imshow("image", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ViewImage()
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

4. Finish the Implementation!

In this exercise, you are provided with a partially completed ROS 2 node that will allow you to view images from a USB webcam.

Your task is to complete the missing parts of the code by creating a subscriber that listens to the /image_raw topic and processes the incoming image messages. These messages are of type sensor_msgs/msg/Image.

5. To Display your image, you may use the following helper function:

```python
def view_image(img_msg)
    cv_image = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding='passthrough')
    cv2.imshow("image", cv_image)
    cv2.waitKey(1)
```
6. Build your `image_viewer` package:

```bash
cd ~/ros2_ws
colcon build --packages-select image_viewer
```

Do not forget to source your workspace!

```bash
source install/setup.bash
```

7. Run your `view_image` executable

```bash 
ros2 run image_viewer view_image
```

## 4B.2: Verification of Image Viewer Module

1. Open a new terminal to bringup and initialise the Turtlebot3. the IP address is specific to TurtleBot3.

Ensure that `ROS_DOMAIN_ID` of your terminal matches the Turtlebot3's `ROS_DOMAIN_ID`!

```bash
ssh ubuntu@<ip_address>
cd camera_ws
source install/setup.bash
ros2 launch camera_calibration_pkg camera_calibration.launch.py
```

**Insert output of turtlebot3 here

2. Run your image viewer node

Then run the following command for the image viewer node:

```bash
ros2 run image_viewer view_image
```

You should be able to see the image feed from turtlebot3!
