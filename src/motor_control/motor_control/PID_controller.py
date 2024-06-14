#PID Loop: only uses P and D term. I think integral term is not needed because, unlike cars and stuff, stopping the motors will cause
# the sub to glide and not instantly stop which should reduce the problem of the sub getting infinitely close to the goal. I think it works but it is untested
# and could have dumb errors. Kp and Kd values will need to be tuned.

import rclpy
from rclpy.node import Node

import math
import time

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
        self.Kd = 0.1
        self.deadzone = 1

    def controller_callback(self, msgPose):
        self.goal = msgPose

    def current_pose_callback(self, msg):
        self.currentPosition = msg
 
    def pidLoop(self):
        prevDimDiff = [
            self.goal.position.x - self.currentPosition.position.x,
            self.goal.position.y - self.currentPosition.position.y,
            self.goal.position.z - self.currentPosition.position.z
        ]

        prevTime = time.time()
        msg = Twist()
        diff = self.getDistance()
        prevDiff = diff

        while(True):

            diff = self.getDistance()
            if(diff < self.deadzone): break
            
            xDiff = self.goal.position.x - self.currentPosition.position.x
            yDiff = self.goal.position.y - self.currentPosition.position.y
            zDiff = self.goal.position.z - self.currentPosition.position.z
            # The derivative term reduces the output based on how fast we are getting to the goal which should reduce overshoot.
            xDerivative = (xDiff - prevDimDiff[0])/(time.time() - prevTime) 
            yDerivative = (yDiff - prevDimDiff[1])/(time.time() - prevTime)
            zDerivative = (zDiff - prevDimDiff[2])/(time.time() - prevTime)

            prevTime = time.time()

            xOutPut = (self.Kp * xDiff) + (self.Kd * xDerivative) 
            yOutPut = (self.Kp * yDiff) + (self.Kd * yDerivative) 
            zOutPut = (self.Kp * zDiff) + (self.Kd * zDerivative) 

            if(xDiff < 0): xOutPut *= -1
            if(yDiff < 0): yOutPut *= -1
            if(zDiff < 0): zOutPut *= -1 

            msg.linear.x = xOutPut
            msg.linear.y = yOutPut
            msg.linear.z = zOutPut


            msg.linear.x = 0
            msg.linear.y = 0

            prevDimDiff[0] = xDiff
            prevDimDiff[1] = yDiff
            prevDimDiff[2] = zDiff

            prevDiff = diff
        
            self.publisher_.publish(msg)

            time.sleep(0.25) # this could be completely uneeded but IDK if we want to limit the rate of commands send.

    def getDistance(self):
        return math.sqrt((self.goal.position.x - self.currentPosition.position.x)**2 +
                         (self.goal.position.y - self.currentPosition.position.y)**2 +
                         (self.goal.position.z - self.currentPosition.position.z)**2)
    
                    


def main(args=None):
    rclpy.init(args=args)

    pid = pid_controller()

    rclpy.spin(pid)
    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
