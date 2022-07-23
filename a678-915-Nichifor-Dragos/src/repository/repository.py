"""


@author: Nichifor Dragos


"""


class RepositoryMovies:
    def __init__(self):
        self.__movies = []

    def add_mov(self, obj):
        """
        Adds a movie to the movie repository

        :param obj: the movie object
        :return:
        """

        for i in range(len(self.__movies)):
            k = self.__movies[i]
            if k.id == obj.id:
                raise ValueError("The id", obj.id, "is already in repo")
        self.__movies.append(obj)

    def remove_mov(self, obj):
        """
        Removes a movie from the movie repository

        :param obj: the movie object
        :return:
        """

        self.__movies.remove(obj)

    def update_mov_title(self, obj, title):
        """
        Update's a movie title

        :param obj: the movie object
        :param title: the new title
        :return:
        """

        for i in range(len(self.__movies)):
            k = self.__movies[i]
            if k.id == obj.id:
                self.__movies[i].title = title

    def update_mov_description(self, obj, description):
        """
        Updates a movie description

        :param obj: the movie object
        :param description: the new description
        :return:
        """

        for i in range(len(self.__movies)):
            k = self.__movies[i]
            if k.id == obj.id:
                self.__movies[i].description = description

    def update_mov_genre(self, obj, genre):
        """
        Updates a movie genre

        :param obj: the movie object
        :param genre: the new genre
        :return:
        """

        for i in range(len(self.__movies)):
            k = self.__movies[i]
            if k.id == obj.id:
                self.__movies[i].genre = genre

    def return_list_movies(self):
        """
        Returns the list of movies

        :return:
        """

        return self.__movies


class RepositoryClients:
    def __init__(self):
        self.__clients = []

    def add_cl(self, obj):
        """
        Adds a new client to the client repository

        :param obj: the client object
        :return:
        """

        for i in range(len(self.__clients)):
            k = self.__clients[i]
            if k.client_id == obj.client_id:
                raise ValueError("The id", obj.client_id, "is already in repo")
        self.__clients.append(obj)

    def remove_cl(self, obj):
        """
        Removes a client from the client repository

        :param obj: the client object
        :return:
        """

        self.__clients.remove(obj)

    def update_cl(self, obj, name):
        """
        Updates a client name

        :param obj: the client object
        :param name: the new name
        :return:
        """

        for i in range(len(self.__clients)):
            k = self.__clients[i]
            if k.client_id == obj.client_id:
                self.__clients[i].name = name

    def return_list_clients(self):
        """
        Returns the list of clients

        :return:
        """
        return self.__clients


class RepositoryRentals:
    def __init__(self):
        self.__rentals = []

    def add_rental(self, obj):
        """
        Adds a new rental to the rental repository

        :param obj: the rental object
        :return:
        """

        self.__rentals.append(obj)

    def update_renturned_date(self, obj, current_date):
        """
        Updates the return date of a rental

        :param obj: the rental object
        :param current_date: the return date
        :return:
        """

        for i in range(len(self.__rentals)):
            if self.__rentals[i].rent_id == obj.rent_id:
                self.__rentals[i].returned_date = current_date

    def remove_borrow(self, obj):
        self.__rentals.remove(obj)

    def return_list_rentals(self):
        """
        Returns the list of rentals

        :return:
        """

        return self.__rentals
