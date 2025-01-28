import datetime as date
from enum import Enum
def input_validation(request, lowerbound =0, upperbound=0):
    try:
        request = int(request)
        while request  < lowerbound and request  > upperbound:
                    request = input("please insert a number between", lowerbound, "and: ", upperbound)
        return request
    
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
       creation_date = date.today()
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

               



a = Menu()
function_dict = {
       "editFile":editFile,
}
a.load_options("menu_options.txt")
print(a)
print("#"*15)
b = input("please insert your choice for personal assistant ")
res = int(input_validation(b,0, a.get_upper_bound()))
if res != -1:
       a.call_function_by_name(a.dict[res][1],function_dict[a.dict[res][1]], "hi")





     
    
    
