import rclpy
from rclpy.node import Node

import math

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

class pid_controller(Node):

    def __init__(self):
        super().__init__('pid_controller')
        self.publisher_ = self.create_publisher(Twist, 'sys_cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.goalpose = self.create_subscription(Pose, 'goal_pose', self.controller_callback, 10)
        self.currentpose = self.create_subscription(Pose, 'pose', self.current_pose_callback, 10)
        self.goal = Pose()
        self.currentPosition = Pose()
        self.Kp = 1
        self.limit = 50
        self.i = 0

    def controller_callback(self, msgPose):
        self.goal = msgPose

    def current_pose_callback(self, msg):
        self.currentPosition = msg

    def at_goal(self):
        return (self.goal.position.x == self.currentPosition.position.x and 
                self.goal.position.y == self.currentPosition.position.y and
                self.goal.position.z == self.currentPosition.position.z)
    
    def pidLoop(self):
        msg = Twist()
        while(not self.at_goal):
            diff = self.getDistance
            if(diff > self.limit):
                diff = self.limit

            if(self.currentPosition.position.x < self.goal.position.x):
                msg.linear.x = self.Kp * diff
            else:
                msg.linear.x = -self.Kp * diff
            if(self.currentPosition.position.y < self.goal.position.y):
                msg.linear.y = self.Kp * diff
            else:
                msg.linear.y = -self.Kp * diff
            if(self.currentPosition.position.z < self.goal.position.z):
                msg.linear.z = self.Kp * diff 
            else:
                msg.linear.z = -self.Kp * diff
            

            self.publisher_.publish(msg)

    def getDistance(self):
        return math.sqrt((self.goal.position.x - self.currentPosition.position.x)**2 +
                         (self.goal.position.y - self.currentPosition.position.y)**2 +
                         (self.goal.position.y - self.currentPosition.position.y)**2)
    
                    


def main(args=None):
    rclpy.init(args=args)

    pid = pid_controller()

    rclpy.spin(pid)
    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
