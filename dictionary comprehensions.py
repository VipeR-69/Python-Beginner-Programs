# dictionary comprehensions - create dictionaries using an expression
#                             can replace for loops and certain lambda functions.
# SYNTAX -
#    dictionary = { key : expression for (key,value) in iterable }
#    dictionary = { key : expression for (key,value) in iterable if conditional }
#    dictionary = { key : (if/else) for (key,value) in iterable }
#    dictionary = { key : function(value) for (key,value) in iterable }


cities_f = {"New York":32 , "Boston":75 , "Los Angeles":100 , "Chicago":50 }

cities_c = {key : round((value-32)*5/9) for (key,value) in cities_f.items()}
print(cities_c)

#####################################################################################

weather = {"New York":"Snowing" , "Boston":"Sunny" , "Los Angeles":"Sunny" , "Chicago":"Cloudy"}

sunny_weather = {key : value for (key,value) in weather.items() if value == "Sunny"}
print(sunny_weather)

#######################################################################################

cities = {"New York":32 , "Boston":75 , "Los Angeles":100 , "Chicago":50 }

desc_cities = {key : ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

#######################################################################################

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York":32 , "Boston":75 , "Los Angeles":100 , "Chicago":50 }

desc_cities = {key : check_temp(value) for (key,value) in cities.items()}
print(desc_cities)