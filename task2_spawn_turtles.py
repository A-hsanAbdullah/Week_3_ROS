#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import time

class SpawnAndMoveTurtles(Node):
    def __init__(self):
        super().__init__('spawn_and_move_turtles')
        
        # Service client to spawn turtles
        self.spawn_cli = self.create_client(Spawn, 'spawn')
        while not self.spawn_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
            
        # Spawn turtle2 and turtle3
        self.spawn_turtle(5.0, 5.0, 0.0, 'turtle2')
        self.spawn_turtle(2.0, 8.0, 0.0, 'turtle3')
        
        # Publishers for all three turtles
        self.pub1 = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        
        self.timer = self.create_timer(0.5, self.timer_callback)

    def spawn_turtle(self, x, y, theta, name):
        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        req.name = name
        future = self.spawn_cli.call_async(req)
        # We won't block on the future to keep it simple

    def timer_callback(self):
        # Turtle 1: Circle
        msg1 = Twist()
        msg1.linear.x = 2.0
        msg1.angular.z = 1.0
        self.pub1.publish(msg1)
        
        # Turtle 2: Straight line
        msg2 = Twist()
        msg2.linear.x = 1.5
        msg2.angular.z = 0.0
        self.pub2.publish(msg2)
        
        # Turtle 3: Spin in place
        msg3 = Twist()
        msg3.linear.x = 0.0
        msg3.angular.z = 3.0
        self.pub3.publish(msg3)

def main(args=None):
    rclpy.init(args=args)
    node = SpawnAndMoveTurtles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
