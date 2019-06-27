#podcast.py
#app to allow users to search for podcasts

import os
import requests
import json
import pprint
from dotenv import load_dotenv
import datetime
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

def format_date(timestamnp):
    new_timestamp = datetime.datetime.fromtimestamp(timestamp)
    new_timestamp = new_timestamp.strftime('%b %d %Y %H:%M:%S')
    return new_timestamp

#if __name__ == '__main__': 

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

results = []

results = list(parsed_response['results'])

#print(results[0])

if len(results) == 0:
    print("Your search returned 0 results. Please try again")
else:
    if len(results) == 1:
        print("You search returned " + str(parsed_response['count']) + " result")
    else: 
        print("You search returned " + str(parsed_response['count']) + " result")
print("-------------------")


for r in results:
    timestamp = r['pub_date_ms']
    title = r['title_original']
    podcast = r['podcast_title_original']

    timestamp = timestamp/1000.0

    #new_timestamp = format_date(timestamp)

    print(f"DATE: {format_date(timestamp)}")
    print(f"TITLE: {title}")
    print(f"DESCRIPTION: {podcast}")
    print("-------------------")



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


