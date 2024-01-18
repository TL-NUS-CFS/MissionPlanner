'''
"ros2 run ai_deck_wrapper ai_deck_wrapper --ros-args -p period:=0.1 -r image_rect:=/cf37/image_rect -r camera_info:=/cf37/camera_info "
"ros2 run apriltag_ros apriltag_node --ros-args -r image_rect:=/cf37/image_rect -r tf:=/cf37/tf -r camera_info:=/cf37/camera_info -r detections:=/cf37/detections"
"ros2 run mission_planner mission_planner"
'''
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node





def generate_launch_description():

    # DRONE 1
    ai_deck_wrapper = Node(
            package='ai_deck_wrapper',
            executable='ai_deck_wrapper',
            namespace='cf37',
            output='screen',
            parameters=[{
                'period': 0.1,
                'ip': "192.168.1.137"
            }],
            remappings=[
                ('/image_rect', '/cf37/image_rect'),
                ('/camera_info', '/cf37/camera_info'),
            ])
    apriltag_node = Node(
            package='apriltag_ros',
            executable='apriltag_node',
            namespace='cf37',
            output='screen',
            remappings=[
                ('/image_rect', '/cf37/image_rect'),
                ('/camera_info', '/cf37/camera_info'),
                ('/tf','/cf37/tf'),
                ('/detections','/cf37/detections'),
            ]
            )
    
    # DRONE 2
    ai_deck_wrapper2 = Node(
            package='ai_deck_wrapper',
            executable='ai_deck_wrapper',
            namespace='cf38',
            output='screen',
            parameters=[{
                'period': 0.1,
                'ip':"192.168.1.138",
                'name':"cf38"
            }],
            remappings=[
                ('/image_rect', '/cf38/image_rect'),
                ('/camera_info', '/cf38/camera_info'),
            ])
    apriltag_node2 = Node(
            package='apriltag_ros',
            executable='apriltag_node',
            namespace='cf38',
            output='screen',
            remappings=[
                ('/image_rect', '/cf38/image_rect'),
                ('/camera_info', '/cf38/camera_info'),
                ('/tf','/cf38/tf'),
                ('/detections','/cf38/detections'),
            ])
    
    # DRONE 3
    ai_deck_wrapper3 = Node(
            package='ai_deck_wrapper',
            executable='ai_deck_wrapper',
            namespace='cf39',
            output='screen',
            parameters=[{
                'period': 0.1,
                'ip':"192.168.1.139",
                'name':"cf39"
            }],
            remappings=[
                ('/image_rect', '/cf39/image_rect'),
                ('/camera_info', '/cf39/camera_info'),
            ])
    apriltag_node3 = Node(
            package='apriltag_ros',
            executable='apriltag_node',
            namespace='cf39',
            output='screen',
            remappings=[
                ('/image_rect', '/cf39/image_rect'),
                ('/camera_info', '/cf39/camera_info'),
                ('/tf','/cf39/tf'),
                ('/detections','/cf39/detections'),
            ])
    
    # # DRONE 4
    # ai_deck_wrapper4 = Node(
    #         package='ai_deck_wrapper',
    #         executable='ai_deck_wrapper',
    #         namespace='cf16',
    #         output='screen',
    #         parameters=[{
    #             'period': 0.1,
    #             'ip':"192.168.1.116",
    #             'name':"cf16"
    #         }],
    #         remappings=[
    #             ('/image_rect', '/cf16/image_rect'),
    #             ('/camera_info', '/cf16/camera_info'),
    #         ])
    # apriltag_node4 = Node(
    #         package='apriltag_ros',
    #         executable='apriltag_node',
    #         namespace='cf16',
    #         output='screen',
    #         remappings=[
    #             ('/image_rect', '/cf16/image_rect'),
    #             ('/camera_info', '/cf16/camera_info'),
    #             ('/tf','/cf16/tf'),
    #             ('/detections','/cf16/detections'),
    #         ])

    # # DRONE 5
    # ai_deck_wrapper5 = Node(
    #         package='ai_deck_wrapper',
    #         executable='ai_deck_wrapper',
    #         namespace='cf17',
    #         output='screen',
    #         parameters=[{
    #             'period': 0.1,
    #             'ip':"192.168.1.117",
    #             'name':"cf17"
    #         }],
    #         remappings=[
    #             ('/image_rect', '/cf17/image_rect'),
    #             ('/camera_info', '/cf17/camera_info'),
    #         ])
    # apriltag_node5 = Node(
    #         package='apriltag_ros',
    #         executable='apriltag_node',
    #         namespace='cf17',
    #         output='screen',
    #         remappings=[
    #             ('/image_rect', '/cf17/image_rect'),
    #             ('/camera_info', '/cf17/camera_info'),
    #             ('/tf','/cf17/tf'),
    #             ('/detections','/cf17/detections'),
    #         ])



    # MISSION PLANNER
    mission_planner = Node(
            package='mission_planner',
            executable='mission_planner',
            output='screen',
            # parameters=[{
            #     'undetectedTags': ["tag36h11:200"]
            # }],
            )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(ai_deck_wrapper)
    ld.add_action(apriltag_node)
    ld.add_action(ai_deck_wrapper2)
    ld.add_action(apriltag_node2)
    ld.add_action(ai_deck_wrapper3)
    ld.add_action(apriltag_node3)
    # ld.add_action(ai_deck_wrapper4)
    # ld.add_action(apriltag_node4)
    # ld.add_action(ai_deck_wrapper5)
    # ld.add_action(apriltag_node5)
    ld.add_action(mission_planner)

    return ld
