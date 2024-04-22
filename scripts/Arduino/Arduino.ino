#include "DHT.h"

const int dht_pin = 7;
const int mq135_pin = 0;
const int mq7_pin = 1;

DHT dht(dht_pin, DHT11);
int mq135_value = 0;
int mq7_value = 0;
float temp = 0.0f;
float humi = 0.0f;

void setup() {
    Serial.begin(9600);
    dht.begin();
}

void loop() {
    
    temp = dht.readTemperature();
    humi = dht.readHumidity();
    if(isnan(temp)) temp = 0.0f;
    if(isnan(humi)) humi = 0.0f;

    mq135_value = analogRead(mq135_pin);
    mq7_value = analogRead(mq7_pin);
    
    Serial.print(temp);
    Serial.print(",");
    Serial.print(humi);
    Serial.print(",");
    Serial.print(mq135_value);
    Serial.print(",");
    Serial.print(mq7_value);
    Serial.println();

    delay(10000);
}