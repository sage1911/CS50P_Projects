import requests


def main():
    print("Fetching data from the Art Institute of Chicago API...")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} 
            ) 
        response.raise_for_status()
    except requests.HTTPError:
        print("HTTP error occurred")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
