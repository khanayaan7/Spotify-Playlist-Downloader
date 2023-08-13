import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = "Any spotify playlist link"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"]
              for x in sp.playlist_tracks(playlist_URI)["items"]]
index = 1
results = []
for track in sp.playlist_tracks(playlist_URI)["items"]:

    track_uri = track["track"]["uri"]
    track_name = track["track"]["name"]
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    artist_name = track["track"]["artists"][0]["name"]

    val = f"{track_name}-{artist_name}"
    results += [val]

df = pd.DataFrame(results, columns=["Song Names"])
df.to_csv(r'Path of where you want to save songs.csv file', index=False)
