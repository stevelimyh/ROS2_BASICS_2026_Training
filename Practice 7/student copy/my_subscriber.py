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
