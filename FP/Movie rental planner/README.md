## Requirements
- Your program must provide a menu-driven console-based user interface.
- Implementation must employ layered architecture and classes.
- Have at least 20 procedurally generated items in your application at startup.
- Provide specification and tests for all non-UI classes and methods for the first functionality.
- Implement and use your own exception classes.
- Implement **PyUnit test cases**
- Implement persistent storage for all entities using file-based repositories. Also implement a `settings.properties` file to configure your application.
- You must implement two additional repository sets: one using text files for storage, and one using binary files (e.g. using object serialization with [Pickle](https://docs.python.org/3.8/library/pickle.html)).
- The program must work the same way using in-memory repositories, text-file repositories and binary file repositories.
- The decision of which repositories are employed, as well as the location of the repository input files will be made in the program’s `settings.properties` file.
- Create a Python module that contains an iterable data structure, a sort method and a filter method, together with complete PyUnit unit tests (100% coverage). The     module must be reusable in other projects.
- Implement an iterable data structure. Study the [`__setItem__`](https://docs.python.org/3/reference/datamodel.html#object),`__getitem__`, `__delItem__`, `__next__` and `__iter__` Python methods.
- Implement a sorting algorithm. You can use one of shell sort, comb sort, bingo sort, gnome sort, or other sorting method. The sort function will accept two parameters: the list to be sorted as well as a comparison function used to determine the order between two elements.
- Implement a filter function that can be used to filter the elements from a list. The function will use 2 parameters: the list to be filtered, and an acceptance function that decided whether a given value passes the filter.

## Movie Rental
Write an application for movie rentals. The application will store:
- **Movie**: `movie_id`, `title`, `description`, `genre`
- **Client**: `client_id`, `name`
- **Rental**: `rental_id`, `movie_id`, `client_id`, `rented_date`, `due_date`, `returned_date`

Create an application which allows to:
1. Manage clients and movies. The user can add, remove, update, and list both clients and movies.
2. Rent or return a movie. A client can rent a movie until a given date, as long as they have no rented movies that passed their due date for return. A client can return a rented movie at any time.
3. Search for clients or movies using any one of their fields (e.g. movies can be searched for using id, title, description or genre). The search must work using case-insensitive, partial string matching, and must return all matching items.
4. Create statistics:
    - Most rented movies. This will provide the list of movies, sorted in descending order of the number of days they were rented.
    - Most active clients. This will provide the list of clients, sorted in descending order of the number of movie rental days they have (e.g. having 2 rented movies for 3 days each counts as 2 x 3 = 6 days).
    - Late rentals. All the movies that are currently rented, for which the due date for return has passed, sorted in descending order of the number of days of delay.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying).
