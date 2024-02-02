from cflib.drivers.crazyradio import Crazyradio
import time
import sys
from cflib.utils import power_switch

if __name__ == '__main__':
    id = sys.argv[1]
    cf = power_switch.PowerSwitch(f'radio://0/80/2M/E7E7E7E7{id}')
    cf.platform_power_down()
