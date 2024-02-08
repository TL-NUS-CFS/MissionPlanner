from cflib.drivers.crazyradio import Crazyradio
import time; import threading
import sys
from land_all import land_all_command

def takeoff(channel):
    cr = Crazyradio(devid=0)
    cr.set_channel(channel)
    cr.set_data_rate(cr.DR_2MPS)

    for i in range(3):
        # Send multicast packet to P2P port 7
        cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7))
        cr.set_ack_enable(False)
        cr.send_packet( (0xff, 0x80, 0x63, 0x01, 0xff) )
        print('send')

        time.sleep(0.01)
    cr.close()
if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            takeoff(channel = int(sys.argv[i]))

    timer_thread = threading.Timer(2, land_all_command) 
    timer_thread.start()       
    #takeoff(channel=int(sys.argv[1]))
