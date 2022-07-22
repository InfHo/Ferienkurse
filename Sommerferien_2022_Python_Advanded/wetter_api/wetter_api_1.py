import requests
import json



##print(t_json['weather'][14])

##for i in t_json['weather'][0]:
##    print(i, t_json['weather'][0][i])




##for i in t_json['weather']:
####    print(i, "\n\n")
##    for x in i:
##        print(x, i[x])
    
def wettermaschine(uhrzeit):
    result = requests.get(url)
    t = result.text
    t_json = json.loads(t)
    werte = t_json['weather'][uhrzeit]  
    quellen = t_json['weather'][uhrzeit]  
    print("Datum:", werte['timestamp'])
    print("Temperatur:",werte['temperature'])
    print("Windgeschwindigkeit:", werte['wind_speed'])

    
    return werte


if __name__ == "__main__":

    url = "https://api.brightsky.dev/weather?lat=52.5&lon=13.4&date=2022-07-22"

    result = requests.get(url)
    t = result.text
    t_json = json.loads(t)

    print(t_json["sources"][2])
