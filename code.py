import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

MQ135_PIN = 5
GPIO.setup(MQ135_PIN, GPIO.IN)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print("Failed to read from DHT sensor")

    print("MQ135 value: {0}".frmat(GPIO.input(MQ135_PIN)))
    
    time.sleep(3)
