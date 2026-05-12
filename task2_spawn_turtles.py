#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import time

class SpawnAndMoveTurtles(Node):
    def __init__(self):
        super().__init__('spawn_and_move_turtles')
        
        self.spawn_cli = self.create_client(Spawn, 'spawn')
        while not self.spawn_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting...')
            
        # Spawn turtle2 at the top right for Rectangle
        self.spawn_turtle(8.0, 7.0, 0.0, 'turtle2')
        # Spawn turtle3 at the bottom for Triangle
        self.spawn_turtle(5.0, 2.0, 0.0, 'turtle3')
        
        self.pub1 = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) # turtle1 starts at 5.5, 5.5 (Circle)
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10) # turtle2 Rectangle
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10) # turtle3 Triangle
        
        self.start_time = time.time()
        self.timer = self.create_timer(0.1, self.timer_callback)

    def spawn_turtle(self, x, y, theta, name):
        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        req.name = name
        self.spawn_cli.call_async(req)

    def timer_callback(self):
        t = time.time() - self.start_time
        
        # Turtle 1: Circle
        msg1 = Twist()
        msg1.linear.x = 1.5
        msg1.angular.z = 1.5
        self.pub1.publish(msg1)
        
        # Turtle 2: Rectangle (cycle = 2.5s -> 1.5s straight, 1s turn)
        msg2 = Twist()
        t2_mod = t % 2.5
        if t2_mod < 1.5:
            msg2.linear.x = 1.5
            msg2.angular.z = 0.0
        else:
            msg2.linear.x = 0.0
            msg2.angular.z = 1.5708 # 90 degrees
        self.pub2.publish(msg2)
        
        # Turtle 3: Triangle (cycle = 3.0s -> 2.0s straight, 1.0s turn)
        msg3 = Twist()
        t3_mod = t % 3.0
        if t3_mod < 2.0:
            msg3.linear.x = 1.5
            msg3.angular.z = 0.0
        else:
            msg3.linear.x = 0.0
            msg3.angular.z = 2.094 # 120 degrees
        self.pub3.publish(msg3)

def main(args=None):
    rclpy.init(args=args)
    node = SpawnAndMoveTurtles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
