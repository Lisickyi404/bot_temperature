import requests
import json

def parseGetCity(message):
	city=''
	for i in range(len(message)):
		if(i>4):
			city+=message[i]
	return city

print(parseGetCity('temp Moscow'))
def getTemeratureCity(city):
	url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

	querystring = {"q": str(city), "days": "3"}

	headers = {
		"X-RapidAPI-Key": "8310a092damsh88d5f346c407ed7p18784fjsn304e9d3e486b",
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)

	data_dict = json.loads(response.text)
	print(data_dict['current']['temp_c'])
	return data_dict['current']['temp_c']


print(getTemeratureCity(city='Moscow'))



