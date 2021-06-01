#!/usr/bin/env python3
import os
import sys
import yaml
import matplotlib.pyplot as plt
import requests

def graph(city: str, apikey: str, file: str) -> str:
	# GET request to openWeatherMap API for fetching the coming 5 days per 3 hours (40 datapoints) API-key can be requested for free on https://openweathermap.org/api
	data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={apikey}")
	weatherInfo = data.json()

	# map the x and y axis with the weatherInfo
	dts = [x['dt_txt'] for x in weatherInfo['list']]
	y_val = [x['main']['temp'] for x in weatherInfo['list']]

	# adjusting figure size to fit the 40 datapoints and add labels to axis.
	plt.figure(figsize=(17, 8))
	plt.subplots_adjust(bottom=0.3)
	plt.title(f"Weather for: {weatherInfo['city']['name']}")
	plt.ylabel('Temperature C')
	plt.xticks(rotation=45)
	plt.tick_params(axis='x', which='minor', labelsize=15)

	# plot the graph and save it to file path.
	plt.plot(dts, y_val)
	plt.savefig(file)

	return file


if __name__ == "__main__":
  command = sys.argv[1]
  argument_file = os.environ["FILE"]
  argument_city = os.environ["CITY"]
  argument_key = os.environ["APIKEY"]

  functions = {
    "graph": graph,
  }
  output = functions[command](argument_city, argument_key, argument_file)
  print(yaml.dump({"output": output}))
