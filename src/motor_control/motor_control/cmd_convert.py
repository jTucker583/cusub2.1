import rclpy
from rclpy.node import Node
from .submodules.motorController import motorController # Class with motor control functions
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool
from sensor_msgs.msg import Joy
from std_msgs.msg import String
import testMC # importing this clears the motors for use
"""
AUTHOR: JAKE TUCKER
EMAIL: jakob.tucker@colorado.edu
PURPOSE: Subscribe to cmd_vel, publish value to motorController to send to servos, as well as find the depth level
"""
class cmd_convert(Node):

    def __init__(self):
        super().__init__('cmd_convert')
        self.cmd_vel_sub = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.last_msg_time = self.get_clock().now()
        self.timeout = 0.01 # 10 ms
        self.timer = self.create_timer(self.timeout, self.check_timeout)
        self.mc = motorController()

    def listener_callback(self, msg): # test fxn for joy_node
        
        if(msg.linear.x > 0): # only send a command when vel is not 0
            channels = [0,1,2,7] # dummy channel list
            self.mc.run(channels,msg.linear.x, INVERT=False)
        elif(msg.linear.x < 0):
            channels = [0,1,2,7] # dummy channel list
            self.mc.run(channels,msg.linear.x, INVERT=True)
        if(msg.linear.y > 0): # only send a command when vel is not 0
            forward_channels = [7,1] # dummy channel list
            backward_channels = [2,0] # dummy channel list
            self.mc.run(forward_channels,msg.linear.y, INVERT=False)
            self.mc.run(backward_channels,msg.linear.y, INVERT=True)
        elif(msg.linear.y < 0): # only send a command when vel is not 0
            forward_channels = [2,0] # dummy channel list
            backward_channels = [7,1] # dummy channel list
            self.mc.run(forward_channels,msg.linear.y, INVERT=False)
            self.mc.run(backward_channels,msg.linear.y, INVERT=True)
        if(msg.linear.x == 0 and msg.linear.y == 0 and msg.angular.z == 0):
            channels = [0,1,2,7]
            self.mc.killAll(channels)
        if(msg.linear.z != 0): # only send a command when vel is not 0
            channels = [3,4,5,6] # dummy channel list
            self.mc.run(channels,msg.linear.z, INVERT=False)
        else:
            channels = [3,4,5,6]
            self.mc.killAll(channels)
        if(msg.angular.z > 0): # spin left?
            forward_channels = [7,2] # dummy channel list
            backward_channels = [0,1] # dummy channel list
            self.mc.run(forward_channels,msg.linear.y, INVERT=False)
            self.mc.run(backward_channels,msg.linear.y, INVERT=True)
        elif(msg.angular.z < 0): # spin right?
            forward_channels = [0,1] # dummy channel list
            backward_channels = [7,2] # dummy channel list
            self.mc.run(forward_channels,msg.linear.y, INVERT=False)
            self.mc.run(backward_channels,msg.linear.y, INVERT=True)
    
    def check_timeout(self):
        if (self.get_clock().now() - self.last_msg_time).seconds > self.timeout:
            channels = [0, 1, 2, 3, 4, 5, 6, 7]
            self.mc.killAll(channels)
    


def main(args=None):
    rclpy.init(args=args)

    convert = cmd_convert()

    rclpy.spin(convert)

    convert.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()