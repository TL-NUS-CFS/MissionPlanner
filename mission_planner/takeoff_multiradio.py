from cflib.drivers.crazyradio import Crazyradio
import time; import threading
import sys
from land_all import land_all_command

def takeoff(channel):

    all_cr = dict()
    for i in range(0, len(channel)-1):
        variable = 'cr_' + str(i)
        all_cr[variable] = Crazyradio(devid=i)
        all_cr[variable].set_channel(int(channel[i+1]))
        all_cr[variable].set_data_rate(all_cr[variable].DR_2MPS)


    # Takeoff for multiple channels 
    for i in range(3):
        for i, (variable, cr) in enumerate(all_cr.items()):
          
            cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7))
            cr.set_ack_enable(False)
            cr.send_packet( (0xff, 0x80, 0x63, 0x01, 0xff) )
            print(str(variable), 'send')
        time.sleep(0.01)

    for i, (variable, cr) in enumerate(all_cr.items()):
        cr.close()


if __name__ == '__main__':
    print('here',sys.argv)
    takeoff(channel=(sys.argv))

    timer_thread = threading.Timer(1, land_all_command, args=(sys.argv,))
    timer_thread.start()       
