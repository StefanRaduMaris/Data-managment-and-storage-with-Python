

movie_list = []

class movie():
    def __init__(self,name,release_year,genre,imdb_address):
        self.__name = name
        self.__release_year = release_year
        self.__genre = genre
        self.__imdb_address = imdb_address

    def __str__(self):
        return f'Name : {self.__name} Release year : {self.__release_year} Type : {self.__genre} \n IMDB : {self.__imdb_address}'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str) and len(new_name) > 1 :
            self.__name = new_name
        else:
            raise TypeError('Name should be a string longer than 1 character')
        return self.__name

    @property
    def year(self):
        return self.__release_year
    
    @year.setter
    def year(self,new_year):
        if isinstance(new_year,int) and new_year > 0:
            self.__release_year = new_year
        else:
            raise TypeError('Year must be a pozitive integer')
        return self.__release_year        

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self,new_genre):
        if isinstance(new_genre,str) and len(new_genre) > 1:
            self.__genre = new_genre
        else:
            raise TypeError("Gender must be a string longer than 1 character")
        return self.genre

    @property
    def imdb(self):
        return self.__imdb_address
    
    @imdb.setter
    def imdb(self,new_imdb):
        if isinstance(new_imdb,str) and len(new_imdb) > 6 :
            self.__imdb_address = new_imdb
        else :
            raise TypeError("IMDB address must be a string longer than 6 characters")
        return self.__imdb_address
    
    def add_movie(self):
        movie_name = input("Movie name :")
        movie_year = input("Movie release year:")
        movie_genre = input("Movie Gender:")
        movie_imdb_address = input("Movie imdb link :")
        new_movie = movie(movie_name , movie_year , movie_genre, movie_imdb_address)
        movie_list.append(new_movie)

        
    
    def display_info(self):
        return print(self.__str__())
