def input_validation(request, lowerbound, upperbound):
    try:
        request = int(request)
        while request  < lowerbound and request  > upperbound:
                    request = input("please insert a number between", lowerbound, "and: ", upperbound)
        return request
    
    except Exception as e:
           return -1


     
    
    
