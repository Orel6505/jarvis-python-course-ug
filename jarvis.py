def input_validation(request, lowerbound, upperbound):
    try:
        request = int(request)
        while request  < lowerbound and request  > upperbound:
                    request = input("please insert a number between", lowerbound, "and: ", upperbound)
        return request
    
    except Exception as e:
           return -1


class Menu:
       def __init__(self):
              self.dict = {}
       
       def call_function_by_name(func_name, *args, **kwargs):
              if func_name :
                     return functions[func_name](*args, **kwargs)  # Pass arguments dynamically
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
              
                     
 
a = Menu()
a.load_options("menu_options.txt")
# print(a)




     
    
    
