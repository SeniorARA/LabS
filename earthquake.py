import requests
import asyncio

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

def print_earthquake():

    min_magnitude = input("Min Magnitude (float) : ")
    max_magnitude = input("Max Mangitude (float) : ")
    start_time = input("Start Time (xxxx-xx-xx format) : ")
    end_time = input("End Time (xxxx-xx-xx format) : ")

    try:
        responce = requests.get(url, params={
            "format" : "geojson",
            "starttime" : start_time,
            "endtime" : end_time,
            "minmagnitude" : min_magnitude,
            "maxmagnitude" : max_magnitude
        })
    except ConnectionError:
        print(requests.ConnectionError)

    data = responce.json()

    for feature in data["features"]:
        print("   Place : {}\n   Magnitude : {}\n   Coordinate : {}".format(feature["properties"]["place"], feature["properties"]["mag"], feature["geometry"]["coordinates"][0]))
        print("------------------------------")

print_earthquake()