"""

@author: Nichifor Dragos

"""

"""

A family wants to manage their monthly expenses. They need an application to store, for a given month, all 
their expenses. Each expense will be stored using the following elements: day (of the month in which it was 
made, between 1 and 30, for simplicity), amount of money (positive integer) and expense type (one of: housekeeping, 
food, transport, clothing, internet, others). Write a program that implements the functionalities exemplified below:

(A) Add a new expense
add <sum> <category>
insert <day> <sum> <category>
e.g.
add 10 internet – add to the current day an expense of 10 RON for internet
insert 25 100 food – insert to day 25 an expense of 100 RON for food

(B) Modify expenses
remove <day>
remove <start day> to <end day>
remove <category>
e.g.
remove 15 – remove all expenses for day 15
remove 2 to 9 – remove all expenses between days 2 and 9
remove food – remove all expenses for food

(C) Display expenses with different properties
list
list <category>
list <category> [ < | = | > ] <value>
e.g.
list – display all expenses
list food – display all the expenses for food
list food > 5 - display all food expenses with an amount of money >5
list internet = 44 - display all internet expenses with an amount of money =44

"""


# =============================================== CHECKERS ===============================================


def check_if_present(x, date, sum, type):
    """

    This function check wheater there is already an expense created by the applicationlike in the
    following example:

    if payment day: 10 sum: 8 type: internet exists

    and the user enters

    day: 10 sum: 3 type: internet

    we won't add a new expense, instead we will modify the sum to 8 + 3 = 11

    :param x: the list of expenses
    :param date: the date of the expense
    :param sum: the sum of the expense
    :param type: the type of the expense
    :return: True if there is an expense made with a determined category and day and False if there is not
    """

    for i in range(len(x)):
        if int(get_day(x[i])) == int(date) and get_expense_type(x[i]) == type:
            aux = int(get_amount_of_money(x[i]))
            aux += int(sum)
            set_amount_of_money(x[i], aux)
            return True
    return False


def check_if_date(date):
    """
    Checks if the date is valid

    :param date: the date
    :return: True if the date is valid and False if the date is invalid
    """

    date = int(date)
    if date < 1 or date > 30:
        return False
    return True


def check_expense(exp):
    """
    Checks if the expense entered by the user is valid

    :param exp: the expense
    :return: True if the expense is valid and False if the expense is invalid
    """

    if exp == 'housekeeping' or exp == 'transport' or exp == 'food' or exp == 'clothing' or exp == 'internet' or \
            exp == 'others':
        return True
    return False


# ====================================== GETTERS, SETTERS, CREATORS ======================================


def get_day(x):
    """
    Gets the day when expense 'x' was made

    :param x: the expense
    :return: the day the expense 'x' was made
    """

    return x['day']


def get_amount_of_money(x):
    """
    Gets the sum used to satisfy the expense 'x'
    :param x: the expense
    :return: the sum used to satisfy expense 'x'
    """

    return x['amount_of_money']


def get_expense_type(x):
    """
    Gets the type of the expense 'x'

    :param x: the expense
    :return: the type of expense 'x'
    """
    return x['expense_type']


def set_day(x, day):
    """
    Sets the day when expense 'x' was made

    :param x: the day when expense 'x' was made
    :param day: the expense
    :return:
    """

    x['day'] = day


def set_amount_of_money(x, amount):
    """
    Sets the sum used to satisfy the expense 'x'

    :param x: the sum used to satisfy the expense 'x'
    :param amount: the expense
    :return:
    """

    x['amount_of_money'] = amount


def set_expense_type(x, expense):
    """
    Sets the type of the expense 'x'

    :param x: the type of the expense 'x'
    :param expense: the expense
    :return:
    """

    x['expense_type'] = expense


def create_expense_specified_day(day, amount, expense):
    """
    Creates a new expense

    :param day: the day
    :param amount: the amount
    :param expense: the type of expense
    :return:
    """

    return {'day': day, 'amount_of_money': amount, 'expense_type': expense}


def create_expense_current_day(current, amount, expense):
    """
    Creates a new expense at a knew date

    :param current: current_day
    :param amount: the amount
    :param expense: the type of expense
    :return:
    """
    return {'day': current, 'amount_of_money': amount, 'expense_type': expense}


