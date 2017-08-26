from machine import Pin
from network import WLAN
from time import sleep
from DHT22RinusW import DHT22

dht_pin=Pin('P9', Pin.OPEN_DRAIN) # connect DHT22 sensor data line to pin P9/G16 on the expansion board
lastSSID = ""
while True:
    dht_pin(1) # drive pin high to initiate data conversion on DHT sensor
    tempInC, hum = DHT22(dht_pin)
    tempInF = round((tempInC/10) * 1.8 + 32)
    humidity = round(hum/10)
    SSID = "Temp: %d  Hum: %d" % (tempInF, humidity)
    if not lastSSID == SSID:
        wlan = WLAN(mode=WLAN.AP, ssid=SSID, auth=(WLAN.WPA2, '<YOUR PASSWORD HERE>'), channel=11, antenna=WLAN.INT_ANT)
        print ("Changed SSID:", SSID)
        lastSSID = SSID
    sleep(60*5) # update every 5 minutes
