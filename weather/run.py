#!/usr/bin/env python3
import os
import sys
import yaml
import matplotlib.pyplot as plt
import matplotlib.dates as md
import requests


def graph(city: str, file: str) -> str:
	data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid=e372c502e24c89544b4d0f938b65ca84")
	weatherInfo = data.json()

	dts = [x['dt_txt'] for x in weatherInfo['list']]
	y_val = [x['main']['temp'] for x in weatherInfo['list']]
	plt.subplots_adjust(bottom=0.3)
	plt.text(0.9, 0.9, f"Weather for: {weatherInfo['city']['name']}", size=8, color='black')
	plt.xticks(rotation=90)
	plt.tick_params(axis='x', which='minor', labelsize=8)
	plt.plot(dts, y_val)
	plt.savefig(file)

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
