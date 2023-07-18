def decorator_name(_func=None,*,parameters=None)->None:
    #This is called when we call the decorator as <decorator(args)
    def decorator(func):
        #This is called when the function that is decorated is called
        def wrapper(*args, **kwargs):
            #Used to pass the args and kwargs to the function, and return it 
            return func(*args,**kwargs)
            #Also we can save the returned in a variable and return it late
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)
    
    





