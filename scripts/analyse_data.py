import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

pd.set_option('display.float_format', lambda x: '%.2f' % x)

now = datetime.now()

year_str = str(now.year)
month_str = f"{now.month:02d}"
day_str = f"{now.day:02d}"

file_path = f"data/{year_str}/{month_str}/{day_str}.csv"

data = pd.read_csv(file_path)
data.columns = ["Time", "Temp", "Humi", "MQ135", "MQ7"]
data["Time"] = pd.to_datetime(data["Time"], format="%H:%M:%S")
data.set_index("Time", inplace=True)

with open("analysed_data/text.txt", mode='w') as file:
    file.write(data.describe().to_string())


data_to_plot = ["Temp", "Humi", "MQ135", "MQ7"]

plt.figure(figsize=(10, 6))

for col in data_to_plot:
    plt.plot(data.index, data[col], label=col)

plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Indoor Air Quality")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analysed_data/chart.png")