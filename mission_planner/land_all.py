
from cflib.drivers.crazyradio import Crazyradio
import time
import sys



def land_all_command(channel):   
    
    # Define crazyradios
    all_cr = dict()
    for i in range(0, len(channel)-1):
        variable = 'cr_' + str(i)
        all_cr[variable] = Crazyradio(devid=i)
        all_cr[variable].set_channel(int(channel[i+1]))
        all_cr[variable].set_data_rate(all_cr[variable].DR_2MPS)

    
    # Land all for multiple channels
    for i in range(2):
        for i, (variable, cr) in enumerate(all_cr.items()):

            cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7)) # sets destination address for outgoing packets
            cr.set_ack_enable(False) # disable acknowledgement for outgoing packets
            cr.send_packet((0xff, 0x80, 0x63, 0x00, 0xff )) # sends packet to destination address via radio link 
            print(str(variable),'send land to all')

        time.sleep(0.01)



if __name__ == '__main__':
    print('here',sys.argv)
    land_all_command(channel=(sys.argv))
    #land_all_command(channel=int(sys.argv[1]), drone_address=int(sys.argv[2], 16))
