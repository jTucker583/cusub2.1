import rclpy
from rclpy.node import Node
from .submodules.motorController import motorController # Class with motor control functions
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool
from sensor_msgs.msg import Joy
from std_msgs.msg import String
# import testMC # importing this clears the motors for use
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
            channels = [0,1,2,3,4,5,6,7]
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
        duration_in_ns = (self.get_clock().now() - self.last_msg_time).nanoseconds
        duration_in_s = duration_in_ns / 1e9
        if duration_in_s > self.timeout:
            channels = [0, 1, 2, 3, 4, 5, 6, 7]
            self.mc.killAll(channels)
    
    def experimental_callback(self, msg):
        # convert msg to PWM here, and do proportion logic
        INVERTER = -1
        x_channels = [0,1,2,7]
        y_forward_channels = [1,7]
        y_backward_channels = [0,2]
        z_channels = [3,4,5,6]
        az_forward_channels = [2,7]
        az_backward_channels = [0,1]
        
        xmsg = msg.linear.x
        ymsg = msg.linear.y
        zmsg = msg.linear.z
        azmsg = msg.angular.z
        # proportion logic
        sum_axis = sum(xmsg, ymsg, azmsg)
        
        if (sum_axis > 12): # look at sub_properties.yaml
            xmsg = xmsg / sum_axis
            ymsg = ymsg / sum_axis
            azmsg = azmsg / sum_axis
            
        
        x_targetPWM = self.convert_to_PWM(xmsg)
        y_targetPWM = self.convert_to_PWM(ymsg)
        z_targetPWM = self.convert_to_PWM(zmsg)
        az_targetPWM = self.convert_to_PWM(azmsg)
        
        self.mc.run(x_channels, x_targetPWM, raw_pwm=True)
        self.mc.run(y_forward_channels, y_targetPWM, raw_pwm=True)
        self.mc.run(y_backward_channels, y_targetPWM * INVERTER, raw_pwm=True)
        self.mc.run(z_channels, z_targetPWM, raw_pwm=True)
        self.mc.run(az_forward_channels, az_targetPWM, raw_pwm=True)
        self.mc.run(az_backward_channels, az_targetPWM * INVERTER, raw_pwm=True)
        
        
    def convert_to_PWM(self, target, multiplier=30):
        return round(4 * (1490 + (target * multiplier)))


def main(args=None):
    rclpy.init(args=args)

    convert = cmd_convert()

    rclpy.spin(convert)

    convert.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
