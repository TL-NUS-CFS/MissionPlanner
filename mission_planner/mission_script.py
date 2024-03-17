import time; import threading
import sys
from land_all import land_all_command
from takeoff_multiradio import takeoff


MISSION_TIME = 180
WAVE_TAKEOFF_INTERVAL = 20
WAVE_LAND_INTERVAL = 2

if __name__ == '__main__':
    #print('input',sys.argv)
    half = len(sys.argv[1:])//2
    all_channels = sys.argv[1:]
    channel_list = all_channels[:half]
    print('first wave',channel_list)
    channel_list_2 = all_channels[half:]
    print('second wave',channel_list_2)

    print('takeoff for first wave')
    takeoff_multiradio(channel=channel_list)
    time.sleep(WAVE_INTERVAL)
    print('takeoff for second wave')
    takeoff_multiradio(channel=channel_list_2)

    time.sleep(MISSION_TIME/4)
    print('MISSION TIME 25%')
    time.sleep(MISSION_TIME/4)
    print('MISSION TIME 50%')
    time.sleep(MISSION_TIME/4)
    print('MISSION TIME 75%')
    time.sleep(MISSION_TIME/4)
    print('MISSION DONE')

    print('land for first wave')
    land_all_command(channel=channel_list)
    time.sleep(WAVE_LAND_INTERVAL)
    print('land for second wave')
    land_all_command(channel=channel_list_2)