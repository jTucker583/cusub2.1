# Submodule Nesting

Often times we see that we need to include modules that we have created to make our ros nodes work correctly. The example in this package is the maestro class we created, along with imported modules to make that class work correctly. Simply importing the module you created is not enough in the context of a ROS2 package. In order to ensure that the module you import into your ROS node works correctly, perform the following steps:

1. In the `setup.py` file, add a path to the packages list to the folder containing the module you wish to import:

   ```
    package_name = 'teleoperation'
    submodules = 'teleoperation/submodules'
    maestro = 'teleoperation/submodules/Maestro'
    setup(
        name=package_name,
        version='0.0.0',
        packages=[package_name, submodules, maestro],
    ...
   ```

2. In each of the python files referencing a user defined module, add a `.` in front of the folder name:

   ```
    import rclpy
    from rclpy.node import Node
    from .submodules import motorController # user defined module
   ```

3. Make sure that each of the folders with a submodule you use has an `__init__.py` file inside.

4. Rebuild and source the package, and run like normal.

More information can be found [here](https://answers.ros.org/question/367793/including-a-python-module-in-a-ros2-package/).
