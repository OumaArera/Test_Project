#Our list
travel_log = [
    {
        "Country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

#we define a function and assign it three parameters
def add_new_country(name, no_of_visits,cities_visited):

    #create an empty dictionary
    #so that we can add new arguments to it
    new_country = {}

    new_country["Country"] = name
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_visited

    # print(new_country)
    #We add the new_country dictionary to travel_log
    #using append() method
    travel_log.append(new_country)

#Calling the function
add_new_country("Brazil", 5, ["Saol Paulo", "Rio de Janeiro", "Salvador"])

print(travel_log)

