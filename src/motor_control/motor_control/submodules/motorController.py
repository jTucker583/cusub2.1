"""
    AUTHOR: XAVIER O'KEEFE
    CONTACT: xaok7569@colorado.edu
    PURPOSE: Create class for basic motor control functions
"""
import serial
import time
import sys
from .Maestro import maestro
import yaml

PWM_MULTIPLIER = 0
NEUTRAL_PWM = 0
with open('src/cfg/sub_properties.yaml') as f:
    file = yaml.safe_load(f)
    PWM_MULTIPLIER = file['PWM_multiplier']
    NEUTRAL_PWM = file['neutral_PWM']


class motorController:
    
    def __init__(self):
        # initialize serial port , set baud rate, set timeout
        self.port = '/dev/ttyACM0'
        self.serial = None
        try:
            self.serial = serial.Serial(port, 9600, timeout=1) 
        except:
            print("Error opening serial port {port}")
        

    def run(self, channels, target, duration=-1):
        """Sends a PWM command to a set of servos

        Args:
            channels (int[]): list of integer channels from the maestro
            target (int): target PWM value
            duration (int, optional): duration of command. Defaults to -1 (runs once).
        """
        targetPWM = round(4 * (NEUTRAL_PWM + target * PWM_MULTIPLIER)) # target is cmd_vel
        targetPWM = targetPWM
        targetBytes = [(targetPWM & 0x7F), ((targetPWM >> 7) & 0x7F)]
        for channel in channels: # loop through channels
            finalCommand = [0x84, channel] + targetBytes # Send 4 byte command to maestro
            if self.serial is not None: self.serial.write(bytearray(finalCommand))
        if duration != -1: # if duration parameter is passed
            time.sleep(duration)
            self.killAll(channels)
        return targetPWM

    def killAll(self, channels):
        """Send the neutral PWM command to the list of servos

        Args:
            channels (int[]): list of integer channels from the maestro
        """
        target = 4*NEUTRAL_PWM # neutral target
        targetBytes = [(target & 0x7F), ((target >> 7) & 0x7F)]
        for channel in channels: # kill all channels
            finalCommand = [0x84, channel] + targetBytes
            if self.serial is not None: self.serial.write(bytearray(finalCommand))

    def testFunc(val):
        """Print recieved teleop value

        Args:
            val (float): got from joystick
        """
        finalVal = NEUTRAL_PWM + val*PWM_MULTIPLIER
        print("received val: ", finalVal)



 