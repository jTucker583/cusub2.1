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
from .submodules.motorController import motorController

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
        self.joy_sub = self.create_subscription(
            Joy, # msg type
            '/joy', # topic to listen to
            self.listener_callback, #callback fxn
            10 # overflow queue
        )
        self.cmd_sub = self.create_subscription(
            Twist, # msg type
            '/sys_cmd_vel', # topic to listen to
            self.sys_cmd_vel_callback, #callback fxn
            10 # overflow queue
        )
        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)
        self.joy_sub
        self.cmd_sub
        self.jlinear_x = 0
        self.jlinear_y = 0
        self.jlinear_z = 0
        self.jangular_z = 0
        self.slinear_x = 0
        self.slinear_y = 0
        self.slinear_z = 0
        self.sangular_z = 0
        self.publish_cmd()
        self.mc = motorController()
        self.fmc_pressed = False
        self.fmc_val = 1
        self.light_pressed = False
        self.light_on = False
        

    # def listener_callback(self, msg): # test fxn for joy_node
    #     mc = motorController()
    #     if(msg.axes[1] != 0): # trigger button
    #         channels = [0,1,2,3,4,5,6,7] # dummy channel list
    #         mc.run(channels,msg.axes[1])
    def listener_callback(self, msg):
        # Need to adjust values
        # implement logic to dermine max values to send
        x = msg.axes[1] # forward/backward
        y = msg.axes[0] # side to side
        z = msg.axes[5] * MAXVEL_Z # depth control (need point implementation)
        az = msg.axes[2] # yah
        
        # proportion logic
        sum_ax = abs(x) + abs(y) + abs(az)
        if sum_ax < 1: sum_ax = 1
        self.jlinear_x = x / sum_ax * MAXVEL_X * self.fmc_val # forward/backward
        self.jlinear_y = y / sum_ax * MAXVEL_Y * self.fmc_val # side to side
        self.jlinear_z = z * self.fmc_val # depth control (need point implementation)
        self.jangular_z = az / sum_ax * MAXVEL_AZ # yaw
        
        self.get_logger().info(f"{self.convert_to_PWM(msg.axes[3])}")
        self.mc.run([9],self.convert_to_PWM(msg.axes[3]), raw_pwm=True)
        if (not int(msg.buttons[0])):
            self.mc.run([8],1200, 1, raw_pwm=True)
        else:
            self.mc.run([8],1800, 1, raw_pwm=True)
        if(int(msg.buttons[1]) and not self.fmc_pressed):
            self.toggle_fmc()
        if(int(msg.buttons[2]) and not self.light_pressed):
            self.light_on = not self.light_on
            if self.light_on:
                self.get_logger().info(f"Light ON")
            else:
                self.get_logger().info(f"Light OFF")
            
        self.fmc_pressed = bool(msg.buttons[1])
        self.light_pressed = bool(msg.buttons[2])
        
        self.publish_cmd()
        self.send_light_pwm()

    def toggle_fmc(self):
        if (self.fmc_val == 1):
            self.get_logger().info(f"Fine Motor Control ON")
            self.fmc_val = 0.66
        else:
            self.get_logger().info(f"Fine Motor Control OFF")
            self.fmc_val = 1
    
    def send_light_pwm(self):
        if (self.light_on):
            self.mc.run([10],1900)
        else:
            self.mc.run([10],1100)
    
    def convert_to_PWM(self, axis):
        return round(1500 + 500 * axis)

    def sys_cmd_vel_callback(self, msg):
        self.slinear_x = msg.linear.x
        self.slinear_y = msg.linear.y
        self.slinear_z = msg.linear.z
        self.sangular_z = msg.angular.z
        self.publish_cmd()

    def publish_cmd(self):
        # Create Twist message
        twist_msg = Twist()
        
        # Publish jlinear data if available, otherwise use slinear data
        if self.jlinear_x is not None and self.jlinear_x != 0:
            twist_msg.linear.x = float(self.jlinear_x)
        else:
            twist_msg.linear.x = float(self.slinear_x)
            
        if self.jlinear_y is not None and self.jlinear_y != 0:
            twist_msg.linear.y = float(self.jlinear_y)
        else:
            twist_msg.linear.y = float(self.slinear_y)
            
        if self.jlinear_z is not None and self.jlinear_z != 0:
            twist_msg.linear.z = float(self.jlinear_z)
        else:
            twist_msg.linear.z = float(self.slinear_z)
            
        if self.jangular_z is not None and self.jangular_z != 0:
            twist_msg.angular.z = float(self.jangular_z)
        else:
            twist_msg.angular.z = float(self.sangular_z)
            
        self.publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)

    jl = JoyListener()
    rclpy.spin(jl)



if __name__ == '__main__':
    main()
