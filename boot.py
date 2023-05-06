import network
import urequests as requests
import config
"""
in config file
username = "YOUR_ADAFRUIT_USERNAME"
wifi_ssid = "YOUR_WIFI_SSID"
wifi_password = "YOUR_WIFI_PASSWORD"
aio_key = "YOUR_ADAFRUIT_IO_KEY"
"""
from time import sleep as delay

def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(config.wifi_ssid, config.wifi_password)
    print("Connecting to", str(config.wifi_ssid))
    while not sta_if.isconnected():
        print(".", end = "")
        delay(1)
    print("Connected")
    
def publish_data(feed, value):
    url = 'https://io.adafruit.com/api/v2/' + config.username + '/feeds/' + feed + '/data'
    body = {'value': str(value)}
    headers = {'X-AIO-Key': config.aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        #print(r.text)
        print("published")
    except Exception as e:
        print(e)