# ========================================== REMOVE FUNCTIONS ============================================


def remove_by_category(x, category):
    """
    Removes all expenses of a given category

    :param x: the list of expenses
    :param category: all the expenses with this category will be removed
    :return:
    """

    current = int(0)
    while current < len(x):
        if get_expense_type(x[current]) == category:
            x.pop(current)
            current -= 1
        current += 1


def remove_by_day(x, day):
    """
    Remove all expenses from a given day

    :param x: the list of expenses
    :param day: the day from which all expenses will be removed
    :return:
    """

    current = int(0)
    while current < len(x):
        if int(get_day(x[current])) == int(day):
            x.pop(current)
            current -= 1
        current += 1


def remove_between_days(x, start, end):
    """
    Remove all the expenses from the start day to the end day

    :param x: the list of expenses
    :param start: the start day
    :param end: the end day
    :return:
    """

    current = int(0)
    while current < len(x):
        if int(get_day(x[current])) >= int(start) and int(get_day(x[current])) <= int(end):
            x.pop(current)
            current -= 1
        current += 1


# ========================================== COMMAND FUNCTIONS ===========================================


def split_command(cmd):
    """
    Splits command into the command word and the list of parameters

    Ex: add 10 internet --> 'add' '10 internet'
        remove 10 to 20 --> 'remove' '10 to 20'

    :param cmd: the command
    :return: the command word and the parameters
    """

    cmd = cmd.strip()
    tokens = cmd.split(maxsplit=1)
    cmd_word = tokens[0].lower() if len(tokens) > 0 else None
    cmd_param = tokens[1].lower() if len(tokens) > 1 else None
    return cmd_word, cmd_param


def insert_command_run(current_day, params, x):
    """
    Adds a new expense at a given date of the month

    :param params: the parameters which will be split into: day, sum, type
    :param x: the list of expenses
    :return:
    """

    try:
        tokens = params.split(" ")
        tokens = [s.strip() for s in tokens]
        if len(tokens) == 3:
            tokens[0] = int(tokens[0])
            tokens[1] = int(tokens[1])
            if check_expense(tokens[2]) == False or check_if_date(tokens[0]) == False:
                raise ErrorValue
            if check_if_present(x, tokens[0], tokens[1], tokens[2]) == False:
                value = {'day': tokens[0], 'amount_of_money': tokens[1], 'expense_type': tokens[2]}
                x.append(value)
        else:
            raise ErrorValue
    except:
        print("Please enter a valid date, a valid sum and a valid type of expense")


def remove_command_run(current_day, params, x):
    """
    Removes all the expenses specified by the user

    :param params: the parameters which will be split into: day / day to day / category
    :param x: the list of expenses
    :return:
    """

    try:
        tokens = params.split(" ")
        tokens = [s.strip() for s in tokens]
        if (len(tokens) < 2):
            raise ErrorValue
        start = int(tokens[0])
        if tokens[1].lower() != "to" or len(tokens) == 2 or check_if_date(tokens[0]) == False or \
                check_if_date(tokens[2]) == False:
            print("Enter a valid date, 2 valid dates or a valid category")
            return
        end = int(tokens[2])
        if start > end:
            aux = start
            start = end
            end = aux
        remove_between_days(x, start, end)
    except:
        try:
            tokens[0] = int(tokens[0])
            day = tokens[0]
            if check_if_date(tokens[0]) == True:
                remove_by_day(x, day)
        except:
            try:
                if check_expense(tokens[0]) == False:
                    raise ErrorValue
                else:
                    category = tokens[0]
                    remove_by_category(x, category)
            except:
                print("Enter a valid date, 2 valid dates or a valid category")


def add_command_run(current_day, params, x):
    """
    Adds a new expense to the current day

    :param current_day: the current day
    :param params: the parameters which will be split: sum, type
    :param x: the list of expenses
    :return:
    """

    try:
        tokens = params.split(" ")
        tokens = [s.strip() for s in tokens]
        if len(tokens) == 2:
            tokens[0] = int(tokens[0])
            if check_expense(tokens[1]) == False:
                raise ErrorValue
            if check_if_present(x, current_day, tokens[0], tokens[1]) == False:
                value = {'day': current_day, 'amount_of_money': tokens[0], 'expense_type': tokens[1]}
                x.append(value)
        else:
            raise ErrorValue
    except:
        print("Please enter a valid sum and a valid type of expense")


