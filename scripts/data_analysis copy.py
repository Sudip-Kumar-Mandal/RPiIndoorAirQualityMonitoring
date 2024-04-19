from datetime import datetime
import csv
import matplotlib.pyplot as plt

now = datetime.now()

year_str = str(now.year)
month_str = f"{now.month:02d}"
day_str = f"{now.day:02d}"
hour_str = f"{now.hour:02d}"
minute_str = f"{now.minute:02d}"
second_str = f"{now.second:02d}"

file_path = f"data/{year_str}/{month_str}/{day_str}.csv"

time_stamp = []
temp = []
humi = []
mq135 = []
mq7 = []

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        time_stamp.append(row[0])
        temp.append(float(row[1]))
        humi.append(float(row[2]))
        mq135.append(int(row[3]))
        mq7.append(int(row[4]))

print(time_stamp)
print(temp)
print(humi)

plt.plot(time_stamp, temp)
plt.savefig("analysed_data/plot.png")

