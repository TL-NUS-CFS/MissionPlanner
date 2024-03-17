## How to use
1) `mkdir -p <workspace_name>/src && cd <workspace_name>/src`
2)	git clone these 4 repos
    *	https://github.com/christianrauch/apriltag_ros
    *	https://github.com/christianrauch/apriltag_msgs
    *	https://github.com/TL-NUS-CFS/ai_deck_wrapper
    *	https://github.com/TL-NUS-CFS/MissionPlanner

3)	Change these lines in *MissionPlanner/mission_planner/mission_planner.py* for your required tags and drones
   ```
self.undetectedTags = {"tag36h11:200","tag36h11:204","tag36h11:205"}
self.doublerescue = {"tag36h11:206":2}
drone_ids = {"cf03":True,"cf04":True,"cf05":True}
```
5)	Change this line in *MissionPlanner/launch/april_tag_launch.py* for your required drones
```
drone_ids = ["cf04","cf03","cf05"]
```
6)	cd back to <workspace_name> 
7)	`colcon build && source install/setup.bash`
8)	`ros2 launch mission_planner april_tag_launch.py`
    *	starts apriltag streaming and processing
    *	starts the mission tracking node
    *	any changes to drone names and ip and targets id alter this launch file
    *	will open the camera view as well
    *	will print to terminal if target detected
9)	`python3 src/MissionPlanner/mission_planner/mission_script.py <channels>`
    *	sends the takeoff command for multiple channels
    *	terminates after set time with move away from walls command


## Helper scripts
* takeoff.py
  
`python3 takeoff.py <channel>`
* land.py
  
`python3 land.py <channel> <id>`

* kill.py
  
`python3 kill.py <channel> <id>`

* takeoff_multiradio.py
  
`python3 takeoff_multiradio.py <channels> `

sends takeoff command to multiple channels

* land_all.py
  
`python3 land_all.py <channels>` 

sends move away from wall and land command to multiple channels
* land_multiradio.py

`python3 land_multiradio.py <channels>`

sends land immediately command to multiple channels