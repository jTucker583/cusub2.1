"""
    AUTHOR: XAVIER O'KEEFE
    CONTACT: xaok7569@colorado.edu
    PURPOSE: Create subscriber for teleoperation
"""
import rclpy
from rclpy.node import Node
# from .submodules import motorController # Class with motor control functions
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import yaml

MAXVEL_X = 0
MAXVEL_Y = 0
MAXVEL_Z = 0
MAXVEL_AZ = 0
with open('src/cfg/sub_properties.yaml') as f:
    file = yaml.safe_load(f)
    MAXVEL_X = file['max_vel_x']
    MAXVEL_Y = file['max_vel_y']
    MAXVEL_Z = file['max_vel_z']
    MAXVEL_AZ = file['max_vel_az']


class JoyListener(Node):

    def __init__(self):
        super().__init__('joyListener')
        self.subscription = self.create_subscription(
            Joy, # msg type
            '/joy', # topic to listen to
            self.listener_callback, #callback fxn
            10 # overflow queue
        )
        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)
        self.subscription

    # def listener_callback(self, msg): # test fxn for joy_node
    #     mc = motorController()
    #     if(msg.axes[1] != 0): # trigger button
    #         channels = [0,1,2,3,4,5,6,7] # dummy channel list
    #         mc.run(channels,msg.axes[1])
    def listener_callback(self, msg):
        # Need to adjust values
        linear_x = msg.axes[1]  # forward/backward
        linear_y = msg.axes[0]  # side to side
        linear_z = msg.axes[5]  # depth control (need point implementation)
        angular_z = msg.axes[2]  # yah

        # Create Twist message
        twist_msg = Twist()
        twist_msg.linear.x = linear_x * MAXVEL_X
        twist_msg.linear.y = linear_y * MAXVEL_Y
        twist_msg.linear.z = linear_z * MAXVEL_Z
        twist_msg.angular.z = angular_z * MAXVEL_AZ

        # Publish Twist message
        self.publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)

    jl = JoyListener()
    rclpy.spin(jl)



if __name__ == '__main__':
    main()
