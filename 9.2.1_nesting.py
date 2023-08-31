#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

#Nesting a List in a dictionary

travel_log = {

    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#List within a list nesting

["A", "B", ["C", "D"]]

#Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visted": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visted": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
}

#Nesting a dictionary in a list

travel_log = [    #travel_log contains two items, each being a dictionary
    #Each ditionary has 3 key:value pairs
    #first holds a string, second holds a list, third holds a number (int)
    {
    "country": "France", 
    "cities_visted": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {
     "country": "Germany",
     "cities_visted": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": 5
    },
]