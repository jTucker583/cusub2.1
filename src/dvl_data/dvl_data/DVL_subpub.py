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
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import serial
import math
import asyncio
from dvl_tcp_parser import _DVLMessage
import time
import json

class DVL(Node):

    def __init__(self):
        super().__init__('DVLPublisher')
        self.publisher_ = self.create_publisher(String, 'dvl_data', 10)
        self.twistpub = self.create_publisher(Twist, 'measured_vel', 10)
        self.posepub = self.create_publisher(Pose, 'pose', 10)
        self.timer_ = self.create_timer(0.2, self.og_data_callback)  # Call data_callback every 0.2 seconds (dead reckoning report update cycle is 5hz)
        self.dvlmsg = _DVLMessage()
        self.posemsg = Pose()

        while (self.dvlmsg._start_dvl_socket("dead_reckoning") == ConnectionRefusedError):
            self.get_logger().error("Error connecting to DVL")
            time.sleep(1)
        self.posemsg = self.convert_to_pose(self.dvlmsg.readMessage())
        self.dvlmsg.stopReading()
        self.get_logger().info(f"Initial Pose: {self.posemsg}")
        self.posepub.publish(self.posemsg)

        self.getDeadreckoningData()

    def convert_to_pose(self, data):
        parsed_data = json.loads(data)
        self.posemsg.position.x = parsed_data['x']
        self.posemsg.position.y = parsed_data['y']
        self.posemsg.position.z = parsed_data['z']
        angdata = self.euler_to_quaternion(parsed_data['roll'],parsed_data['pitch'],parsed_data['yaw'])
        self.posemsg.orientation.x = angdata[0]
        self.posemsg.orientation.y = angdata[1]
        self.posemsg.orientation.z = angdata[2]
        self.posemsg.orientation.w = angdata[3]

    def publish_pose(self):
        self.posepub.publish(self.posemsg)

    @asyncio.coroutine
    def getDeadreckoningData(self):
        try:
            self.dvlmsg.startReading("dead_reckoning")
        except ConnectionRefusedError:
            self.get_logger().error("Error connecting to DVL")
            return ConnectionRefusedError
        while not ConnectionError:
            self.pose = self.convert_to_pose(self.dvlmsg.readMessage())
            self.publish_pose()
            yield from asyncio.sleep(0.2)
    
    # @asyncio.coroutine
    # def getVelocityData(self):
    #     try:
    #         self.dvlmsg.startReading("velocity")
    #     except ConnectionRefusedError:
    #         self.get_logger().error("Error connecting to DVL")
    #         return ConnectionRefusedError
    #     while not ConnectionError:
    #         try:
    #             data = self.dvlmsg.readMessage()
    #         except ConnectionRefusedError:
    #             self.get_logger().error("Error connecting to DVL")
    #             return ConnectionRefusedError
    #         self.twistpub.publish(data)
    #         yield from asyncio.sleep(0.2)

    def euler_to_quaternion(self, roll, pitch, yaw):
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        qw = cr * cp * cy + sr * sp * sy
        qx = sr * cp * cy - cr * sp * sy
        qy = cr * sp * cy + sr * cp * sy
        qz = cr * cp * sy - sr * sp * cy

        return qw, qx, qy, qz

def main(args=None):
    rclpy.init(args=args)

    dvl_publish = DVL()

    rclpy.spin(dvl_publish)
    dvl_publish.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

