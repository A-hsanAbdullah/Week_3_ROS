#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        
        self.current_pose = Pose()
        self.goal_x = 8.0  # Target X
        self.goal_y = 8.0  # Target Y
        self.tolerance = 0.1
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info(f'Moving to Goal: ({self.goal_x}, {self.goal_y})')

    def pose_callback(self, msg):
        self.current_pose = msg

    def timer_callback(self):
        msg = Twist()
        
        distance = math.sqrt((self.goal_x - self.current_pose.x)**2 + (self.goal_y - self.current_pose.y)**2)
        
        if distance >= self.tolerance:
            # Proportional control for linear velocity
            msg.linear.x = 1.5 * distance
            
            # Proportional control for angular velocity
            angle_to_goal = math.atan2(self.goal_y - self.current_pose.y, self.goal_x - self.current_pose.x)
            
            # Normalize angle difference
            angle_diff = angle_to_goal - self.current_pose.theta
            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi
                
            msg.angular.z = 4.0 * angle_diff
        else:
            # Stop the turtle
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Goal Reached!')
            
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
