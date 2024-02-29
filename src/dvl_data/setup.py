import os
from glob import glob
from setuptools import setup
# for setuptools, use version 58.2.0 to avoid stderr msg
from setuptools import find_packages

package_name = 'dvl_data'
dvl = 'dvl_data/dvl-python'
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, f"{package_name}.dvl-python.serial.wldvl", f"{package_name}.dvl-python.serial", dvl],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jake tucker',
    maintainer_email='tuckerjake11@gmail.com',
    description='Get and publish data from the DVL to ROS',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dvl_publisher = dvl_data.DVL_subpub:main'
        ],
    },
)
