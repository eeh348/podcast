#podcast.py
#app to allow users to search for podcasts

import os
import requests
import json
import pprint
import datetime as dt
import PySimpleGUI as sg

from dotenv import load_dotenv

#capture keys
list_string = []
new_search = []

#define fonts
font = ('Veranda', 12)

#define functions
def format_search(search):
    list_string = search.split()
    new_search = '%20'.join(list_string)
    return new_search

def format_date(timestamnp):
    new_timestamp = dt.datetime.fromtimestamp(timestamp)
    new_timestamp = new_timestamp.strftime('%b %d %Y')
    return new_timestamp

def format_dur(len):
    new_len = round(len/60)
    return new_len
           
#if __name__ == '__main__':

load_dotenv()
my_cred = os.environ.get("X_LISTEN_API_KEY")

#build search GUI - adapted from https://pysimplegui.readthedocs.io/en/latest/tutorial/#the-5-minute-gui
while True:

    layout = [      
            [sg.Text('Please search on a podcast name, episdoe or topic')],      
            [sg.Text('Search', size=(15, 1)), sg.InputText()],          
            [sg.Submit("Search"), sg.Exit()]      
            ]

    window = sg.Window('Search Podcasts', layout, font='Veranda')       
    event, values = window.Read()
    search = values[0]

    #display processing message
    if event is None or event == 'Exit':
        break
    elif search == "":
        sg.Popup('Your input was blank. Please search a topic:')
        window = sg.Window('Search Podcasts', layout)       
        event, values = window.Read()
    else:
        window.Close()
        sg.Popup(f'Searching on {search}... ', font='Veranda')
        break

#format user input  
new_search = format_search(search)

#fetch data
request_url = f"https://listen-api.listennotes.com/api/v2/search?q={new_search}&sort_by_date=0&scope=episode&offset=0&len_min=10&len_max=100&published_before=0&published_after=1390190241000&only_in=title%2Cdescription%20author&language=English&safe_mode=1"
response = requests.get(request_url, headers={"X-ListenAPI-Key": my_cred})
parsed_response = json.loads(response.text)

results = []

results = list(parsed_response['results'])

#build output - adapted from https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegu

#check to make sure results aren't blank
if len(results) == 0:
    result_msg = 'Your search returned 0 results. Please try again'
else:
    if len(results) == 1:
        result_msg = 'You search returned ' + str(parsed_response['count']) + ' result'
    else: 
        result_msg = 'You search returned ' + str(parsed_response['count']) + ' results'

#sort list on release date - adapted from https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
sorted_results = sorted(results, key = lambda i: i['pub_date_ms'],reverse=True)

#create list of dictionaries for results
podcast_results = []

#print results
for r in sorted_results:

    timestamp = r['pub_date_ms']
    title = r['title_original']
    podcast = r['podcast_title_original']
    audio = r['audio']
    length = r['audio_length_sec']
    thumbnail = r['thumbnail']

    timestamp = timestamp/1000.0

    new_time = format_date(timestamp)

    print(f"PUB DATE: {format_date(timestamp)}")
    print(f"PODCAST TITLE: {title}")
    print(f"PODCAST NAME: {podcast}")
    print(f"DURATION: {format_dur(length)} MINS")
    print("-------------------")

