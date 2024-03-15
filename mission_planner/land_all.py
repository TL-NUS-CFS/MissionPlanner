
from cflib.drivers.crazyradio import Crazyradio
import time
import sys



def land_all_command(channel):   
    
    # Define crazyradios
    all_cr = dict()
    for i in range(len(channel)):
        variable = 'cr_' + str(i+1)
        all_cr[variable] = Crazyradio(devid=i+1)
        all_cr[variable].set_channel(int(channel[i]))
        all_cr[variable].set_data_rate(all_cr[variable].DR_2MPS)

    
    # Land all for multiple channels
    for i in range(3):
        for i, (variable, cr) in enumerate(all_cr.items()):

            cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7)) # sets destination address for outgoing packets
            cr.set_ack_enable(False) # disable acknowledgement for outgoing packets
            cr.send_packet((0xff, 0x80, 0x63, 0x02, 0xff )) # sends packet to destination address via radio link 
            #cr.send_packet( (0xff, 0x80, 0x63, 0x00, 0xff))
            print(str(variable), 'Move away from walls ', int(channel[i]))

        time.sleep(0.01)
    for i, (variable, cr) in enumerate(all_cr.items()):
        cr.close()


if __name__ == '__main__':
    print('here',sys.argv)
    channel_list = sys.argv[1:]
    # land_all_command(channel=(sys.argv))
    try:
            land_all_command(channel=channel_list)
    except IndexError:
        print("Please specify channels")
