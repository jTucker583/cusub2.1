"""
    AUTHOR: JAKE TUCKER
    CONTACT: jakob.tucker@colorado.edu
    PURPOSE: Convert cmd_vel commands to PWM values 
"""
import serial
import time
import sys
from .submodules.Maestro import maestro
import yaml
import logging

PWM_MULTIPLIER = 0
NEUTRAL_PWM = 1490
with open('src/cfg/sub_properties.yaml') as f:
    file = yaml.safe_load(f)
    PWM_MULTIPLIER = file['PWM_multiplier']
    NEUTRAL_PWM = file['neutral_PWM']
    MAX_PWM = file['max_PWM']
    MIN_PWM = file['min_PWM']
    PORT = file['maestro_port']

class motorController:
    
    def __init__(self):
        # initialize serial port , set baud rate, set timeout
        self.serial = None
        try:
            self.serial = serial.Serial(PORT, 9600, timeout=1) 
        except:
            print("Error opening serial port {port}")
        

    def run(self, channels, target=0, duration=-1, multiplier=PWM_MULTIPLIER, INVERT=False, raw_pwm=False):
        """Sends a PWM command to a set of servos

        Args:
            channels (int[]): list of integer channels from the maestro
            target (int): target PWM value (can be cmd_vel value or raw PWM value)
            duration (int, optional): duration of command. Defaults to -1 (runs once).
            multiplier (float, optional): multiplier for cmd_vel values. Defaults to PWM_MULTIPLIER.
            INVERT (bool, optional): inverts the target value. Defaults to False.
            raw_pwm (bool, optional): if True, target is raw PWM value. Defaults to False.
        """
        INVERTER = 1
        if(INVERT):
            INVERTER = -1
            
        if not raw_pwm:
            targetPWM = round(4 * (NEUTRAL_PWM + INVERTER * (target * multiplier)))
        else:
            targetPWM = round(target * 4)
        logging.info(f'PWM: {targetPWM / 4}')
        
        if (targetPWM > MAX_PWM * 4): targetPWM = MAX_PWM * 4
        elif (targetPWM < MIN_PWM * 4): targetPWM = MIN_PWM * 4
        
        targetBytes = [(targetPWM & 0x7F), ((targetPWM >> 7) & 0x7F)]
        for channel in channels: # loop through channels
            finalCommand = [0x84, channel] + targetBytes # Send 4 byte command to maestro
            if self.serial is not None: self.serial.write(bytearray(finalCommand))
        # if duration != -1: # if duration parameter is passed
        #     time.sleep(duration)
        #     self.killAll(channels)
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



 
