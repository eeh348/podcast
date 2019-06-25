#podcast.py
#app to allow users to search for podcasts

import os
import requests
import json
import pprint
#import unirest

from dotenv import load_dotenv

#capture keys
load_dotenv()
my_cred = os.environ.get("X_LISTEN_API_KEY")

list_string = []
new_search = []

#define functions
def format_search(search):
    list_string = search.split()
    new_search = '%20'.join(list_string)
    return new_search

#if __name__ == '__main__': 

#capture multiple inputs in a list until user types DONE; does not validate if it's a valid stock symbol
#while True:
    #ask user for stock symbol
search = input("What topics are you looking to search: ") #fix spaces

new_search = format_search(search)

    #earch = symbol.upper()

    #if search == "DONE":
        #break
    #elif symbol.isalpha() and len(symbol) < 6:
        #symbol = symbol.upper()
        #symbol_list.append(symbol.upper())
    #else:
        #print("Input must be A-Z characters only and less than or equal to 5 characters")

#create user input

request_url = f"https://listen-api.listennotes.com/api/v2/search?q={new_search}&sort_by_date=0&type=episode&offset=0&len_min=10&len_max=30&genre_ids=68%2C82&published_before=1390190241000&published_after=0&only_in=title%2Cdescription&language=English&safe_mode=1"
response = requests.get(request_url, headers={"X-ListenAPI-Key": my_cred})
parsed_response = json.loads(response.text)

results = parsed_response['results']



for record in results:
    #results[record]['title_original']
        #title = results[t]['title_original']
        #title = title.append
    pass

breakpoint()

#print(response)
#print(parsed_response)
#print(my_cred)

#capture multiple inputs in a list until user types DONE; does not validate if it's a valid stock symbol
##while True:
#    #ask user for stock symbol
#    search = input("What topics are you looking to search")
#    symbol = symbol.upper()
#
#    if symbol == "DONE":
#        break
#    elif symbol.isalpha() and len(symbol) < 6:
#        #symbol = symbol.upper()
#        symbol_list.append(symbol.upper())
#    else:
#        print("Input must be A-Z characters only and less than or equal to 5 characters")
#
#create user input

#price = response.json()


