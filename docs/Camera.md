# Camera
Updated: Jan 21, 2024
---
**Current state:** Currently have a working raw camera node, need to fix the compressed image portion, and the launch file.

### How does the camera package work?
This package has the following dependencies:
- rclpy
- numpy
- cv2
- cvbridge
- sensor_msgs.msg

This package basically creates an `/image` topic which can be subscribed to using RVIZ2.