import rclpy
from chimera_camera.srv import DetectObjects
from ultralytics import YOLO
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2
import numpy as np

CAMERA_PORT = 0

class Camera(Node):
    def __init__(self):
        super().__init__('CameraPublisher')

        self.model = YOLO("../models/yolo11m.pt")

        #Sets up the service with the custom type in ../srv/DetectObjects.srv
        self.srv = self.create_service(DetectObjects, 'detect_objects', self.detect_objects) 
        
        #Initiate the CvBride to convert openCv images into Ros images
        self.bridge = CvBridge()

        #Opens up the camera port to be read from
        self.cam_feed = cv2.VideoCapture(CAMERA_PORT) 

        #If camera does not open shut down the node because it is useless
        if not self.cam_feed.isOpened():
            self.get_logger.error("Failed to open camera")
            rclpy.shutdown()

        #OpenCV keeps a buffer of frames, for our purposes we only need the most recent frame
        self.cam_feed.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    def detect_objects(self, request, response):

        ret, frame = self.cam_feed.read()
        if not ret:
            self.get_logger.error("Could not read camera")
            return response
    
        cv2.imshow("test", frame)


        #Test output
        response.object_names = ["cat", "dog", "mouse"]
        response.object_positions_x = [100.0, 200.0, 132.0]
        response.object_positions_y = [150.0, 250.0, 120.0]
        response.confidence = [90.0, 95.0, 17.6]

        return response
    
    def __del__(self):
        if self.cam_feed.isOpened():
            self.cam_feed.release()

    
def main(args=None):
    rclpy.init(args=args)
    image = Camera()
    rclpy.spin(image)

    rclpy.shutdown()
        
if __name__ == '__main__':
    main()

