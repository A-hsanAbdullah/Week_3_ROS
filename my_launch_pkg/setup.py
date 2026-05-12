import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_launch_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # This line ensures your launch files are copied to the install directory
        (os.path.join('share', package_name, 'launch'), 
         glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahsan Abdullah',
    maintainer_email='ahsan@example.com',
    description='Lab 4 Introduction to ROS 2 Launch and Rosbag',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # If you create a Python script for the Follow-the-Leader task, 
            # you would add it here, for example:
            # 'follower = my_launch_pkg.follower_node:main',
        ],
    },
)     
