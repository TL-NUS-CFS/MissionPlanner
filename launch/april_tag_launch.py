'''
"ros2 run ai_deck_wrapper ai_deck_wrapper --ros-args -p period:=0.1 -r image_rect:=/cf13/image_rect -r camera_info:=/cf13/camera_info "
"ros2 run apriltag_ros apriltag_node --ros-args -r image_rect:=/cf13/image_rect -r tf:=/cf13/tf -r camera_info:=/cf13/camera_info -r detections:=/cf13/detections"
"ros2 run mission_planner mission_planner"
'''
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node





def generate_launch_description():
    ai_deck_wrapper = Node(
            package='ai_deck_wrapper',
            executable='ai_deck_wrapper',
            namespace='cf13',
            output='screen',
            parameters=[{
                'period': 0.1,
            }],
            remappings=[
                ('/image_rect', '/cf13/image_rect'),
                ('/camera_info', '/cf13/camera_info'),
            ])
    apriltag_node = Node(
            package='apriltag_ros',
            executable='apriltag_node',
            namespace='cf13',
            output='screen',
            remappings=[
                ('/image_rect', '/cf13/image_rect'),
                ('/camera_info', '/cf13/camera_info'),
                ('/tf','/cf13/tf'),
                ('/detections','/cf13/detections'),
            ]
            )
    ai_deck_wrapper2 = Node(
            package='ai_deck_wrapper',
            executable='ai_deck_wrapper',
            namespace='cf15',
            output='screen',
            parameters=[{
                'period': 0.1,
                'ip':"192.168.1.115"
            }],
            remappings=[
                ('/image_rect', '/cf15/image_rect'),
                ('/camera_info', '/cf15/camera_info'),
            ])
    apriltag_node2 = Node(
            package='apriltag_ros',
            executable='apriltag_node',
            namespace='cf15',
            output='screen',
            remappings=[
                ('/image_rect', '/cf15/image_rect'),
                ('/camera_info', '/cf15/camera_info'),
                ('/tf','/cf15/tf'),
                ('/detections','/cf15/detections'),
            ]
    mission_planner = Node(
            package='mission_planner',
            executable='mission_planner',
            output='screen',
            )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(ai_deck_wrapper)
    ld.add_action(apriltag_node)
    ld.add_action(ai_deck_wrapper2)
    ld.add_action(apriltag_node2)

    return ld
