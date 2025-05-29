import datetime as dt
from enum import Enum
import pyttsx3
import tkinter as tk
from tkinter import ttk
import pywhatkit
# import pyttsx3
import base_tic_tac_toe as bTTT

def input_validation(request: str, lowerbound=0, upperbound=0) -> int:
    """
    Validates that the request is a digit and within (lowerbound, upperbound).
    Returns the digit if valid, -1 if the user wants to exit, otherwise -2 for error.
    """
    request = request.strip()
    if request == "-1":
        return -1  # Explicit request to exit

    if not request.isdigit():
        print("Invalid input.")
        return -2

    value = int(request)
    if lowerbound < value < upperbound:
        return value
    else:
        print("The number specified is not in range.")
        return -2
 
def edit_file():
    print("Entered the function edit_file")
    path = input("Please insert file path for reading. I'll read the first two lines: ")
    try:
        with open(path, 'r') as input_file:
            line1 = input_file.readline()
            line2 = input_file.readline()
            print("The first two lines are:", line1, line2)
    except Exception as e:
        print(f"Failed to read file: {e}")

def start_a_game():
    bTTT.TTT().mainloop()

def open_to_do_list():
    print("To-do list function is not implemented yet.")

class Menu:
    def __init__(self):
        # dict: key=int option num, value=(description, func_name)
        self.options = {}

    def get_upper_bound(self):
        return len(self.options)

    def call_function_by_name(self, func_name: str, func_ref, *args, **kwargs):
        if func_name:
            return func_ref(*args, **kwargs)
        raise ValueError(f"Function '{func_name}' is not defined.")

    def load_options(self, path_name):
        try:
            with open(path_name, 'r') as input_file:
                for idx, line in enumerate(input_file):
                    result = [item.strip() for item in line.split(".") if item.strip()]
                    if len(result) >= 2:
                        self.options[idx] = (result[0], result[1])
        except Exception as e:
            print(f"Failed to load options from {path_name}: {e}")

    def __str__(self):
        return str(self.options)

class Priority(Enum):
    LOW = 0
    MED = 1
    HIGH = 2

class Status(Enum):
    START = 0
    IN_PROGRESS = 1
    DONE = 2

class Item:
    def __init__(self):
        self.title = "empty"
        self.status = Status.START
        self.priority = Priority.LOW
        self.due_date = ""
        self.notes = ""
        print("Item has been created")

    def modify_title(self, title: str):
        if title:
            self.title = title

    def modify_notes(self, notes: str):
        if notes:
            self.notes = notes

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def talk(text: str) -> None:
    """Speak the provided text using TTS."""
    engine.say(text)
    engine.runAndWait()
    
def ttsx_stop():
       if engine:
              engine.stop()
              engine = None
              print("Text-to-speech engine stopped.")
       else:
              print("Text-to-speech engine is not running.")

def run_menu(menu_object, function_dict):
    """
    Runs the assistant's main menu loop.
    Prompts the user for choices, validates input, and executes the selected option.
    """
    upper_bound = menu_object.get_upper_bound()
    talk("Welcome to your personal assistant. Please choose an option from the menu.")

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