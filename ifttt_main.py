
from time import sleep

sensor = dht.DHT11(Pin(14))

try:
  sensor.measure()
  temp = sensor.temperature() * (9/5) + 32.0
  hum = sensor.humidity()
  print(temp, hum)
  
  sensor_readings = {'value1':temp, 'value2':hum}
  print(sensor_readings)

  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    'https://maker.ifttt.com/trigger/dht11_reading/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  print(request.text)
  request.close()
  
except:
    print('panic')
