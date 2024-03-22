from cflib.drivers.crazyradio import Crazyradio
import time
import sys
from cflib.utils import power_switch

if __name__ == '__main__':
    try:
        channel = sys.argv[1]
    except IndexError:
        print("Enter channel number")
    drone_channel = {"cf01":80,"cf02":80,"cf03":80,"cf04":80,"cf05":80,
        "cf06":120,"cf07":120,"cf08":120,"cf09":120,"cf10":120,
        "cf11":120,"cf12":120,"cf13":120,"cf14":60,"cf15":60,
        "cf16":60,"cf17":60,"cf18":60,"cf19":60,"cf20":60,
        "cf21":60,"cf22":60,"cf23":60,"cf24":60,"cf25":60,
        "cf26":120,"cf27":80,"cf28":60,"cf29":60,"cf30":120,
        "cf31":80,"cf32":120,"cf33":120,"cf34":120,"cf35":60,
        "cf36":60,"cf37":60,"cf38":60,"cf39":60,"cf40":60}
    for i in drone_channel:
        if drone_channel[i] == int(channel):
            id = i[2:]
            cf = power_switch.PowerSwitch(f'radio://0/{channel}/2M/E7E7E7E7{id}')
            cf.platform_power_down()
            print(f'power down Drone {id} on channel {channel}')