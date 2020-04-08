from machine import Pin, I2C
import network
import urequests

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'wifi_network'
password = 'wifi_password'

api_key = 'api_key'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


