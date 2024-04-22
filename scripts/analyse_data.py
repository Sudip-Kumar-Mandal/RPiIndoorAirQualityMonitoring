import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)

data = pd.read_csv("data/2024/04/19.csv")
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