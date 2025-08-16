
from movie import *
import pickle

def read_file(my_file):
    try :
        with open(my_file,'rb') as file:
            return pickle.load(file) 
    except (EOFError , FileNotFoundError):
        return []

 
def write_file(my_file,movie_list):
    with open(my_file,'wb') as file:
        pickle.dump(movie_list,file) 

