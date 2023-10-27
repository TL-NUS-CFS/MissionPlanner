import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from std_msgs.msg import String
from .land import land_command
import time

class MissionPlanner(Node):

    def __init__(self):
        super().__init__('mission_planner')
        #maybe do a subscription creation loop for drone in drones[]
        self.undetectedTags = {"tag36h11:64"}
        self.subscription = self.create_subscription(
            TFMessage,
            'cf13/tf',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "something' )
        # check if drone is up down
            #ignore
        # check if message empty
            #ignore
        # check if target is captured
            #ignore
            #run takeoff.py
        if msg.transforms:
            detectedTag = msg.transforms[0].child_frame_id
            self.get_logger().info('I saw: "%s"' % detectedTag)
            if detectedTag in self.undetectedTags:
                self.get_logger().info('"%s" is in undetected tags' & detectedTag)
                time.sleep(1)
                self.get_logger().info('LANDING')
                land_command()
                
                self.undetectedTags.remove(detectedTag)
                
        return



        


def main(args=None):
    rclpy.init(args=args)

    mission_planner = MissionPlanner()

    rclpy.spin(mission_planner)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    mission_planner.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()