"""

@author: Nichifor Dragos





Write an application for movie rentals. The application will store:

Movie: movie_id, title, description, genre
Client: client_id, name
Rental: rental_id, movie_id, client_id, rented_date, due_date, returned_date
Create an application which allows to:

--> Manage clients and movies. The user can add, remove, update, and list both clients and movies.

--> Rent or return a movie. A client can rent a movie until a given date, as long as they have no rented movies
that passed their due date for return. A client can return a rented movie at any time.

--> Search for clients or movies using any one of their fields (e.g. movies can be searched for using id, title,
description or genre). The search must work using case-insensitive, partial string matching, and must return all
matching items.

Create statistics:

<> Most rented movies. This will provide the list of movies, sorted in descending order of the number of days they were
rented.
<> Most active clients. This will provide the list of clients, sorted in descending order of the number of movie rental
days they have (e.g. having 2 rented movies for 3 days each counts as 2 x 3 = 6 days).
<> Late rentals. All the movies that are currently rented, for which the due date for return has passed, sorted in
descending order of the number of days of delay.
<> Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo
operations must cascade and have a memory-efficient implementation (no superfluous list copying).

"""
from src.domain.validators import ClientValidator, MovieValidator, RentalValidator
from src.repository.repository import RepositoryRentals, RepositoryClients, RepositoryMovies
from src.services.services import ServicesRentals, ServicesClients, ServicesMovies
from src.ui.ui import UI
from src.ui.gui import GUI


def check_option(cmd):
    if cmd != 1 and cmd != "1" and cmd != 2 and cmd != "2":
        raise ValueError("\nPlease enter a valid command\n")


def print_menu():
    print("\n1 - Start with UI")
    print("2 - Start with GUI")


if __name__ == '__main__':
    client_validator = ClientValidator
    repository_clients = RepositoryClients()
    service_clients = ServicesClients(repository_clients, client_validator)

    movie_validator = MovieValidator
    repository_movies = RepositoryMovies()
    service_movies = ServicesMovies(repository_movies, movie_validator)

    rental_validator = RentalValidator
    repository_rentals = RepositoryRentals()
    service_rentals = ServicesRentals(repository_rentals, rental_validator)

    # print_menu()
    #
    # while True:
    #     try:
    #         cmd = input("\nYour command: ")
    #         check_option(cmd)
    #         if cmd == "1" or cmd == 1:
    #             st = UI(service_clients, service_movies, service_rentals)
    #             st.start_ui()
    #             break
    #         if cmd == "2" or cmd == 2:
    #             st = GUI(service_clients, service_movies, service_rentals)
    #             st.start_gui()
    #             break
    #     except ValueError as ve:
    #         print(ve)

    st = UI(service_clients, service_movies, service_rentals)
    st.start_ui()
