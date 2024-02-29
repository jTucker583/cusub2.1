"""
    AUTHOR: JAKE TUCKER
    CONTACT: jakob.tucker@colorado.edu
    PURPOSE: Get and publish data from our DVL to ROS
"""

# package requries additional setup, see documentation from https://github.com/waterlinked/dvl-python/tree/master/serial

import rclpy
from rclpy.node import Node
from wldvl import WlDVL
from std_msgs.msg import String

class DVL(Node):

    def __init__(self):
        super().__init__('DVLPublisher')
        self.publisher_ = self.create_publisher(String, 'DVL_Data', 10)
        self.timer_ = self.create_timer(0.1, self.data_callback)  # Call data_callback every 0.1 seconds
        try:
            self.dvl = WlDVL("port to DVL")
        except:
            self.dvl = None
    def data_callback(self):
        msg = String()
        if self.dvl is not None:
            msg.data = dvl.read()
        else:
            msg.data = 'Error conencting to DVL'
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    dvl_publish = DVL()

    rclpy.spin(dvl_publish)
    dvl_publish.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