def display_list_command_run(current_day, params, x):
    try:
        tokens = params.split(" ")
        tokens = [s.strip() for s in tokens]
        if len(tokens) == 1 and check_expense(tokens[0]) == True:
            display_by_category(x, tokens[0])
            return
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == "<":
            tokens[2] = int(tokens[2])
            display_by_value1(x, tokens[0], tokens[2])
            return
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == ">":
            tokens[2] = int(tokens[2])
            display_by_value2(x, tokens[0], tokens[2])
            return
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == "=":
            tokens[2] = int(tokens[2])
            display_by_value3(x, tokens[0], tokens[2])
            return
        if len(tokens) != 0:
            print("Please enter valid format")
            return
    except:
        display(x)


# =========================================== DISPLAY FUNCTIONS===========================================


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


# ============================================= UI FUNCTIONS =============================================


def display_expense(x):
    """
    Displays the expense in a more friendly way

    :param x: the list of expenses
    :return:
    """

    print("day:", get_day(x), "  amount of money:", get_amount_of_money(x), "  expense_type:", get_expense_type(x))


def read_current_date():
    """
    Read the current date

    :return:
    """

    current_day = None
    while current_day == None:
        current_day = input("Which is the current date? ")
        try:
            if int(current_day) < 1 or int(current_day) > 30:
                raise ErrorValue
        except:
            current_day = None
            print("Please enter a valid date\n")
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


# ================================================ TESTERS ================================================


def test_function(x):
    """
    The test function
    --> assert crashes if False, does nothing if True

    :return:
    """

    assert split_command('add 10 internet') == ('add', '10 internet')
    assert split_command('   ADD    230 internet   ') == ('add', '230 internet')
    assert split_command('insert 10 22 housekeeping') == ('insert', '10 22 housekeeping')
    assert split_command('inSERt          3 40 food') == ('insert', '3 40 food')
    assert split_command('remove internet') == ('remove', 'internet')
    assert split_command('list food') == ('list', 'food')
    assert split_command('list transport > 4') == ('list', 'transport > 4')
    insert_command_run(3, '10 10 internet', x)
    assert get_day(x[len(x) - 1]) == 10
    assert get_amount_of_money(x[len(x) - 1]) == 10
    assert get_expense_type(x[len(x) - 1]) == 'internet'
    add_command_run(10, '3 housekeeping', x)
    assert get_day(x[len(x) - 1]) == 10
    assert get_amount_of_money(x[len(x) - 1]) == 3
    assert get_expense_type(x[len(x) - 1]) == 'housekeeping'
    remove_command_run(3, '10', x)
    assert get_day(x[len(x) - 1]) == 1
    assert get_amount_of_money(x[len(x) - 1]) == 5
    assert get_expense_type(x[len(x) - 1]) == 'others'


# =========================================== UI START COMMAND ===========================================


def start_command_ui():
    """
    The base function that loops untill the user exits the aplication. The user can enter commands
    specified in the menu in order to realise different operations

    :return:
    """
    printmenu()

    begin()

    cmd_dict = {'add': add_command_run, 'remove': remove_command_run, 'insert': insert_command_run,
                'list': display_list_command_run}

    x = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 17, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    current_day = read_current_date()

    test_function(x)

    while True:
        cmd = input("The command is: ")
        if cmd.lower() == "exit":
            exit_function()
            break
        elif cmd.lower() == "menu":
            printmenu()
        else:
            cmd_word, cmd_params = split_command(cmd)
            if cmd_word not in cmd_dict:
                print("\nPlease enter a valid command\n")
            else:
                try:
                    cmd_dict[cmd_word](current_day, cmd_params, x)
                except ValueError as ve:
                    print("Please enter a valid atribute")


if __name__ == '__main__':
    """
    The main function
    """

    start_command_ui()
