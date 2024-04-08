'''import Adafruit_DHT
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
'''

import csv

with open('data/2024/04/08.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Headers are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tmq135: {row[0]}, mq7: {row[1]}, temp: {row[2]}, humi: {row[3]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('data/2024/04/08.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['mq135', 'mq7', 'temp', 'humi'])
    writer.writerow([12,13,14,15])
    writer.writerow([14,10,15,15])