import rclpy
from rclpy.node import Node

class ObjectSpawnerNode(Node):
    def __init__(self):
        super().__init__('object_spawner_node')

        #------------------------------------------------
        #                    TODO:
        #  Create your Service Client here! Remember to check
        #  what is the Client type you need.
        #------------------------------------------------


    def send_request(self):

    #------------------------------------------------
    #                    TODO:

    #  Populate the send_request function.This is where you should craft your 
    #  request and read the response to be passed to the publish_markers function
    #  In the publish_markers fuction do the following

    # Set the pose of the marker

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3

    # Set the scale of the marker

    # Set the color


    #------------------------------------------------

def main():
    rclpy.init()
    node = ObjectSpawnerNode()
    while rclpy.ok():
        node.send_request()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
