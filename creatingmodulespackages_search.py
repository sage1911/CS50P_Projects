import requests
from apicall_artists import get_artists

def main():
    artist = input("Artist: ")  
    artworks = get_artists(query=artist, limit=3)
    for artist in artworks:
        print(f"* {artist}")

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status() 
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]
    