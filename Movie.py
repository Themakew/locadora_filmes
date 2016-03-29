# -*- coding: utf-8 -*-

class Movie:

    children_rating = 2
    regular_rating = 0
    new_release = 1
    movie_title = None
    price_of_the_movie = None

    def __init__(self, movie_title, price_of_the_movie):
        self.movie_title = movie_title
        self.price_of_the_movie = price_of_the_movie

    def get_movie_rating(self):
        return self.price_of_the_movie

    def set_code_price(self, price_of_the_movie):
        self.price_of_the_movie = price_of_the_movie

    def get_title(self):
        return self.movie_title

if __name__ == '__main__':
    my_movie = Movie('titanic', 3)
