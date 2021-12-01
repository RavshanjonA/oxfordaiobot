import requests
from pprint import pprint as print
from keys import app_id, app_key
import json
language = "en-gb"
word_id = "python"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
data = r.json()
print(data)