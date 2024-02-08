from cflib.drivers.crazyradio import Crazyradio
import time; import threading
import sys
from land_all import land_all_command

def takeoff(channel):
    cr = Crazyradio(devid=0)
    print(channel)
    cr.set_channel(int(channel[1]))
    cr.set_data_rate(cr.DR_2MPS)

    cr2 = Crazyradio(devid=1)
    cr2.set_channel(int(channel[2]))
    cr2.set_data_rate(cr.DR_2MPS)

    for i in range(3):
        # Takeoff for 1st channel 
        cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7))
        cr.set_ack_enable(False)
        cr.send_packet( (0xff, 0x80, 0x63, 0x01, 0xff) )
        print('CR1: send')

        # Takeoff for 2nd channel 
        cr2.set_address((0xff,0xe7,0xe7,0xe7,0xe7))
        cr2.set_ack_enable(False)
        cr2.send_packet( (0xff, 0x80, 0x63, 0x01, 0xff) )
        print('CR2: send')

        time.sleep(0.01)
    cr.close()
    cr2.close()
if __name__ == '__main__':
    takeoff(channel=(sys.argv))

    timer_thread = threading.Timer(2, land_all_command) 
    timer_thread.start()       
