from cflib.drivers.crazyradio import Crazyradio
import time; import threading
import sys
from land_all import land_all_command

def takeoff_multiradio(channel):
    #uses radios 1,2,etc for however many different channels specified
    #radio 0 reserved for land.py
    #always plug in one more radio than number of channels used

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
    channel_list = sys.argv[1:]
    try:
            takeoff_multiradio(channel=channel_list)
    except IndexError:
        print("Please specify channels")