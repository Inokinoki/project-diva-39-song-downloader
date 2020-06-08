import requests
from bs4 import BeautifulSoup
import os

def get_youtube_url(song_name):
    response = requests.get("https://www.youtube.com/results?search_query={}".format(song_name))
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('h3', class_="yt-lockup-title"):
        return "https://www.youtube.com{}".format(link.find('a')["href"])

def get_songs():
    response = requests.get("http://asia.sega.com/mega39s/cht/song/songlist.json")
    if response.status_code != 200:
        return []
    response_json = response.json()

    print(len(response_json))
    for song in response_json:
        url = get_youtube_url(song["title"])
        os.system("youtube-dl \"{}\"".format(url))  # TODO: maybe replace with the other solution

if __name__ == "__main__":
    get_songs()