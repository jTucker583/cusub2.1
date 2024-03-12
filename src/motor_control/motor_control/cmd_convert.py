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
        self.valid_goal = False
        self.pose = Pose()
        self.depth = -0.1

        self.cmd_vel_sub = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.joy_sub = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10
        )
        self.dvl_sub = self.create_subscription(
            String,
            'dvl_data',
            self.depth_callback,
            10
        )
        self.goal_sub = self.create_subscription(
            Pose,
            'pose_goal',
            self.pose_callback,
            10
        )

        self.position_publish = self.create_publisher(
            Pose,
            'goal_pose',
            10
        )
        self.valid_publish = self.create_publisher(
            Bool,
            'pose_goal_valid',
            10
        )

        # exec('testMC.py') # clear the motors for use
        self.mc = motorController()

    def listener_callback(self, msg): # test fxn for joy_node
        if (self.valid_goal == False):
            pmsg = Bool()
            pmsg.data = False
            self.valid_publish.publish(pmsg)
        if(msg.linear.x != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.get_logger().info(f"Recieved: {self.mc.run(channels,msg.linear.x) / 4}") # debug
        if(msg.linear.y != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.linear.y)
        if(msg.linear.z != 0): # only send a command when vel is not 0
            t = 0.1 # measured in seconds
            self.pose.position.z = msg.linear.z / 2 * t + self.depth
            self.position_publish.publish(self.pose)
            pmsg = Bool()
            pmsg.data = True
            self.valid_publish.publish(pmsg)
            self.get_logger().info(f"Depth: {self.pose.position.z}")
        if(msg.angular.z != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.angular.z)

    def depth_callback(self, msg):
        """
        TODO: Set the depth variable to the depth data from the DVL
        """

    def joy_callback(self, msg):
        if(msg.axes[0] > 0 or msg.axes[1] > 0 or msg.axes[2] > 0):
            self.valid_goal = False
    def pose_callback(self, msg):
        self.pose = msg
    


def main(args=None):
    rclpy.init(args=args)

    convert = cmd_convert()

    rclpy.spin(convert)

    convert.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()