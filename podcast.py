#podcast.py
#app to allow users to search for podcasts

import os
import requests
import json
#import unirest

from dotenv import load_dotenv

#capture keys
load_dotenv()
my_cred = os.environ.get("X_LISTEN_API_KEY")
request_url = "https://listen-api.listennotes.com/api/v2/search?q=star%20wars&sort_by_date=0&type=episode&offset=0&len_min=10&len_max=30&genre_ids=68%2C82&published_before=1390190241000&published_after=0&only_in=title%2Cdescription&language=English&safe_mode=1"
response = requests.get(request_url, headers={"X-ListenAPI-Key": my_cred})
parsed_response = json.loads(response.text)

print(response)
print(my_cred)

breakpoint()


#price = response.json()


