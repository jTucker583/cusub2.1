from custom_interfaces.srv import DetectObjects

import rclpy
from rclpy.node import Node

class CameraTest(Node):

    def __init__(self):
        super().__init__("CameraTest")
        self.cli = self.create_client(DetectObjects, "detect_objects")
        while not self.cli.wait_for_service(timeout_sec=1):
            self.get_logger().info("Waiting for camera service...")

        self.req = DetectObjects.Request()

    def send_request(self):
        return self.cli.call_async(self.req)
    

def main():
    rclpy.init()
    camera_test = CameraTest()
    future = camera_test.send_request()
    rclpy.spin_until_future_complete(camera_test, future)
    res = future.result()

    # Log the result
    if res is not None:
        camera_test.get_logger().info(str(res))
    else:
        camera_test.get_logger().info("Failed to get response from service")

    camera_test.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
