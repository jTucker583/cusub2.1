# Documentation for Maestro 
This was a massive pain for us so we've tried to document it. Code can be seen in `/cusub2_teleop/motorController.py`

## What is the Maestro?
The pololu mini maestro is a multi-channel servo controller. This device is able to send PWM signals sperately to each of these channels. There is a GUI for windows which allows you to do this visually, see [this link.](https://www.pololu.com/docs/0J40/3.a)

## How does it work?
There are two things to note about the Maestro:
- The Maestro works in quarter-microseconds, so this is why you see the 4x multiplier on PWM values
- You must manually convert the desired PWM signal to byte-level code. This is why you see shifts and hex values in the code. The documentation for this process can be seen [here.](https://www.pololu.com/docs/0J40/5.c)

## How to update/maintain
The function that sends commands to the Maestro is `motorController.run(self, channels, target, duration=-1)`. This function takes in an array of channels (or just one) and sends a given command to these channel(s). 
### To be implemented:
We plan to map each command from the joystick (right/left, forward/back) to a certain motor group. The goal is to use a map that returns an array of channels for each desired command passed to it. This array of channels will then be passed into the run function.

