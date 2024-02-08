
from cflib.drivers.crazyradio import Crazyradio
import time
import sys
#from .land import land_command

channels = [120, 80] # Vary this for different channels 

def land_all_command(drone_address=0xff):   
    cr = Crazyradio(devid=0) #devid = radio dongle id (0 being the first dongle)
    cr.set_channel(channels[0])
    cr.set_data_rate(cr.DR_2MPS)

    cr2 = Crazyradio(devid=1)
    cr2.set_channel(channels[1])
    cr2.set_data_rate(cr.DR_2MPS)


    for i in range(2):

        # Land all for 1st channel
        cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7)) # sets destination address for outgoing packets
        cr.set_ack_enable(False) # disable acknowledgement for outgoing packets
        cr.send_packet( (0xff, 0x80, 0x63, 0x00, drone_address) ) # sends packet to destination address via radio link 
        print('CR1: send land to ' + str(drone_address))

        # Land all for 1st channel
        cr2.set_address((0xff,0xe7,0xe7,0xe7,0xe7)) 
        cr2.set_ack_enable(False) 
        cr2.send_packet( (0xff, 0x80, 0x63, 0x00, drone_address) ) 
        print('CR2: send land to ' + str(drone_address))

        time.sleep(0.01)
    #cr.close()
    #return 0



if __name__ == '__main__':
    land_all_command()

'''
0xff = broadcast address
0xe7 = multicast address (vendor specific address)
0x80 = 
0x63 = command to control whether crazyflies should keep flying
0x00 = 
'''
