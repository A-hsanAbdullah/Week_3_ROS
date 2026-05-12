#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TrianglePattern(Node):
    def __init__(self):
        super().__init__('triangle_pattern')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()
        self.get_logger().info('Moving in a Triangle...')

    def timer_callback(self):
        msg = Twist()
        t = time.time() - self.start_time
        t_mod = t % 3.0
        
        if t_mod < 2.0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 2.094  # 120 degrees
            
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrianglePattern()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
