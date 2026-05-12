import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # STABILITY ADJUSTMENT: Increase front threshold [cite: 74, 142]
        # Reacting earlier (0.8m instead of 0.3m) prevents collisions due to inertia.
        self.front_threshold = 0.5  
        self.side_threshold = 0.3
        

    def scan_callback(self, msg):
        # Handle invalid values for stability [cite: 56-57]
        ranges = np.array(msg.ranges)
        ranges[np.isinf(ranges)] = 3.5
        ranges[np.isnan(ranges)] = 3.5

        # Define regions 
        front_region = np.concatenate((ranges[0:30], ranges[330:359])) # Wider front view
        left_region = ranges[70:110]
        right_region = ranges[250:290]

        # Compute minimum distance [cite: 34, 89-92]
        front_dist = np.min(front_region)
        left_dist = np.min(left_region)
        right_dist = np.min(right_region)

        twist = Twist()

        # Decision-making logic [cite: 94, 40-42]
        if front_dist < self.front_threshold:
            # STOP AND TURN BEHAVIOR [cite: 35-38, 42]
            self.get_logger().info(f"Obstacle! Distance: {front_dist:.2f}m. Turning...")
            twist.linear.x = 0.0 # Full stop to prevent flipping [cite: 38]
            
            # Turn toward side with larger clearance [cite: 42, 101]
            if left_dist > right_dist:
                twist.angular.z = 0.4 # Moderate angular speed [cite: 55]
            else:
                twist.angular.z = -0.4
        else:
            # STABILIZED FORWARD MOTION [cite: 53-54, 111]
            # Suggested speed is 0.1-0.2 m/s 
            twist.linear.x = 0.1
            twist.angular.z = 0.0

        self.publisher.publish(twist) # [cite: 115]

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator() # [cite: 119]
    try:
        rclpy.spin(node) # [cite: 120]
    except KeyboardInterrupt:
        pass
    node.destroy_node() # [cite: 121]
    rclpy.shutdown() # [cite: 122]

if __name__ == '__main__':
    main()
