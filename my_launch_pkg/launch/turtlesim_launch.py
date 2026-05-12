from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Main Simulator
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # Teleop for Keyboard control
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop'
        ),
        # Spawn a second turtle via a service call (Alternative: separate node)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim2',
            parameters=[{'background_r': 150}] # Visual difference
        )
    ])
