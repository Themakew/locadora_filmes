# -*- coding: utf-8 -*-
#import java.util.Enumeration;
#import java.util.Vector;
from Movie import Movie
from Allocation import Allocation
import itertools

children_rating = 2
regular_rating = 0
new_release = 1

class Client():
    name = None
    allocations_made = []

    def __init__(self, name):
        self.name = name
        self.allocations_made = []

    def add_new_allocation(self, movie_days_allocated): # art de tipo alocacao
        self.allocations_made.append(movie_days_allocated)

    def get_name(self):
        return self.name

    def calculate_price_of_the_allocation(self):
        total_quantity = 0.0
        total_price_of_the_movie_in_retal = 0.0
        allocation_frequency_point = 0
        allocations = iter(self.allocations_made)
        output_allocation_register = "\n" + "Registro de Locação para o usuário: " + self.get_name() + "\n"

        for location_type in allocations:
            price_of_the_movie_in_retal = 0.0

            location_type.calculate_price_of_the_movie_allocation()
            total_price_of_the_movie_in_retal += location_type.calculate_price_of_the_movie_allocation()

            #add frequent renter points
            allocation_frequency_point = allocation_frequency_point + 1

            #add bonus for a two-day lease for releases
            if location_type.getMovie().get_movie_rating() == Movie.new_release and location_type.get_movie_days_allocated() == 2:
                allocation_frequency_point = allocation_frequency_point + 1

            #show information for this allocation
            output_allocation_register = output_allocation_register + " " + location_type.getMovie().get_title() + " R$" + str(location_type.calculate_price_of_the_movie_allocation()) + "\n"

        #add footer report
        output_allocation_register = output_allocation_register + "\n" + "Quantia devida é R$" + str(total_price_of_the_movie_in_retal) + "\n"
        output_allocation_register = output_allocation_register + "Você ganhou " + str(allocation_frequency_point) + " pontos de locação." + "\n"
        return output_allocation_register

if __name__ == '__main__':
    ALLOCATED_DAYS_FIRST_MOVIE = 5
    ALLOCATED_DAYS_SECOND_MOVIE = 2
    ALLOCATED_DAYS_THIRD_MOVIE = 1

    my_client = Client('Ruben')
    #print my_client.get_name()

    movie_allocated = Movie('Titanic', 2)

    first_allocation = Allocation(movie_allocated, ALLOCATED_DAYS_FIRST_MOVIE)
    second_allocation = Allocation(movie_allocated, ALLOCATED_DAYS_SECOND_MOVIE)
    third_allocation = Allocation(movie_allocated, ALLOCATED_DAYS_THIRD_MOVIE)

    my_client.add_new_allocation(first_allocation)
    my_client.add_new_allocation(second_allocation)
    my_client.add_new_allocation(third_allocation)

    print(my_client.calculate_price_of_the_allocation())
