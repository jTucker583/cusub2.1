"""
    AUTHOR: JAKE TUCKER
    CONTACT: jakob.tucker@colorado.edu
    PURPOSE: Get and publish data from our DVL to ROS
"""

# package requries additional setup, see documentation from https://github.com/waterlinked/dvl-python/tree/master/serial

import rclpy
from rclpy.node import Node
# from wldvl import WlDVL
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import serial
import math
import asyncio
from .dvl_tcp_parser import _DVLMessage
import time
import json
import threading

class DVL(Node):

    def __init__(self):
        super().__init__('DVLPublisher')
        self.rawvelpub = self.create_publisher(String, 'dvl_vel_data', 10)
        self.rawrecpub = self.create_publisher(String, 'dvl_deadrec_data', 10)
        self.twistpub = self.create_publisher(Twist, 'measured_vel', 10)
        self.posepub = self.create_publisher(Pose, 'pose', 10)
        self.timer_ = self.create_timer(0.2, self.publish_data)  # Call data_callback every 0.2 seconds (dead reckoning report update cycle is 5hz)
        self.deadrecmsg = _DVLMessage()
        self.velmsg = _DVLMessage()
        self.posemsg = Pose()
        self.twistmsg = Twist()
        self.rthread = None
        self.vthread = None
    def publish_data(self):
        self.get_logger().info(f"Publishing data")
        self.getDeadreckoningData()
        self.getVelocityData()
        self.publish_raw_deadrec()
        self.publish_raw_velocity()

    def convert_to_twist(self, data):
        if (data is None):
            return
        parsed_data = json.loads(data)
        self.twistmsg._linear._x = parsed_data['vx']
        self.twistmsg._linear._y = parsed_data['vy']
        self.twistmsg._linear._z = parsed_data['vz']

    def publish_raw_deadrec(self):
        tmp = String()
        if self.deadrecmsg.readMessage() is None:
            tmp.data = "No data"
        else:
            tmp.data = self.deadrecmsg.readMessage().to_string()
        self.rawrecpub.publish(tmp)
    def publish_raw_velocity(self):
        tmp = String()
        if self.velmsg.readMessage() is None:
            tmp.data = "No data"
        else:
            tmp.data = self.velmsg.readMessage().to
        self.rawvelpub.publish(tmp)

    def publish_twist(self):
        if (self.twistmsg is not None):
            self.twistpub.publish(self.twistmsg)

    def convert_to_pose(self, data):
        if (data is None):
             return
        parsed_data = json.loads(data)
        self.posemsg.position.x = parsed_data['x']
        self.posemsg.position.y = parsed_data['y']
        self.posemsg.position.z = parsed_data['z']
        angdata = self.euler_to_quaternion(parsed_data['roll'],parsed_data['pitch'],parsed_data['yaw'])
        self.posemsg.orientation.x = angdata[0]
        self.posemsg.orientation.y = angdata[1]
        self.posemsg.orientation.z = angdata[2]
        self.posemsg.orientation.w = angdata[3]

        self.get_logger().info(f"Pose data: {self.posemsg}")

    def publish_pose(self):
        if (self.posemsg is not None):
            self.posepub.publish(self.posemsg)

    def stopReadingData(self, dvlmsg):
        dvlmsg.stopReading()

    def getDeadreckoningData(self):
        try:
            if (not self.deadrecmsg.readingdata):
                # self.deadrecmsg.startReading("dead_reckoning")
                self.rthread = threading.Thread(target=self.deadrecmsg.startReading, args=("dead_reckoning"))
            if (self.deadrecmsg.readingdata):
                self.convert_to_pose(self.deadrecmsg.readMessage()) # updates class posemsg
                self.publish_pose() # publishes class posemsg to ROS
        except ConnectionRefusedError:
            self.get_logger().error(f"Error connecting to DVL")
        except KeyboardInterrupt:
            self.get_logger().info(f"Stopping DVL reading")

    def getVelocityData(self):
        try:
            if (not self.velmsg.readingdata):
                self.vthread = threading.Thread(target=self.velmsg.startReading, args=("velocity"))
                # self.velmsg.startReading("velocity")
            if (self.velmsg.readingdata):
                self.convert_to_twist(self.velmsg.readMessage()) # updates class posemsg
                self.publish_twist() # publishes class posemsg to ROS
        except ConnectionRefusedError:
            self.get_logger().error(f"Error connecting to DVL")
        except KeyboardInterrupt:
            self.get_logger().info(f"Stopping DVL reading")

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

