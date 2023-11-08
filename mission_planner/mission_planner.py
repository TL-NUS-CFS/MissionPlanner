import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from std_msgs.msg import String
from .land import land_command

class MissionPlanner(Node):

    def __init__(self):
        super().__init__('mission_planner')
        #maybe do a subscription creation loop for drone in drones[]
        #self.declare_parameter("undetectedTags", ["tag36h11:52","tag36h11:203"]) 
        #self.undetectedTags = set(self.get_parameter("undetectedTags"))
        self.undetectedTags = {"tag36h11:200","tag36h11:204"}
        self.subscription = self.create_subscription(
            TFMessage,
            'cf13/tf',
            self.listener_callback,
            10)
        self.subscription2 = self.create_subscription(
            TFMessage,
            'cf15/tf',
            self.listener_callback2,
            10)
        self.subscription  # prevent unused variable warning
        self.subscription2  # prevent unused variable warning

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
            #self.get_logger().info('CF13 saw')
            detectedTag = msg.transforms[0].child_frame_id
            self.get_logger().info('CF13 saw: "%s"' % detectedTag)
            if detectedTag in self.undetectedTags:
                self.get_logger().info('Target "%s" has been detected' % detectedTag)    
                self.get_logger().info('Landing Crazyflie 13 on "%s"' % detectedTag)
                self.undetectedTags.remove(detectedTag)
                land_command(0x13)
                #land
        return
    def listener_callback2(self, msg):
        #self.get_logger().info('I heard: "something' )
        # check if drone is up down
            #ignore
        # check if message empty
            #ignore
        # check if target is captured
            #ignore
            #run takeoff.py
        if msg.transforms:
            #self.get_logger().info('CF15 saw')
            detectedTag = msg.transforms[0].child_frame_id
            self.get_logger().info('CF15 saw: "%s"' % detectedTag)
            if detectedTag in self.undetectedTags:
                self.get_logger().info('Target "%s" has been detected' % detectedTag)    
                self.get_logger().info('Landing Crazyflie 15 on "%s"' % detectedTag)       
                self.undetectedTags.remove(detectedTag)
                land_command(0x14)
                #land
        return



        


def main(args=None):
    rclpy.init(args=args)

    mission_planner = MissionPlanner()

    rclpy.spin(mission_planner)




if __name__ == '__main__':
    main()