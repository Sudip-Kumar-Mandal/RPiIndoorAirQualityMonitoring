from datetime import datetime
import os
import serial

ser = serial.Serail('/dev/ttyACMO', 9600) #Opens a serial connection with the Arduino. You might need to identify the correct device name using ls /dev/tty* in the Raspberry Pi terminal. The name might be like /dev/ttyACM0.

while True:
    if ser.available():

        now = datetime.now()

        year_str = str(now.year)
        month_str = f"{now.month:02d}"
        day_str = f"{now.day:02d}"
        hour_str = f"{now.hour:02d}"
        minute_str = f"{now.minute:02d}"
        second_str = f"{now.second:02d}"

        time_str = f"{hour_str}:{minute_str}:{second_str}"

        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists(f"data/{year_str}"):
            os.mkdir(f"data/{year_str}")
        if not os.path.exists(f"data/{year_str}/{month_str}"):
            os.mkdir(f"data/{year_str}/{month_str}")
    
        data = ser.readline().decode('utf-8')
        data = f"{time_str},{data}"

        file_path = f"data/{year_str}/{month_str}/{day_str}.csv"

        with open(file_path, mode='a') as file:
            file.write(data)