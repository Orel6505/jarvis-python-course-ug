import datetime as date
from enum import Enum
import tkinter as tk
import tkinter.ttk  as ttk
# import pyttsx3


def input_validation(request: str, lowerbound =0, upperbound=0):
    """ The function gets a string input, if it's a digit in range, it returns the digit.
    otherwise, if it's digit but it's not in range or a non digit string it will return -1. """
    try:
        if(request.isdigit()):
                request = int(request)
                if request < upperbound and request  > lowerbound :
                       return request
                else:
                       print("The number specified specified is not in range.")
                       return -1
        else:
              print("Invalid input.")
              return -1               
                
    except Exception as e:
           return -1

def editFile():
       print("Entered the function editFile")
       path = input("please insert file path for reading, i'll read the first two lines")
       with open(path, 'r') as input_file:
              line1 = input_file.readline()
              line2 = input_file.readline()
              print("the first two lines are:", line1,line2)


class Menu:
       def __init__(self):
              self.dict = {}
       #dict has: key: number,value: tuple- (function description, name of function)

       def get_upper_bound(self):
             return len(self.dict)
              

       def call_function_by_name(self,func_name,func_ref, *args, **kwargs):
              if func_name :
                     return func_ref(*args, **kwargs)  # Pass arguments dynamically
              else:
                     raise ValueError(f"Function '{func_name}' is not defined.")

       
       def load_options(self, path_name):
              with open(path_name, 'r') as input_file:
                     line_index = 0
                     while(True): 
                            line = input_file.readline()
                            if not line:
                                break
                            result = [item.strip() for item in line.split(".") if item.strip()]
                            self.dict[line_index] = (result[0],result[1])
                            line_index+=1             
              
       def __str__(self):
              return str(self.dict)
              
                     
class Priority(Enum):
       LOW = 0
       MED = 1
       HIGH = 2

class Status(Enum):
       START = 0
       IN_PROGRESS = 1
       DONE = 2

class Item():
       # creation_date = date.today()
       __title = "empty"
       __status = Status.START
       __priority = Priority.LOW
       __due_date = ""
       __notes = ""
       
       def __init__(self):
              return "Item has been created"
       def modify_title(self,str):
              if str:
                     self.__title = str


       def modify_notes(self, str):
              if str:
                     self.__notes = str

               

window = tk.Tk()
greeting2 = ttk.Label(text="hello2!",font= ("arial",20))
btn1 = tk.Button(text= "click me!", width=30, height=30, fg="salmon", background="DarkKhaki",command=editFile)
btn1.pack()
greeting2.pack()
window.mainloop()


# engine = pyttsx3.init()
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# engine.say("Good morning sir.")
# engine.runAndWait()
# menu_object = Menu()
# # a dictionary that maps function names is String to the refrence of the functions
# function_dict = {
#        "editFile":editFile,
# }
# menu_object.load_options("menu_options.txt")
# print("#"*15)
# flag = -1
# while(flag == -1):
#        flag = input("please insert your choice for personal assistant ")
#        flag = input_validation(flag,-1, 2)
# print("The option specified is:",menu_object.dict[flag][0])
# menu_object.call_function_by_name(menu_object.dict[flag][1],function_dict[menu_object.dict[flag][1]])





     
    
    
