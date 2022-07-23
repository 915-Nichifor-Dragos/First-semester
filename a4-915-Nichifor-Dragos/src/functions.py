"""


@author: Nichifor Dragos


"""


# =========================================== SPLIT FUNCTIONS ============================================


def split_params(params):
    """
    Splits the string of parameters in different words inside a list

    :param params: the string of parameters
    :return:
    """

    try:
        tokens = params.split(" ")
        tokens = [s.strip() for s in tokens]
        return tokens
    except:
        raise ValueError("Please enter a valid operation")


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


# ========================================== COMMAND FUNCTIONS ===========================================


def insert_command_run(current_day, x, tokens):
    """
    Adds a new expense at a given date of the month

    :param tokens: the parameters string split into words and stored inside a list
    :param x: the list of expenses
    :return:
    """

    try:
        if len(tokens) == 3:
            tokens[0] = int(tokens[0])
            tokens[1] = int(tokens[1])
            if check_expense(tokens[2]) == False or check_if_date(tokens[0]) == False:
                raise ValueError("Please enter a valid expense type")
            if check_if_present(x, tokens[0], tokens[1], tokens[2]) == False:
                value = {'day': tokens[0], 'amount_of_money': tokens[1], 'expense_type': tokens[2]}
                x.append(value)
        else:
            raise ValueError("Please enter a valid day, a valid sum or a valid expense type")
    except:
        raise ValueError("Please enter a valid day, a valid sum or a valid expense type")


def remove_command_run(current_day, x, tokens):
    """
    Removes all the expenses specified by the user

    :param tokens: the parameters string split into words and stored inside a list
    :param x: the list of expenses
    :return:
    """

    try:
        if (len(tokens) < 2):
            raise ValueError("Please enter a valid command")
        start = int(tokens[0])
        if tokens[1].lower() != "to" or len(tokens) == 2 or check_if_date(tokens[0]) == False or \
                check_if_date(tokens[2]) == False:
            raise ValueError("Enter a valid date, 2 valid dates or a valid category")
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
                    raise ValueError("Please enter a valid command")
                else:
                    category = tokens[0]
                    remove_by_category(x, category)
            except:
                print("Enter a valid date, 2 valid dates or a valid category")


def add_command_run(current_day, x, tokens):
    """
    Adds a new expense to the current day

    :param current_day: the current day
    :param tokens: the parameters string split into words and stored inside a list
    :param x: the list of expenses
    :return:
    """

    try:
        if len(tokens) == 2:
            tokens[0] = int(tokens[0])
            if check_expense(tokens[1]) == False:
                raise ValueError("Please enter a valid expense type")
            if check_if_present(x, current_day, tokens[0], tokens[1]) == False:
                value = {'day': current_day, 'amount_of_money': tokens[0], 'expense_type': tokens[1]}
                x.append(value)
        else:
            raise ValueError("Please enter a valid sum and a valid expense type")
    except:
        print("Please enter a valid sum and a valid type of expense")


def display_list_command_run(current_day, x, tokens):
    """
    Returns the type of display the user wants the program to do

    :param current_day: the current day
    :param x: the list of expenses
    :param tokens: the parameters string split into words and stored inside a list
    :return:
    """
    try:
        if tokens == None:
            return 1
        if len(tokens) == 1 and check_expense(tokens[0]) == True:
            return 2
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == "<":
            return 3
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == ">":
            return 4
        if len(tokens) == 3 and check_expense(tokens[0]) == True and tokens[1] == "=":
            return 5
        raise ValueError("Please enter a valid format")
    except:
        raise ValueError("Please enter a valid format")


def sum_command_run(x, category):
    """
    Computes the total sum of one category of expense

    :param x: the list of expenses
    :param category: the category that the user wants the total monthly expense for
    :return:
    """

    try:
        sum_category = 0
        if check_expense(category) == False:
            raise ValueError("Please enter a valid category")
        for i in range(len(x)):
            if get_expense_type(x[i]) == category:
                sum_category += get_amount_of_money(x[i])
        return sum_category
    except:
        raise ValueError("Please enter a valid command")


def max_spent_command(x):
    """
    Returns the date in which the biggest sum of money was used

    :param x: the list of expenses
    :return:
    """

    try:
        sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(x)):
            sum[int(get_day(x[i]))] += get_amount_of_money(x[i])
        max_sum = 0
        pos = 0
        for i in range(len(sum)):
            if sum[i] > max_sum:
                max_sum = sum[i]
                pos = i
        return pos
    except:
        ValueError("Please enter a valid command")


def sort_day_command(y, w):
    """
    Computes the total daily expenses in ascending order by amount of money spent

    :param y: the list of expenses
    :param w: the list of days
    :return:
    """

    try:
        sum = do_sum_of_days(y)
        y.clear()
        y[:] = sum
        for i in range(len(y)):
            for j in range(i, len(y)):
                if (y[j] < y[i]):
                    aux1 = y[i]
                    aux2 = w[i]
                    y[i] = y[j]
                    w[i] = w[j]
                    y[j] = aux1
                    w[j] = aux2
    except:
        ValueError("Please enter a valid command")


def sort_category_command(y, category):
    """
    Computes the daily expenses for a given category in ascending order by amount of money spent

    :param y: the list of expenses
    :param category: the category we compute for
    :return:
    """

    try:
        current = 0
        while current < len(y):
            if get_expense_type(y[current]) != category:
                y.remove(y[current])
                current -= 1
            current += 1
        sort_category(y)
    except:
        ValueError("Please enter a valid category")


