import rclpy
from rclpy.node import Node
from .submodules.motorController import motorController # Class with motor control functions
from geometry_msgs.msg import Twist


class cmd_convert(Node):

    def __init__(self):
        super().__init__('cmd_convert')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.mc = motorController()

    def listener_callback(self, msg): # test fxn for joy_node
        if(msg.linear.x != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.get_logger().info(f"Recieved: {self.mc.run(channels,msg.linear.x) / 4}")
            
        if(msg.linear.y != 0): # only send a command when vel is not 0
            channels = [0,1,2,3,4,5,6,7] # dummy channel list
            self.mc.run(channels,msg.linear.y)
        if(msg.linear.z != 0): # only send a command when vel is not 0
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