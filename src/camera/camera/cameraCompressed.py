import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage  # Import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class Camera(Node):
    def __init__(self, cameraport, topic):
        super().__init__('CameraPublisher')
        self.publisher = self.create_publisher(CompressedImage, topic, 10)  # Use CompressedImage instead of Image
        self.bridge = CvBridge()
        self.cam_feed = cv2.VideoCapture(cameraport)

    def compress_and_publish_image(self, topic='image_compressed'):
        ret, img = self.cam_feed.read()
        
        # Resize the image
        img_resized = cv2.resize(img, (640, 480))  # Adjust the size as needed

        # Convert the OpenCV image to a ROS message
        try:
            image_msg = self.bridge.cv2_to_compressed_imgmsg(img_resized, dst_format='jpeg')  # Use JPEG compression
        except CvBridgeError as e:
            rclpy.logerr(e)
            return -1

        # Publish the compressed ROS image message
        self.publisher.publish(image_msg)

def main(args=None):
    rclpy.init(args=args)
    image = Camera(cameraport=0, topic='image_compressed')
    while True:
        if image.compress_and_publish_image() == -1:
            break
        if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
            image.destroy_node()
            rclpy.shutdown()
            break

if __name__ == '__main__':
    main()
