class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artist(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
            cls.genres.append(genre)
            converted_list_to_set = set(cls.genres)
            converted_set_to_list = list(converted_list_to_set)
            cls.genres = converted_set_to_list

    @classmethod
    def add_to_artist(cls, artist):
         cls.artists.append(artist)
         list_to_set = set(cls.artists)
         set_to_list = list(list_to_set)
         cls.artists = set_to_list 

    @classmethod
    def add_to_genre_count(cls, genre):
       if genre in cls.genre_count:
              cls.genre_count[genre] += 1
       else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
         if artist in cls.artist_count:
              cls.artist_count[artist] += 1
         else:
              cls.artist_count[artist] = 1
             
              
         
         
             