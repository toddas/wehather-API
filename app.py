#TODO
#implament djnago
#make a full fledged website


import urllib.request
import json

api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Iveskite miesta: ")
api_key = "9a80336d5c6fa54817f1da43cba71299"
req_unit ="metric"

url = api_url + "?q=" + city + "&appid=" + api_key +"&units="+ req_unit
responce = urllib.request.urlopen(url)
parse_data = json.loads(responce.read())
temperatura = parse_data["main"]["temp"]
oras = parse_data["weather"][0]["description"]
icona = parse_data["weather"][0]["icon"]


print(str(temperatura) + "C")
print(oras)
#print(icona)
