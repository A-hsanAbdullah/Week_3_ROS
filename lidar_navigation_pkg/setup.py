from setuptools import find_packages, setup

package_name = 'lidar_navigation_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahsan Abdullah',
    maintainer_email='your_email@example.com',
    description='Reactive Navigation using LiDAR for TurtleBot3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This line is the most important part! [cite: 58, 123-125]
            'lidar_navigator = lidar_navigation_pkg.lidar_navigator:main',
        ],
    },
)
