"""


@author: Nichifor Dragos


"""

from functions import get_day
from functions import get_amount_of_money
from functions import get_expense_type
from functions import split_params
from functions import add_command_run
from functions import insert_command_run
from functions import remove_command_run
from functions import display_list_command_run
from functions import sum_command_run
from functions import max_spent_command
from functions import sort_day_command
from functions import sort_category_command
from functions import check_expense
from functions import filter_command_run


# ============================================= UI FUNCTIONS =============================================


def read_current_date():
    """
    Read the current date

    :return:
    """

    current_day = None
    while current_day == None:
        current_day = input("Which is the current date? ")
        try:
            if current_day.isnumeric() == False:
                raise ValueError("The date should be a number from 1 to 30")
            if int(current_day) < 1 or int(current_day) > 30:
                raise ValueError("Please enter a valid date")
        except ValueError as ve:
            current_day = None
            print(ve)

    return current_day


def exit_function():
    """
    Prints quit message when the user exits the program

    :return:
    """

    print("\nQuiting...")


def begin():
    """
    The beginning of the program

    :return:
    """

    print("Please enter one of the instructions above! If you want to see the menu later use the "
          "command 'menu'\n")


def printmenu():
    """
    Prints the menu of the function

    :return:
    """

    print("\nadd     --> add <sum> <category>")
    print("insert     --> insert <day> <sum> <category>")
    print("remove     --> remove <day>  //  remove <start day> to <end day>  //  remove <category>")
    print("list     --> list  //  list <category>  //  list <category> [ < | = | > ] <value>\n")


# ========================================= UI COMMAND FUNCTIONS =========================================


def add_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of add_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        tokens = split_params(params)
        add_command_run(current_day, x, tokens)
        undo_op.append(x[:])
    except ValueError as ve:
        print(ve)


def insert_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of insert_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        tokens = split_params(params)
        insert_command_run(current_day, x, tokens)
        undo_op.append(x[:])
    except ValueError as ve:
        print(ve)


def remove_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of remove_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """
    try:
        tokens = split_params(params)
        remove_command_run(current_day, x, tokens)
        undo_op.append(x[:])
    except ValueError as ve:
        print(ve)


def display_list_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of display_list_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """
    try:
        if params != None:
            tokens = split_params(params)
        else:
            tokens = None
        command = display_list_command_run(current_day, x, tokens)
        if command == 1:
            display(x)
        if command == 2:
            display_by_category(x, tokens[0])
        if command == 3:
            display_by_value1(x, tokens[0], tokens[2])
        if command == 4:
            display_by_value2(x, tokens[0], tokens[2])
        if command == 5:
            display_by_value3(x, tokens[0], tokens[2])
    except ValueError as ve:
        print(ve)


def undo_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of undo_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        if len(undo_op) <= 1:
            raise ValueError("Cannot undo")
        x[:] = undo_op[len(undo_op) - 2]
        undo_op.pop(len(undo_op) - 1)
    except ValueError as ve:
        print(ve)


def sum_command_run_ui(current_day, undo_op, x, params):
    """
    The ui of sum_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        tokens = split_params(params)
        if len(tokens) != 1:
            raise ValueError("Please enter a valid command")
        sum_category = sum_command_run(x, tokens[0])
        print("The sum of", tokens[0], "expense is", sum_category)
    except ValueError as ve:
        print(ve)


def max_spent_command_ui(current_day, undo_op, x, params):
    """
    The ui of max_spent_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        tokens = split_params(params)
        if len(tokens) != 1:
            raise ValueError("Please enter a valid command")
        if tokens[0] == 'day':
            date = max_spent_command(x)
        else:
            raise ValueError("Please enter a valid date")
        for i in range(len(x)):
            if int(get_day(x[i])) == int(date):
                display_expense(x[i])
    except ValueError as ve:
        print(ve)


