"""


@author: Nichifor Dragos


"""

from ui import printmenu
from ui import begin
from ui import read_current_date
from ui import exit_function
from ui import add_command_run_ui
from ui import insert_command_run_ui
from ui import remove_command_run_ui
from ui import display_list_command_run_ui
from ui import undo_command_run_ui
from ui import sum_command_run_ui
from ui import max_spent_command_ui
from ui import sort_day_command_ui
from ui import filter_command_ui
from ui import test_function_ui


from functions import remove_command_run
from functions import display_list_command_run
from functions import split_command
from functions import test_function


# =============================================== CHECKERS ===============================================


def start_command_ui():
    """
    The base function that loops untill the user exits the aplication. The user can enter commands
    specified in the menu in order to realise different operations

    :return:
    """
    undo_op = [[{'day': 20, 'amount_of_money': 10, 'expense_type': 'internet'},
                {'day': 3, 'amount_of_money': 200, 'expense_type': 'transport'},
                {'day': 4, 'amount_of_money': 44, 'expense_type': 'clothing'},
                {'day': 5, 'amount_of_money': 5, 'expense_type': 'internet'},
                {'day': 10, 'amount_of_money': 120, 'expense_type': 'food'},
                {'day': 19, 'amount_of_money': 10, 'expense_type': 'others'},
                {'day': 3, 'amount_of_money': 120, 'expense_type': 'housekeeping'},
                {'day': 23, 'amount_of_money': 20, 'expense_type': 'transport'},
                {'day': 29, 'amount_of_money': 10, 'expense_type': 'internet'},
                {'day': 1, 'amount_of_money': 5, 'expense_type': 'others'}]]

    printmenu()

    begin()

    cmd_dict = {'add': add_command_run_ui, 'remove': remove_command_run_ui, 'insert': insert_command_run_ui,
                'list': display_list_command_run_ui, 'undo': undo_command_run_ui, 'sum': sum_command_run_ui,
                'max': max_spent_command_ui, 'sort': sort_day_command_ui, 'filter': filter_command_ui}

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

    test_function()
    test_function_ui()

    current_day = read_current_date()

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
                    cmd_dict[cmd_word](current_day, undo_op, x, cmd_params)
                except ValueError as ve:
                    print("Please enter a valid atribute")


if __name__ == '__main__':
    """
    The main function
    """

    start_command_ui()
