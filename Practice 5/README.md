# Practice 5: Creating a ROS 2 Node which contains a Publisher and Subscriber

In this exercise, you will implement two ROS 2 nodes: Player1 and Player2, that communicate with each other in a simple ping-pong style message exchange.

Through this communication pattern, you will also gain a deeper understanding of ROS 2 Quality of Service (QoS) settings and the importance of compatibility between publishers and subscribers.

- `player1` initiates the ping-pong game by publishing an `integer` to the `/ping_pong` topic.
- `player2` subscribes to the `/ping_pong` topic, receives the integer, increments it, and publishes it back on the same topic.
- `player1` receives the incremented integer, increments it again, and publishes it back to `/ping_pong`.
- This back-and-forth exchange continues indefinitely between `player1` and `player2`.
- The interaction stops only when either or both nodes are shut down by the user.

The video below shows an example execution of `player1` (top-left panel) and `player2` (top-right panel) nodes. The bottom panel shows the messages published to topic `/ping_pong`

<img src="./Image/ping_pong.gif"  width="100%" height="100%">  
<br> 

## Mandatory Exercises:

1. **Practice 5A: Creating Ping-Pong ROS2 Package and Player1 and Player2**

   - [5A.1: Creating a Ping-Pong ROS2 Package](#5a1-creating-a-ping-pong-ros2-package)
   - [5A.2: Creating Player1 Node](#5a2-creating-player1-node)
   - [5A.3: Creating a Player2 Node](#5a3-creating-player2-node)
   - [5A.4: Verifying Player1 and Player2 Output](#5a4-verifying-player1-and-player2-output)

2. **Practice 5B: ROS2 Quality of Service**

   - [5B.1: Transient Locale and Volatile](#5b1-transient-locale-and-volatile)


## Learning Outcomes 
By completing this practice, you will be able to:

- Understand how ROS 2 publishers and subscribers interact in a multi-node system.
- Implement two separate nodes (Player 1 and Player 2) that exchange messages in a ping-pong communication pattern.
- Set up a ROS 2 packagea containing multiple nodes working together.
- Apply message handling, callbacks, and topic-based communication in a practical context.
- Apply Quality-of-Service (QoS) Implementation on ROS2 Publishers and Subscribers

## 5A.1: Creating a Ping-Pong ROS2 Package

1. Create ROS 2 package named `ping_pong_pkg` with node `player1` in `ros2_ws` workspace
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python pingpong_pkg --node-name player1
```

## 5A.2: Creating Player1 Node

2. Edit the `player1.py`

```bash
code ~/ros2_ws/src/pingpong_pkg/pingpong_pkg/player1.py
```
3. You may use the provided code boiler plate below as a starting point for `player1`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from rclpy.duration import Duration

class Player1(Node):

    def __init__(self):
        super().__init__('player1')
        #------------------------------------------------
        #                    TODO:
        # 5.) Create Player1 Publisher of type Int64 to /ping_pong topic
        # 6.) Create Player1 Subscription to /ping_pong of type Int64 to /ping_pong topic
        #------------------------------------------------
        self.count = 1 
        self.get_logger().info('Player1 Ready!')

    def player2_callback(self, player2_msg):
        if player2_msg.data <= self.count: # discard message for player2
            return
        self.get_clock().sleep_for(Duration(seconds=1.0)) # Periodic sleep to slowdown exchange 

        #------------------------------------------------
        #                    TODO:
        # 7.) Store received data to self.count 
        # 8.) Increment self.count
        # 9.) Log Player 1 Publishing <count>
        # 10.) Publish the self.count value!
        #------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    player1_node = Player1()
    #------------------------------------------------
    #                    TODO:
    # 1.) Create a ROS2 message Int64 Object
    # 2.) Store Player1 count into In64 Message
    # 3.) Log Player 1 Publishing 
    #------------------------------------------------
    starting_msg = Int64()
    player1_node.get_logger().info('Player 1 Publishing %d' % starting_msg.data)
    #------------------------------------------------
    #                    TODO:
    # 4.) Publish to the ROS2 message to /ping_pong
    #------------------------------------------------
    player1_node.ping_publisher.publish(starting_msg)
    rclpy.spin(player1_node)
    player1_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

4. Implement the missing code blocks! Use the comment blocks to guide you through the implementation.

5. Build your program and source your workspace! (Note: Pleasre ensure that you are in the right directory!)

6. Run your `player1` Node

7. You should be able to see the following output from your terminal.

```bash
johnaa@johnaa-aftershock:~/ros2_ws$ ros2 run pingpong_pkg player1 
[INFO] [1751865959.482251892] [player1]: Player1 Ready!
[INFO] [1751865959.482399100] [player1]: Player 1 Publishing 1
```

8. Since your player1 node is waiting for a higher integer than it previously published to appear on the /ping_pong topic, you need to publish an integer greater than 1 to resume the communication.

```bash
ros2 topic pub /ping_pong std_msgs/msg/Int64 "{data: 2}" --once
```
**Explanation**

- `ros2 topic pub` : This is the ROS 2 command to publish a message to a topic.
- `/ping_pong` : This is the name of the topic to which the message will be published.
- `std_msgs/msg/Int64` : This specifies the message type.
- `"{data: 1}"` : This is the actual message being sent. It sets the data field of the Int64 message to 1.
- `--once` :
This flag tells the command to publish the message only once and then exit (instead of continuously publishing).

## 5A.3: Creating Player2 Node

1. Create and edit script the `player2.py`

```bash
touch ~/ros2_ws/src/pingpong_pkg/pingpong_pkg/player2.py
code ~/ros2_ws/src/pingpong_pkg/pingpong_pkg/player2.py
```
2. Copy the code below into `player2.py` python script

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from rclpy.duration import Duration

class Player2(Node):

    def __init__(self):
        super().__init__('player2')
        #------------------------------------------------
        #                    TODO:
        # 1.) Create Player2 Publisher of type Int64 to /ping_pong topic
        # 2.) Create Player2 Subscription to /ping_pong of type Int64 to /ping_pong topic
        #------------------------------------------------
        self.count = 0 
        self.get_logger().info('Player2 Ready!')

    def player1_callback(self, player1_msg):
        if player1_msg.data <= self.count: # discard message for player1
            return
        self.get_clock().sleep_for(Duration(seconds=1.0))
        #------------------------------------------------
        #                    TODO:
        # 3.) Store received data to self.count 
        # 4.) Increment self.count
        # 5.) Log Player 2 Publishing <count>
        # 6.) Publish the self.count value!
        #------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    player2_node = Player2()
    rclpy.spin(player2_node)
    player2_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

3. Implement the missing code blocks! Use the comment blocks to guide you through the implementation.

4. Make sure your executables are defined in the entry_points section of your `setup.py`

```python
    entry_points={
        'console_scripts': [
            'player1 = pingpong_pkg.player1:main',
            'player2 = pingpong_pkg.player2:main'
        ],
    },
```

5. Build your program and source your workspace! (Note: Pleasre ensure that you are in the right directory!)

6. Run your `player2` Node

7. You should be able to see the following output from your terminal.
```linux
johnaa@johnaa-aftershock:~/ros2_ws$ ros2 run pingpong_pkg player2 
[INFO] [1751867004.088245454] [player2]: Player2 Ready!
```

## 5A.4: Verifying Player1 and Player2 Output

1. Expected way how to run the program (in order).

- Run the `player2` node executable 
- Run the `player1` node executable
- Listen to topic /ping_pong (optional)
- Both nodes will run indefinitely

The picture below shows an example execution of `player1` (top-left panel) and `player2` (top-right panel) nodes

<img src="./Image/ping_pong.png"  width="100%" height="100%">  
<br> 


**Questions**

- Why should `player2` be started before `player1`?
- What happens if the `player1` node is launched first instead?

## 5B.1: Transient Locale and Volatile

In ROS 2, Quality of Service (QoS) settings control how messages are delivered between publishers and subscribers. Two durability policies are:
- `Volatile` (default):
    Messages are only sent to currently active subscribers. If a subscriber joins after the message is published, it will not receive the previously sent message.
    This is the default behavior in ROS 2.
- `Transient Local` : The publisher retains the last message and delivers it to any future subscribers when they connect. Useful when you want late-joining nodes to receive the most recent state or command.

In **Practice 5A**, your nodes used the default **Volatile** QoS. In **5B** you will modify them to use **Transient Local** QoS, and observe how the start order stops mattering:

- **Volatile QoS (5A):** run `player2` first, then `player1`. If `player1` starts first, `player2` may miss the first message.
- **Transient Local QoS (5B):** run `player1` first, then `player2`. `player2` should still receive the last published message even though it joined later.


1. Edit both `player1` and `player2` python script
- For `player1` script.
```python
### Rest of the Code...
from rclpy.qos import QoSProfile, QoSDurabilityPolicy

class Player1(Node):

    def __init__(self):
        super().__init__('player1')
        qos_profile = QoSProfile(
            depth=10,
            durability=QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL
        )
        self.ping_publisher = self.create_publisher(Int64, '/ping_pong', qos_profile)
        self.pong_subscription = self.create_subscription(Int64, '/ping_pong', self.player2_callback, qos_profile)
        self.count = 1 
        self.get_logger().info('Player1 Ready!')

        ### Rest of the Code...
```

- For `player2` script.
```python
### Rest of the Code...
from rclpy.qos import QoSProfile, QoSDurabilityPolicy

class Player2(Node):

    def __init__(self):
        super().__init__('player2')
        qos_profile = QoSProfile(
            depth=10,
            durability=QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL
        )
        self.pong_publisher = self.create_publisher(Int64, '/ping_pong', qos_profile)
        self.ping_subscription = self.create_subscription(Int64, '/ping_pong', self.player1_callback, qos_profile)
        self.count = 0 
        self.get_logger().info('Player2 Ready!')

        ### Rest of the Code...
```

1. Expected way how to run the program (in order).

- Run the `player1` node executable 
- Run the `player2` node executable
- Both nodes will run indefinitely