def filter_command_run(x, tokens):
    """
    Modifies the list using different given filters

    :param x: the list of expenses
    :param tokens: the parameters string split into words and stored inside a list
    :return:
    """

    try:
        if len(tokens) == 1:
            filter_command_1(x, tokens[0])
        else:
            tokens[2] = int(tokens[2])
            if tokens[1] == '<':
                filter_command_2(x, tokens[0], tokens[2])
            if tokens[1] == '>':
                filter_command_3(x, tokens[0], tokens[2])
            if tokens[1] == '=':
                filter_command_4(x, tokens[0], tokens[2])

    except:
        ValueError("Please enter a valid command")


# =========================================== FILTER FUNCTIONS ===========================================


def filter_command_1(x, category):
    """
    Filters the list and keeps the expenses in the given 'category'

    :param x: the list of parameters
    :param category: the category given
    :return:
    """

    current = 0
    while current < len(x):
        if get_expense_type(x[current]) != category:
            x.remove(x[current])
            current -= 1
        current += 1


def filter_command_2(x, category, sum):
    """
    Filters the list and keeps the expenses in the given 'category' that are less than a given value

    :param x: the list of parameters
    :param category: the category given
    :return:
    """

    current = 0
    while current < len(x):
        if get_expense_type(x[current]) != category:
            x.remove(x[current])
            current -= 1
        current += 1
    current = 0
    while current < len(x):
        if get_amount_of_money(x[current]) >= sum:
            x.remove(x[current])
            current -= 1
        current += 1


def filter_command_3(x, category, sum):
    """
    Filters the list and keeps the expenses in the given 'category' that are more than a given value

    :param x: the list of parameters
    :param category: the category given
    :return:
    """

    current = 0
    while current < len(x):
        if get_expense_type(x[current]) != category:
            x.remove(x[current])
            current -= 1
        current += 1
    current = 0
    while current < len(x):
        if get_amount_of_money(x[current]) <= sum:
            x.remove(x[current])
            current -= 1
        current += 1


def filter_command_4(x, category, sum):
    """
    Filters the list and keeps the expenses in the given 'category' that are equal than a given value

    :param x: the list of parameters
    :param category: the category given
    :return:
    """

    current = 0
    while current < len(x):
        if get_expense_type(x[current]) != category:
            x.remove(x[current])
            current -= 1
        current += 1
    current = 0
    while current < len(x):
        if get_amount_of_money(x[current]) > sum or get_amount_of_money(x[current]) < sum:
            x.remove(x[current])
            current -= 1
        current += 1


# ============================================ SORT FUNCTIONS ============================================


def sort_category(y):
    """
    Sorts the expenses of a list in ascending order by the amount of money used

    :param y: the list of expenses
    :return:
    """

    try:
        for i in range(len(y)):
            for j in range(i, len(y)):
                if get_amount_of_money(y[i]) > get_amount_of_money(y[j]):
                    aux = y[i]
                    y[i] = y[j]
                    y[j] = aux
    except:
        ValueError("Please enter a valid command")


def do_sum_of_days(y):
    """
    Computes the money used for expenses during every single day

    :param y: the list of expenses
    :return:
    """

    try:
        sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(y)):
            sum[int(get_day(y[i]))] += get_amount_of_money(y[i])
        return sum
    except:
        ValueError("Please enter a valid command")


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
-
    :param current: current_day
    :param amount: the amount
    :param expense: the type of expense
    :return:
    """
    return {'day': current, 'amount_of_money': amount, 'expense_type': expense}


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
        raise ValueError("Please enter a valid date")


def check_expense(exp):
    """
    Checks if the expense entered by the user is valid

    :param exp: the expense
    :return: True if the expense is valid and False if the expense is invalid
    """

    if exp == 'housekeeping' or exp == 'transport' or exp == 'food' or exp == 'clothing' or exp == 'internet' or \
            exp == 'others':
        return True
    raise ValueError("Please enter a valid expense")


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


def test_function():

    x = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    cmd, params = split_command('insert 30 10 internet')
    assert cmd == 'insert'
    assert params == '30 10 internet'
    tokens = split_params('10 10 internet')
    assert tokens[0] == '10'
    assert tokens[1] == '10'
    assert tokens[2] == 'internet'
    y = []
    insert_command_run(10, y, tokens)
    assert y == [{'day': 10, 'amount_of_money': 10, 'expense_type': 'internet'}]
    tokens.pop()
    tokens[0] = 20
    tokens[1] = 'food'
    add_command_run(5, y, tokens)
    assert y == [{'day': 10, 'amount_of_money': 10, 'expense_type': 'internet'},
                 {'day': 5, 'amount_of_money': 20, 'expense_type': 'food'}]
    remove_by_category(y, 'food')
    assert y == [{'day': 10, 'amount_of_money': 10, 'expense_type': 'internet'}]
    remove_by_day(y, 10)
    assert y == []
    y = x
    k = 'internet'
    remove_between_days(y, 1, 30)
    assert y == []
    y = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    filter_command_1(y, 'internet')

    assert y == [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                 {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
                 {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'}]

    y = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    filter_command_4(y, 'internet', 10)

    assert y == [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                 {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'}]

    y = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    assert max_spent_command(y) == 3

    y = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    filter_command_3(y, 'internet', 10)

    assert y == []

    y = [{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
         {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
         {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
         {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
         {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
         {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
         {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
         {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
         {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]

    filter_command_2(y, 'internet', 10)

    assert y == [{'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'}]

