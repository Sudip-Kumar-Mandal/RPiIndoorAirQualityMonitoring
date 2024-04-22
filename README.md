# Indoor air quality monitoring with local processing and scheduled telegram alerts for improved health awareness

### Features:

-	Indoor air quality monitoring with mq135, mq7 sensor, dht11 sensor
-	Local data storage and analysis on sd card
-	Daily air quality summary report sent as notification to telegram
-	Hazard detection Telegram alert system

### Novelty:

-	Data stored on sd card and processed/analysed locally, no involvement of a cloud provider
-	Does not require constant internet connection, notification scheduled in case of no internet connictivity
-	User does not have to remember to open any app/dashboard, periodic notification containing the air quality summary is sent to user’s mobile

### Connection:

- MQ135, MQ7, DHT11 and other sensors are connected to Arduino UNO
- Arduino UNO is connected to RPi using serial communication protocol over the USB cable

**Data format**: `{timestamp},{temperature},{humidity},{mq135},{mq7}`

### Scripts:

- data_file_generation.py: receives data from Arudino UNO, creates file structure and writes data into the files
- data_analysis.py: creates a separate file with analysis data once per day
- telegram.py: sends telegram notifications
- arduino.ino: collects data from sensors and sends to RPi

### Libraries:

- Python:
    - datetime
    - time
    - os
    - serial
    - matplotlib
    - pandas
    - csv
    - telepot
- Arduino:
    - DHT.h