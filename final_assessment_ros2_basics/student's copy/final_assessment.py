import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseArray, Pose
from perception_msgs.srv import GetObjectLocation
import numpy as np
import time

class TurtleBotAruco(Node):
    def __init__(self):
        super().__init__('final_assessment')
        # Recommended values, change if you want!
        self.distance_threshold = 0.5
        self.max_linear_velocity = 0.1
        self.max_angular_velocity = 1.0

    def check_tag(self):
        #-----------------------------------------------------------------------
        #                    TODO:
        #  Create a function check the tag poses, and move the robot accordingly
        #------------------------------------------------------------------------
    
    def get_tag_pose(self):
        #------------------------------------------------
        #                    TODO:
        #  Create a function to get the pose of the tag 
        #------------------------------------------------

    def move_turtlebot(self, linear_velocity, angular_velocity):
        #------------------------------------------------
        #                    TODO:
        #  Create a function to move the robot
        #------------------------------------------------

    def get_tag_distance(self, x, y):
        return math.sqrt((x ** 2) + (y ** 2))

    def get_tag_angle(self, x, y):
        return np.arctan(y/x)

def main(args=None):
    rclpy.init(args=args)
    turtlebot_move = TurtleBotAruco()
    while(rclpy.ok()):
        turtlebot_move.check_tag()
    turtlebot_move.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
