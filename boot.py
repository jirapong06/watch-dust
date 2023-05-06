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
from utime import sleep as delay
from machine import Pin, ADC, I2C
import adc_lut as adc

sensor_pin = 35
v_sens = 0.5 # volt per 100ug/mmm
v_no_dust = 0.6


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
    r.close()
    return
        
def accurate_adc(raw):
    return adc.adc_lut[raw]

def read_dust_volt():
    sampling = []
    for i in range(64):
        raw_read = dust_sensor_pin.read()
        value = accurate_adc(raw_read)
        sampling.append(value)
        delay(0.1)
    avg = sum(sampling)/len(sampling)
    v = (3.3/4095)*avg
    return v

dust_sensor_pin = ADC(Pin(sensor_pin))
dust_sensor_pin.atten(ADC.ATTN_11DB)

