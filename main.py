

from movie import *

def main():
    while answer != '3' :
        answer = input("Choose what you will like to do : \n 1. Add new movie \n 2.Display movie list /n 3.Close the program")
        
        if answer == '1':
            movie_list.add_movie()

        elif answer == '2':
            movie_list.display_info()

        elif answer == '3':
            break

if __name__ == "__main__":
    main()
