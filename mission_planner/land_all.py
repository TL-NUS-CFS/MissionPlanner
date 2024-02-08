
from cflib.drivers.crazyradio import Crazyradio
import time
import sys
#from .land import land_command

channels = [120, 80]

def land_all_command(drone_address=0xff):   
    cr = Crazyradio(devid=0) #devid = radio dongle id (0 being the first dongle)

    for i in channels: 
        cr.set_channel(i)
        print(i)
        cr.set_data_rate(cr.DR_2MPS)

        for i in range(2):

            # Send multicast packet to P2P port 7
            cr.set_address((0xff,0xe7,0xe7,0xe7,0xe7)) # sets destination address for outgoing packets
            cr.set_ack_enable(False) # disable acknowledgement for outgoing packets
            cr.send_packet( (0xff, 0x80, 0x63, 0x00, drone_address) ) # sends packet to destination address via radio link 
            print('send land to ' + str(drone_address))

            time.sleep(0.01)
        #cr.close()
        #return 0


# def land_all_command():
#     channels = [80,120]
#     crazyflie_data = {  
#         "CF01": 80, "CF02": 80, "CF03": 80, "CF04": 80, "CF05": 80, "CF06": 120, "CF07": 120, "CF08": 120, "CF09": 100, "CF10": 100,
#         "CF11": 120, "CF12": 120, "CF13": 120, "CF14": 120, "CF15": 120, "CF16": 60, "CF17": 120, "CF18": 60, "CF19": 60,
#         "CF20": 60, "CF21": 60, "CF22": 60, "CF23": 60, "CF24": 60, "CF25": 60, "CF26": 90, "CF27": 90, "CF28": 90,
#         "CF29": 90, "CF30": 90, "CF31": 110, "CF32": 110, "CF33": 110, "CF34": 110, "CF35": 110, "CF36": 70, "CF37": 70,
#         "CF38": 70, "CF39": 70, "CF40": 70
#     }
    

#     for drone_id,ch in crazyflie_data.items():
#         numeric_part = int(drone_id[2:])
#         hex_id = '0x' + str(numeric_part)
#         land_command(channel=ch, drone_address=int(hex_id,16))


if __name__ == '__main__':
    land_all_command()

'''
0xff = broadcast address
0xe7 = multicast address (vendor specific address)
0x80 = 
0x63 = command to control whether crazyflies should keep flying
0x00 = 
'''
