# Teleoperation
Updated: Nov 13, 2023 by Jake Tucker (jakob.tucker@colorado.edu)
---
**Current state:** We are at a point where when running a joystick node, we subscribe to that joystick node and convert the values to PWM
values that can be sent to a singular motor. We need to:
- Map forward/backward motion to our forward/backward motors (pending motor configuration once the sub is built).
- Map side-to-side motion to our side-to-side motors.
- Map forward-backward pwm commands to forward-backward motors depending on the twist command
- Map depth motion to depth motors
- Wrap it all up in a bow so that you can roslaunch the teleop operations
  - Launch ros2 teleop node `ros2 launch teleop_twist_joy teleop-launch.py`
  - Run joyListener.py

### How does the teleoperation package work?
This package has the following dependencies:
- pyserial
- maestro (how do we get maestro?)
- pytime
- rclpy
- sensor_msgs.msg
- ROS2 [teleop_twist_joy_package](https://index.ros.org/r/teleop_twist_joy/)
