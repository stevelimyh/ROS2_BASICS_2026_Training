import rclpy
from rclpy.node import Node
#------------------------------------------------
#                    TODO:
#  Import your SimpleVelocity here
#------------------------------------------------


from geometry_msgs.msg import Twist


class MyPublisher(Node):


    def __init__(self):
        super().__init__('MyPublisher')

        #------------------------------------------------
        #                    TODO:
        #  Create your publisher below! Remember that your
        #  publishes StringVelocity type message to a topic called
        #  simple_vel
        #------------------------------------------------

        #------------------------------------------------
        #                    TODO:
        #  Create your subscriber below! Remember that your
        #  subscribes to twist type message from the topic
        #  simple_vel
        #------------------------------------------------


        #------------------------------------------------
        #                    TODO:
        #  Once you have completed creating your publisher,
        #  Initialise a twist message and call it self.msg
        #------------------------------------------------



        #------------------------------------------------
        #                    TODO:
        # Create your timer below and it should be set at
        # 1 seocnds
        #------------------------------------------------



        
    def listener_callback(self, msg):
        self.msg = msg

    def timer_callback(self):
        msg = SimpleVelocity()
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

    my_publisher = MyPublisher()

    rclpy.spin(my_publisher)

    my_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()