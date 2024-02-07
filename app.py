from flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url) 
    locations = response.read()
    dict = json.loads(locations)

    locations = []

    for location in dict["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
            "link": location["url"]
        }

        locations.append(location)
    
    return {"locations": locations}
