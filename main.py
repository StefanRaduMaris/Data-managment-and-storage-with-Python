

from movie import *
import os
import pickle
from file_creator import *

movies = []

def main():
    
    answer = 'start'
    while answer != '3' :
        answer = input("Choose what you will like to do : \n 1. Add new movie \n 2.Display movie list \n 3.Close the program \n")
        
        if answer == '1':
           
            
            new_movie = Movie.add_new_movie()
            movies.append(new_movie)
            write_file(r'C:\Users\Fane\Desktop\curs python\Data-managment-and-storage-with-Python\movie.txt',movies)

        elif answer == '2':
           for movie in movies:
                movie.display_info()

        elif answer == '3':
            print('Goodbye')
            break

if __name__ == "__main__":
    
    
    movies = read_file(r'C:\Users\Fane\Desktop\curs python\Data-managment-and-storage-with-Python\movie.txt')
    main()
