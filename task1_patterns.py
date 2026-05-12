#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class PatternPublisher(Node):
    def __init__(self):
        super().__init__('pattern_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.state = 0
        self.start_time = time.time()
        self.get_logger().info('Starting Circular Pattern...')

    def timer_callback(self):
        msg = Twist()
        current_time = time.time()
        elapsed = current_time - self.start_time

        if self.state == 0:
            # Circular pattern for 6 seconds
            msg.linear.x = 2.0
            msg.angular.z = 2.0
            if elapsed > 6.0:
                self.state = 1
                self.start_time = time.time()
                self.get_logger().info('Starting Triangular Pattern...')
        elif self.state == 1:
            # Triangular pattern (draw an equilateral triangle roughly)
            cycle_time = elapsed % 3.0
            if cycle_time < 2.0:
                # Move straight
                msg.linear.x = 2.0
                msg.angular.z = 0.0
            else:
                # Turn ~120 degrees (2.09 radians)
                msg.linear.x = 0.0
                msg.angular.z = 2.09
            
            if elapsed > 12.0:
                self.state = 2
                self.get_logger().info('Pattern Complete.')
                msg.linear.x = 0.0
                msg.angular.z = 0.0
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PatternPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
