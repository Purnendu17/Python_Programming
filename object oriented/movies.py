class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def is_good(self):
        return self.rating > 7

movie = Movie("Interstellar", "Sci-Fi", 8.8)
print("Is the movie,",movie.name,"good?",movie.is_good())