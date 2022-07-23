"""

@author: Nichifor Dragos

"""

import datetime
import random

from src.domain.validators import MovieException, ClientException, RentalException
from src.services.undo import UndoRedoManager

from tkinter import *
import pyautogui


class GUI:
    def __init__(self, service_clients, service_movies, service_rentals):
        self.__service_clients = service_clients
        self.__service_movies = service_movies
        self.__service_rentals = service_rentals
        self.__frame = Tk()
        self.__frame.geometry('900x600')
        self.__frame.title("Client/Movie/Rental manager")
        self.__frame.configure(background='black')

    @staticmethod
    def print_menu():
        label1 = Label(text="\n\n\n1 - Add a client/movie\n2 - Remove a client/movie\n3 - Update a client/movie\n4 - "
                            "List both clients and movies\n5 - Borrow/return a movie\n6 - Create statistics\n7 - "
                            "Search a client/movie\n8 - Undo operation\n9 - Redo operation\nx - Exit\n", fg='white',
                       bg='black', font=("Times new roman", 15))
        label1.pack()

    @staticmethod
    def read_command():
        pass

    def start_gui(self):
        self.__service_movies.add_begin_movies()
        self.__service_clients.add_begin_clients()
        self.start_window()

    def start_window(self):
        btn_menu = Button(self.__frame, text="Print menu", height=2, command=self.print_menu)
        btn_command = Button(self.__frame, text="New Command", command=self.read_command())
        btn_exit = Button(self.__frame, text="Exit", command=exit)
        btn_menu.pack(side=TOP)
        btn_exit.pack(side=BOTTOM)
        btn_command.pack(side=BOTTOM)
        Tk.mainloop(self.__frame)
