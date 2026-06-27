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
