# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
scan_result = wlan.scan()

for ap in scan_result:
    print(ap)    
