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
            'cf14/tf',
            self.listener_callback2,
            10)
        # self.subscription3 = self.create_subscription(
        #     TFMessage,
        #     'cf15/tf',
        #     self.listener_callback3,
        #     10)
        self.subscription  # prevent unused variable warning
        self.subscription2  # prevent unused variable warning
        # self.subscription3




        # drones = ["cf37","cf38","cf39"]
        # self.subscriptions = [] 
        # self.callbacks = {}


        # # Create a subscription for each drone
        # for drone in drones:
        #     current_subscription = self.create_subscription(
        #         TFMessage,
        #         drone + '/tf',
        #         self.callbacks[drone],
        #         10)
        #     self.subscriptions.append(current_subscription)
        #     current_subscription


        # # Create a dictionary of callback functions wrt drones
        # for drone in drones:
        #     # Extract the number from the drone's name and use it to construct the function name
        #     callback_name = 'listener_callback' + drone[2:]
        #     self.callbacks[drone] = getattr(self, callback_name)

        #     def create_callback(drone):
        #         def listener_callback(self, msg):
        #             if msg.transforms:
        #                 detectedTag = msg.transforms[0].child_frame_id
        #                 self.get_logger().info( f'{drone} saw: "%s"' % detectedTag)
        #                 if detectedTag in self.undetectedTags:
        #                     self.get_logger().info('Target "%s" has been detected' % detectedTag)    
        #                     self.get_logger().info(f'Landing {drone} on "%s"' % detectedTag)
        #                     self.undetectedTags.remove(detectedTag)
        #                     #land_command(int(drone[2:]))
        #                     land_command(int(drone[2:], 16))
        #             return
        #         return listener_callback
            
            
        #     current_callback = create_callback(drone)
        #     current_callback.__name__ = callback_name   # give the callback function a specific name.
        #     setattr(self, callback_name, current_callback)
        #     self.callbacks[drone] = current_callback





    def listener_callback(self, msg):
        if msg.transforms:
            detectedTag = msg.transforms[0].child_frame_id
            self.get_logger().info('CF13 saw: "%s"' % detectedTag)
            if detectedTag in self.undetectedTags:
                self.get_logger().info('Target "%s" has been detected' % detectedTag)    
                self.get_logger().info('Landing Crazyflie 13 on "%s"' % detectedTag)
                self.undetectedTags.remove(detectedTag)
                land_command(0x37)
        return
    
    def listener_callback2(self, msg):
        if msg.transforms:
            detectedTag = msg.transforms[0].child_frame_id
            self.get_logger().info('CF14 saw: "%s"' % detectedTag)
            if detectedTag in self.undetectedTags:
                self.get_logger().info('Target "%s" has been detected' % detectedTag)    
                self.get_logger().info('Landing Crazyflie 14 on "%s"' % detectedTag)       
                self.undetectedTags.remove(detectedTag)
                land_command(0x38)
        return 

    # def listener_callback3(self, msg):
    #     if msg.transforms:
    #         #self.get_logger().info('CF15 saw')
    #         detectedTag = msg.transforms[0].child_frame_id
    #         self.get_logger().info('CF15 saw: "%s"' % detectedTag)
    #         if detectedTag in self.undetectedTags:
    #             self.get_logger().info('Target "%s" has been detected' % detectedTag)    
    #             self.get_logger().info('Landing Crazyflie 15 on "%s"' % detectedTag)       
    #             self.undetectedTags.remove(detectedTag)
    #             land_command(0x15)
    #     return
    
#     def listener_callback4(self, msg):
#         #self.get_logger().info('I heard: "something' )
#         # check if drone is up down
#             #ignore
#         # check if message empty
#             #ignore
#         # check if target is captured
#             #ignore
#             #run takeoff.py
#         if msg.transforms:
#             #self.get_logger().info('CF16 saw')
#             detectedTag = msg.transforms[0].child_frame_id
#             self.get_logger().info('CF16 saw: "%s"' % detectedTag)
#             if detectedTag in self.undetectedTags:
#                 self.get_logger().info('Target "%s" has been detected' % detectedTag)    
#                 self.get_logger().info('Landing Crazyflie 16 on "%s"' % detectedTag)       
#                 self.undetectedTags.remove(detectedTag)
#                 land_command(0x16)
#                 #land
#         return

#     def listener_callback5(self, msg):
#         #self.get_logger().info('I heard: "something' )
#         # check if drone is up down
#             #ignore
#         # check if message empty
#             #ignore
#         # check if target is captured
#             #ignore
#             #run takeoff.py
#         if msg.transforms:
#             #self.get_logger().info('CF17 saw')
#             detectedTag = msg.transforms[0].child_frame_id
#             self.get_logger().info('CF17 saw: "%s"' % detectedTag)
#             if detectedTag in self.undetectedTags:
#                 self.get_logger().info('Target "%s" has been detected' % detectedTag)    
#                 self.get_logger().info('Landing Crazyflie 17 on "%s"' % detectedTag)       
#                 self.undetectedTags.remove(detectedTag)
#                 land_command(0x17)
#                 #land
#         return


def main(args=None):
    rclpy.init(args=args)

    mission_planner = MissionPlanner()

    rclpy.spin(mission_planner)




if __name__ == '__main__':
    main()