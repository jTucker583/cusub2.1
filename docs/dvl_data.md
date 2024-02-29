# dvl_data 
Updated: Feb 28, 2024
---
**Current state:** Package should theoretically pull data from the DVL and publish it as a string. We may want to change the message type so it is easier to work with, and we need to change the port the DVL accesses, which can be done in `../src/dvl_data/dvl_data/DVL_subpub.py`.

### How does the dvl_data package work?
This package has the following dependencies:
- pyserial
- rclpy
- sensor_msgs.msg
- crcmod
- WLDVL [dvl-python](https://github.com/waterlinked/dvl-python)
    - Configuration of this package is as follows:
        1. Run `pip install crcmod pyserial`
        2. Navigate to `..dvl_data/dvl-python/serial`
        3. Run `pip install -e .`

This package should publish data to the `/DVL_Data` topic. This data should be subscribed to in order to create a depth control pid loop, and a point control package.


