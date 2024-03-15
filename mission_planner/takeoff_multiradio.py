from cflib.drivers.crazyradio import Crazyradio
import time; import threading
import sys
from land_all import land_all_command

def takeoff(channel):

    all_cr = dict()
    for i in range(len(channel)):
        variable = 'cr_' + str(i+1)
        all_cr[variable] = Crazyradio(devid=i+1)
        all_cr[variable].set_channel(int(channel[i]))
        all_cr[variable].set_data_rate(all_cr[variable].DR_2MPS)


    # Takeoff for multiple channels 
    for i in range(3):
        for i, (variable, cr) in enumerate(all_cr.items()):
          
            cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7))
            cr.set_ack_enable(False)
            cr.send_packet( (0xff, 0x80, 0x63, 0x01, 0xff) )
            print(str(variable), 'send takeoff for channel', int(channel[i]))
        time.sleep(0.01)

    for i, (variable, cr) in enumerate(all_cr.items()):
        cr.close()


if __name__ == '__main__':
    #print('input',sys.argv)
    half = len(sys.argv[1:])//2
    all_channels = sys.argv[1:]
    channel_list = all_channels[:half]
    print('first wave',channel_list)
    channel_list_2 = all_channels[half:]
    print('second wave',channel_list_2)

    print('takeoff for first wave')
    takeoff(channel=channel_list)
    time.sleep(20)
    print('takeoff for second wave')
    takeoff(channel=channel_list_2)
    time.sleep(90)
    print('MISSION TIME 50%')
    time.sleep(90)
    print('land for first wave')
    land_all_command(channel=channel_list)
    time.sleep(2)
    print('land for second wave')
    land_all_command(channel=channel_list_2)

    # time_value= 60 # vary the time value to change the time delay before landing
    # timer_thread = threading.Timer(time_value, land_all_command, args=(sys.argv,)) 
    # timer_thread.start()       
