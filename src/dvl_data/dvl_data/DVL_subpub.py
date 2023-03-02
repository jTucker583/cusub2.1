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
import math

baud_rate = 115200
serial_port = '/dev/ttyUSB0'
class DVL(Node):

    def __init__(self):
        super().__init__('DVLPublisher')
        self.publisher_ = self.create_publisher(String, 'dvl_data', 10)
        self.twistpub = self.create_publisher(Twist, 'measured_vel', 10)
        self.posepub = self.create_publisher(Pose, 'pose', 10)
        self.timer_ = self.create_timer(0.2, self.data_callback)  # Call data_callback every 0.2 seconds (dead reckoning report update cycle is 5hz)
        try:
            # self.dvl = WlDVL(serial_port)
            self.ser = serial.Serial(serial_port, baud_rate, timeout=1)
        except:
            self.dvl = None
    # def data_callback(self):
    #     msg = String()
    #     if self.dvl is not None:
    #         data = self.dvl.read()
    #         expected_keys = {'time', 'vx', 'vy', 'vz', 'fom', 'altitude', 'valid'}
    #         if (data is Not None and all(key in data for key in expected_keys)):
    #             msg.data = str(data)
    #             if (msg.data is not None):
    #                 self.publisher_.publish(msg)\
    #     else:
    #         msg.data = 'Error conencting to DVL'

    def data_callback(self):
        twist_msg = Twist()
        pose_msg = Pose()
        vel_data = sendCmd('wrz').split(',') # velocity report
        pose_data = sendCmd('wrp').split(',') # dead reckoning report
        
        qw, qx, qy, qz = euler_to_quaternion(pose_data[5],pose_data[6],pose_data[7])
        x, y, z = pose_data[1], pose_data[2], vel_data[4] # vel_data[4] is altitude from bottom

        vx, vy, vz = vel_data[0], vel_data[1], vel_data[2]
        
        twist_msg.linear.x, twist_msg.linear.y, twist_msg.linear.z = vx, vy, vz
        twist_msg.angular.x, twist_msg.angular.y, twist_msg.angular.z = pose_data[5],pose_data[6],pose_data[7] # currenly shows roll, pitch yaw
        pose_msg.position.x, pose_msg.position.y, pose_msg.position.z = x, y, z
        pose_msg.orientation.x, pose_msg.orientation.y, pose_msg.orientation.z, pose_msg.orientation.w = qx, qy, qz, qw

        self.twistpub.publish(twist_msg)
        self.posepub.publish(pose_msg)

    
    def deadreckoning_reset(self):
        if (sendCmd('wcr') == 'wra'):
            self.get_logger().info('Dead Reckoning Reset. pose and goal_pose topics invalidated.')
        else:
            self.get_logger.info("Dead Reckoning failed to Reset.")
    
    def sendCmd(self, command):
        packet = command.encode() + b'\n'
        ser.write(packet)
        response = ser.readline().decode().strip()
        return response


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

