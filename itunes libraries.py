import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entiy=song&limit=50&term=" + sys.argv[1])

O = response.json()
for result in O["results"]:
    print(result["trackName"])


 
