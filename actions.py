import base_tic_tac_toe as bTTT

def input_file_path():
    return input("Please insert file path for reading. I'll read the first two lines: ")

def edit_file():
    print("Entered the function edit_file")
    path = input_file_path()
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