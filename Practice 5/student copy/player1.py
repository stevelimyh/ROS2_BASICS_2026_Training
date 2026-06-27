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

