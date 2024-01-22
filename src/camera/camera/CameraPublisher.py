import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class Camera(Node):
    def __init__(self, cameraport, topic):
        super().__init__('CameraPublisher')
        self.publisher = self.create_publisher(Image, topic,10)
        self.bridge = CvBridge()
        self.cam_feed = cv2.VideoCapture(cameraport) # needs to be called every time the function is run, or else error

    def publish_image(self, topic='image'):
        ret, img = self.cam_feed.read()
        # Initialize the OpenCV bridge for converting between OpenCV images and ROS messages
        # Convert the OpenCV image to a ROS message
        try:
            image_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
        except CvBridgeError as e:
            rclpy.logerr(e)
            return -1
        
        # Publish the ROS image message
        self.publisher.publish(image_msg)
        # cv2.imshow("publisher",img)
    
def main(args=None):
    rclpy.init(args=args)
    image = Camera(cameraport=0, topic='image')
    while True:
        if image.publish_image() == -1: break
        if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
            image.destroy_node()
            rclpy.shutdown()
            break
        
        
if __name__ == '__main__':
    main()