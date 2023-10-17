import rclpy
from rclpy.node import Node
from motorController import motorController

from sensor_msgs.msg import Joy

class JoyListener(Node):

    def __init__(self):
        super().__init__('joyListener')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        if(msg.buttons[0] != 0):
            motorController.testFunc()

def main(args=None):
    rclpy.init(args=args)

    jl = JoyListener()
    rclpy.spin(jl)



if __name__ == '__main__':
    main()