def sort_day_command_ui(current_day, undo_op, x, params):
    """
    The ui of sort_day_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        y = x[:]
        w = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30]
        tokens = split_params(params)
        if len(tokens) != 1:
            raise ValueError("Please enter a valid command")
        if tokens[0] == 'day':
            sort_day_command(y, w)
            display_2(y, w)
        else:
            if check_expense(tokens[0]) == False:
                raise ValueError("Please enter a valid command")
            sort_category_command(y, tokens[0])
            display(y)
    except ValueError as ve:
        print(ve)


def filter_command_ui(current_day, undo_op, x, params):
    """
    The ui of filter_command_run function

    :param current_day: the current day
    :param undo_op: the list of previous lists of expenses
    :param x: the current list of expenses
    :param params: the parameters
    :return:
    """

    try:
        tokens = split_params(params)
        if len(tokens) != 1 and len(tokens) != 3:
            raise ValueError("Please enter a valid command")
        if check_expense(tokens[0]) == False:
            raise ValueError("Please enter a valid category")
        filter_command_run(x, tokens)
        undo_op.append(x[:])
    except ValueError as ve:
        print(ve)


# ========================================= SORT DISPLAY FUNCTIONS========================================


def display_2(y, w):
    """
    Displays the total sum spent in each day

    :param y: The list of total expenses per day
    :param w: The list of expenses
    :return:
    """

    for i in range(len(y)):
        if y[i] != 0:
            print("The expense for day", w[i], "is", y[i])


# =========================================== DISPLAY FUNCTIONS===========================================


def display_expense(x):
    """
    Displays the expense in a more friendly way

    :param x: the list of expenses
    :return:
    """

    print("day:", get_day(x), "  amount of money:", get_amount_of_money(x), "  expense_type:", get_expense_type(x))


def display(x):
    """
    Displays all the expenses

    :param x: the list of expenses
    :return:
    """

    if len(x) == 0:
        print("The list has no elements")
    for i in range(len(x)):
        display_expense(x[i])


def display_by_category(x, category):
    """
    Displays all the expenses of a specified category

    :param x: the list of expenses
    :param category: all the expenses with this category will be displayed
    :return:
    """

    ok = 0
    for i in range(len(x)):
        if get_expense_type(x[i]) == category:
            display_expense(x[i])
            ok = 1
    if ok == 0:
        print("The list has no elements")


def display_by_value1(x, category, val):
    """
    Displays all the expenses of a specified category less than a given number

    :param x: the list of expenses
    :param category: category: all the expenses with this category will be displayed
    :param val: the number
    :return:
    """

    ok = 0
    for i in range(len(x)):
        if get_expense_type(x[i]) == category and int(get_amount_of_money(x[i])) < int(val):
            display_expense(x[i])
            ok = 1
    if ok == 0:
        print("The list has no elements")


def display_by_value2(x, category, val):
    """
    Displays all the expenses of a specified category higher than a given number

    :param x: the list of expenses
    :param category: category: all the expenses with this category will be displayed
    :param val: the number
    :return:
    """

    ok = 0
    for i in range(len(x)):
        if get_expense_type(x[i]) == category and int(get_amount_of_money(x[i])) > int(val):
            display_expense(x[i])
            ok = 1
    if ok == 0:
        print("The list has no elements")


def display_by_value3(x, category, val):
    """
    Displays all the expenses of a specified category equal to a given number

    :param x: the list of expenses
    :param category: category: all the expenses with this category will be displayed
    :param val: the number
    :return:
    """

    ok = 0
    for i in range(len(x)):
        if get_expense_type(x[i]) == category and int(get_amount_of_money(x[i])) == int(val):
            display_expense(x[i])
            ok = 1
    if ok == 0:
        print("The list has no elements")


def test_function_ui():

    x = [{'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'}]

    undo_op = [[{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'}],
               [{'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
                {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'}]]

    undo_command_run_ui(10, undo_op, x, 'a')

    assert x == [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                 {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'}]

    undo_op = [[{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'}],
               [{'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
                {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'}],
               [{'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
                {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'}]]

    undo_command_run_ui(10, undo_op, x, 'a')

    assert x == [{'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
                 {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'}]
