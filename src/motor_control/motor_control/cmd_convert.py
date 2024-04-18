import rclpy
from rclpy.node import Node
from .submodules.motorController import motorController # Class with motor control functions
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool
from sensor_msgs.msg import Joy
from std_msgs.msg import String
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

        # exec('testMC.py') # clear the motors for use
        self.mc = motorController()

    def listener_callback(self, msg): # test fxn for joy_node
        if(msg.linear.x != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.get_logger().info(f"Recieved: {self.mc.run(channels,msg.linear.x) / 4}") # debug
        if(msg.linear.y != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.linear.y)
        if(msg.linear.z != 0): # only send a command when vel is not 0
            # t = 0.1 # measured in seconds
            # self.pose.position.z = msg.linear.z / 2 * t + self.depth
            # self.position_publish.publish(self.pose)
            # pmsg = Bool()
            # pmsg.data = True
            # self.valid_publish.publish(pmsg)
            # self.get_logger().info(f"Depth: {self.pose.position.z}")
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.linear.z)
        if(msg.angular.z != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.angular.z)
    


def main(args=None):
    rclpy.init(args=args)

    convert = cmd_convert()

    rclpy.spin(convert)

    convert.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()