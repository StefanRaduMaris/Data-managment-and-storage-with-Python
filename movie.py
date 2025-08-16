


class Movie():
    def __init__(self,name,release_year,genre,imdb_address):
        self.name = name
        self.release_year = release_year
        self.genre = genre
        self.imdb_address = imdb_address

    def __str__(self):
        genre_str = ", ".join(self.genre)
        return f'Name : {self.name} \n Release year : {self.release_year} Type : {genre_str} \n IMDB : {self.imdb_address}'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str) and len(new_name) > 1 :
            self.__name = new_name
        else:
            raise TypeError('Name should be a string longer than 1 character')
        

    @property
    def year(self):
        return self.__release_year
    
    @year.setter
    def year(self,new_year):
        if isinstance(new_year,int) and new_year > 0:
            self.__release_year = new_year
        else:
            raise TypeError('Year must be a pozitive integer')
      

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, new_genre):
        if isinstance(new_genre, list) and all(isinstance(g, str) and len(g) > 0 for g in new_genre):
            self.__genre = new_genre
        else:
            raise TypeError("Genre must be a list of non-empty strings")
        

    @property
    def imdb(self):
        return self.__imdb_address
    
    @imdb.setter
    def imdb(self,new_imdb):
        if isinstance(new_imdb,str) and len(new_imdb) > 6 :
            self.__imdb_address = new_imdb
        else :
            raise TypeError("IMDB address must be a string longer than 6 characters")
        
    def display_info(self):
        print(self.__str__())

    @classmethod
    def add_new_movie(cls):
        while True:
            name = input("Movie name: ")
            try:
                if not isinstance(name, str) or len(name) < 2:
                    raise ValueError("Name must be at least 2 characters")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                year = int(input("Movie release year: "))
                if year <= 0:
                    raise ValueError("Year must be positive")
                break
            except ValueError as e:
                print(e)

        genres = []
        while True:
            g = input("Movie genre (Enter to finish): ")
            if g == "":
                break
            genres.append(g)

        while True:
            imdb = input("Movie IMDB link: ")
            if len(imdb) <= 6:
                print("IMDB link must be longer than 6 characters")
            else:
                break

        return cls(name, year, genres, imdb)