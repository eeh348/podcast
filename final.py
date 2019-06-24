#final.py



def calculate_area(length, width):
    return length * width
    pass
    
area = calculate_area(4,2)

print(area)

breakpoint()

delivery = {
    "sender": "Charlie",
    "recipient": "Anika",
    "price": 16.99,
    "status": "in transit",
    "stops": ["New York", "Denver", "San Fran"]
}

print("A delivery from " + delivery['sender'] + " to " + delivery['recipient'])

stops = list(delivery['stops'])

books = [
    {'id':1, 'title':'Book A', 'color':'blue', 'year':1901},
    {'id':2, 'title':'Book B', 'color':'red', 'year':1957},
    {'id':3, 'title':'Book C', 'color':'blue', 'year':1988},
    {'id':4, 'title':'Book D', 'color':'green', 'year':1923},
    {'id':5, 'title':'Book E', 'color':'yellow', 'year':2017}
]

#matching_prods = [p for p in products if p["department"] == d]

[d["title"] for d in books]

[d["title"] for d in books if d["id"] == 4]

title = [d for d in books if d["id"] == 4]

teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

[team["name"] for team in teams if team["city"] == "Boston"] #> ['Yankees', 'Mets', 'Red Sox', 'Ravens']



breakpoint()

#for ids in books:
    #if books['id'] == 4
        #return title
    #pass

for s in stops:
    print(s)

