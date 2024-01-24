# Package Takeaways

1. When creating a python package, all code for the node goes in the package folder (next to "**init**.py")
2. `setup.py` must be configured to find the node file and the launch script:
   - Inside the console scripts list, add the following: `ros_excecutable = package_name.node_name:entry_function(usually main)`
   - Inside the data_files list, add the following: `(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))`. This is a path to the launch file
3. launch files go within the launch directory and should include the package name and ros excecutable in `setup.py`. Launch files should also be named with the following convention: `abbreviated_package_name_launch.xml`
4. Launching the package is as follows:

```
ros2 launch package_name name_launch.xml
```
