import datetime as date
from enum import Enum

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

def editFile(path):
       print("Entered the function editFile")

class Menu:
       def __init__(self):
              self.dict = {}

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

               



# a = Menu()
# function_dict = {
#        "editFile":editFile,
# }
# a.load_options("menu_options.txt")
# print(a)
# print("#"*15)
flag = -1
while(flag == -1):
       flag = input("please insert your choice for personal assistant ")
# res = int(input_validation(b,0, a.get_upper_bound()))
       flag = input_validation(flag,0, 2)
print(flag)
# if res != -1:
#        a.call_function_by_name(a.dict[res][1],function_dict[a.dict[res][1]], "hi")





     
    
    
