from datetime import datetime
import csv

now = datetime.now()

year_str = str(now.year)
month_str = f"{now.month:02d}"
day_str = f"{now.day:02d}"
hour_str = f"{now.hour:02d}"
minute_str = f"{now.minute:02d}"
second_str = f"{now.second:02d}"

file_path = f"data/{year_str}/{month_str}/{day_str}.csv"

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f"{row[0]} , {row[1]} , {row[2]} , {row[3]} , {row[4]}")