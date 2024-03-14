import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class pid_controller(Node):

    def __init__(self):
        super().__init__('pid_controller')
        self.publisher_ = self.create_publisher(Twist, 'sys_cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 69.420
        msg.linear.y = 420.69
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    pid = pid_controller()

    rclpy.spin(pid)
    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()