# -*- coding: utf-8 -*-
from Movie import Movie

class Allocation:

    def __init__(self, movie, movie_days_allocated): #movie type: Movie
        self.movie = movie #movie type
        self.movie_days_allocated = movie_days_allocated

    def get_movie_days_allocated(self):
        return self.movie_days_allocated

    def getMovie(self):
        return self.movie

    def calculate_price_of_the_movie_allocation(self):
        price_of_the_movie_in_retal = 0.0

        if self.getMovie().get_movie_rating() == self.getMovie().regular_rating:
            price_of_the_movie_in_retal = price_of_the_movie_in_retal + 2
            if self.get_movie_days_allocated() > 2:
                price_of_the_movie_in_retal = price_of_the_movie_in_retal + (self.get_movie_days_allocated() - 2) * 1.5
        elif self.getMovie().get_movie_rating() == self.getMovie().new_release:
            price_of_the_movie_in_retal = price_of_the_movie_in_retal + 3
        elif self.getMovie().get_movie_rating() == self.getMovie().children_rating:
            price_of_the_movie_in_retal = price_of_the_movie_in_retal + 1.5
            if self.get_movie_days_allocated() > 3:
                price_of_the_movie_in_retal = price_of_the_movie_in_retal + (self.get_movie_days_allocated() - 3) * 1.5
        return price_of_the_movie_in_retal

if __name__ == '__main__':
    my_allocation = Allocation()
