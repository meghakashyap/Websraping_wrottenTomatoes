from Task4 import *
from Task1 import movie_data
from pprint import pprint

movie = movie_data
user = int(input("enter how many movie you want="))

def get_movie_list_details():
    movie_url = []
    movie_list = []
    i = 0
    while i <len(movie[:user]):
        movie_list.append(scrape_movie_details(movie_data[i]["Url"],movie_data[i]["Movie_Name"]))
        i+=1

    with open("task5.json","w+") as  movie_details:
        json.dump(movie_list,movie_details,indent = 4)
    
    return movie_list

movie_info = get_movie_list_details()
