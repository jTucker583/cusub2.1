"""
    AUTHOR: XAVIER OKEEFE
    CONTACT: xaok7569@colorado.edu
    PURPOSE: Test code to test motor controller
"""
from submodules.motorController import motorController
from submodules.Maestro import maestro
import time

# All of this servo code is needed to clear maes

# Code for controlling motors
channels = {10} # Channels to command
mc = motorController()
mc.run(channels,1100,1) # run motors at set speed for set time (seconds)
