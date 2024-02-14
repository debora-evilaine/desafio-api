from flask import Flask, render_template
import urllib.request, json
from urllib.error import HTTPError, URLError

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

@app.route("/episode/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    uniqueEpisode = json.loads(data)

    return render_template("episode.html", episode=uniqueEpisode)

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

@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    uniqueLocation =  "" #setando a variável dict como uma string vazia para evitar o erro UnboundLocalError
    try:
        response = urllib.request.urlopen(url) 
        data = response.read()
        uniqueLocation = json.loads(data)
    except urllib.error.HTTPError as e:     
        print(e.reason)
        print("AAAAAAA")
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)

    return render_template("location.html", location=uniqueLocation)

@app.route("/character/<id>")
def get_character(id):
    try:
        url = "https://rickandmortyapi.com/api/character/" + id
        uniqueCharacter = ""
        response = urllib.request.urlopen(url)
        data = response.read()
        uniqueCharacter = json.loads(data)
    except urllib.error.HTTPError as e:
        print(e.reason)
        print("ERRO NO URLLIB!!!!!")
    except HTTPError as error:
        print(error.status, error.reason)
        print("ERRO DE HTTP!!!")
    except URLError as error:
        print(error.reason)
        print("ERRO DE URL!!!!!!!")

    return render_template("character.html", character=uniqueCharacter)