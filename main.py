import datetime as dt

from menu import Menu
from utils import input_validation, talk, ttsx_stop
from actions import edit_file, open_to_do_list, start_a_game

def jarvis_greeting():
    """Greet the user based on the current local time."""
    hour = dt.datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good morning sir"
    elif 12 <= hour < 15:
        greeting = "Good noon sir"
    elif 15 <= hour < 18:
        greeting = "Good afternoon sir"
    elif 18 <= hour < 22:
        greeting = "Good evening sir"
    else:
        greeting = "Good night sir"
    print(greeting)
    talk(greeting)
    
def run_menu(menu_object, function_dict):
    """
    Runs the assistant's main menu loop.
    Prompts the user for choices, validates input, and executes the selected option.
    """
    upper_bound = menu_object.get_upper_bound()
    jarvis_greeting()

    while True:
        user_input = input("Please insert your choice for personal assistant: ")
        flag = input_validation(user_input, upperbound=upper_bound)

        if flag == -1:
            print("Exiting Personal Assistant. Goodbye!")
            talk("Exiting Personal Assistant. Goodbye!")
            ttsx_stop()
            break

        if flag == -2:
            print("Invalid input. Please try again.")
            continue

        try:
            description, func_name = menu_object.options[flag]
        except Exception as e:
            print("Invalid choice. Please try again.")
            continue

        print("The option specified is:", description)
        func_ref = function_dict.get(func_name)
        if func_ref:
            menu_object.call_function_by_name(func_name, func_ref)
        else:
            print(f"No function mapped for '{func_name}'.")

def main():
    menu_object = Menu()
    function_dict = {
        "editFile": edit_file,
        "open_to_do_list": open_to_do_list,
        "start_a_game": start_a_game,
    }
    menu_object.load_options("menu_options.txt")
    run_menu(menu_object, function_dict)

if __name__ == "__main__":
    main()