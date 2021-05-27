#!/usr/bin/env python3
import os
import sys
import yaml
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.dates as md
import requests


def graph(city: str, file: str) -> str:
	data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid=e372c502e24c89544b4d0f938b65ca84")
	weatherInfo = data.json()

	dts = [x['dt_txt'] for x in weatherInfo['list']]
	y_val = [x['main']['temp'] for x in weatherInfo['list']]
	plt.figure(figsize=(17, 8))
	plt.subplots_adjust(bottom=0.3)
			# x, y
	# plt.title(11, 23, f"Weather for: {weatherInfo['city']['name']}", size=10, color='black')
	plt.title(f"Weather for: {weatherInfo['city']['name']}")
	plt.ylabel('Temperature C')
	plt.xticks(rotation=45)
	plt.tick_params(axis='x', which='minor', labelsize=15)
	print('y_val: ',y_val)
	print('dts: ',dts)
	plt.plot(dts, y_val)
	# plt.show()
	plt.savefig(file)
	# ax.savefig(file)

	return file


if __name__ == "__main__":
  command = sys.argv[1]
  argument_file = os.environ["FILE"]
  argument_city = os.environ["CITY"]

  functions = {
    "graph": graph,
  }
  output = functions[command](argument_city, argument_file)
  print(yaml.dump({"output": output}))
