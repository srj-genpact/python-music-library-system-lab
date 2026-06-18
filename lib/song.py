class Song:
    # Class attributes to maintain global statistics across all song instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    # Alias attribute to support test suite which references artist_count
    artist_count = {}

    def __init__(self, name, artist, genre):
        """
        Initializes a new instance of the Song class.
        
        Args:
            name (str): The name of the song.
            artist (str): The artist who performed the song.
            genre (str): The genre of the song.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger each class method upon instantiating a new song
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """
        Increments the total count of songs by 1.
        """
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds a new genre to the unique genres list.
        Ensures there are no duplicates.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds a new artist to the unique artists list.
        Ensures there are no duplicates.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Increments the song count for the specified genre in genre_count.
        Initializes the genre count to 1 if it doesn't exist.
        """
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Increments the song count for the specified artist in both artists_count
        and the alias artist_count.
        Initializes the artist count to 1 if it doesn't exist.
        """
        # Update artists_count
        if artist not in cls.artists_count:
            cls.artists_count[artist] = 0
        cls.artists_count[artist] += 1

        # Update artist_count (alias for compatibility with pytest)
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1
