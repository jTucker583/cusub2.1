# Documentation for Maestro 
This was a massive pain for us so we've tried to document it.

## What is the Maestro?
The pololu mini maestro is a multi-channel servo controller. This device is able to send PWM signals sperately to each of these channels. There is a GUI for windows which allows you to do this visually, see [this link.](https://www.pololu.com/docs/0J40/3.a)

## How does it work?
There are two things to note about the Maestro:
- The Maestro works in quarter-microseconds, so this is why you see the 4x multiplier on PWM values
- You must manually convert the desired PWM signal to byte-level code. This is why you see shifts and hex values in the code. The documentation for this process can be seen [here.](https://www.pololu.com/docs/0J40/5.c)

