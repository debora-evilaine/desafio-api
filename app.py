from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_locations_page():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])

@app.route("/episodes")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"] )

# def get_list_episodes():
#     url = "https://rickandmortyapi.com/api/episode"
#     response = urllib.request.urlopen(url)
#     episodes = response.read()
#     dict = json.loads(episodes)

#     episodes = []

#     for episode in dict["results"]:
#         episode = {
#             "name": episode["name"],
#             "air_date": episode["air_date"],
#             "id": episode["id"]
#         }

#         episodes.append(episode)
#     return {"episodes": episodes}
    

@app.route("/locations")
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