import time
from typing import Literal

def timer(_func=None,*,repeat=1,verbose=True)->Literal['execution time']:
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = []
            for k in range(repeat):
                t1 = time.perf_counter_ns()
                value = func(*args,**kwargs)
                t2 = time.perf_counter_ns()
                
                args_repr = [repr(a) for a in args]                      
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
                signature = ", ".join(args_repr + kwargs_repr)           
                if verbose:
                    print(f"[{repeat-k}] Calling {func.__name__}({signature}): returned {value!r}")

                t.append(t2-t1)
                
            if repeat == 1:
                print(f'[+] {func.__name__} Executed in {t[0]:_} nanoseconds.')
            
            elif repeat > 1:
                print(f'[+] {func.__name__} Executed in {(sum(t)/len(t)):_} nanosec average. (Max:{max(t):_}ns, Min:{min(t):_}ns)')
                
            else:
                print('[!] Repeat have to be greater than 1')

            return value
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)
    
    
def debugger(_func=None,*,raise_error=False)->Literal['debug']:
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                value=func(*args,**kwargs)
                status ='+'
                exit_status = 0
                
            except Exception as e:
                value='Error'
                status = '!'
                exit_status = e
                
            finally:
                print(f"[{status}]: {func.__name__} returned {value!r} (exit status:{exit_status})")
                if raise_error and exit_status: raise exit_status
     
            return value
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)
    
    
    
    
def on_thread(_func=None,*,reps=1,loop=False,timeout=600):
    global l
    l = loop
    def decorator(func):
        def wrapper(*args, **kwargs):
            if l:
                def loop(*args,**kwargs):
                    while True:
                        func(*args, **kwargs)
                        sleep(timeout)
            else:
                def loop(*args,**kwargs):
                    for _ in range(reps):
                        func(*args, **kwargs)
                        sleep(timeout)
                        
            t = Thread(target=loop,args=args,kwargs=kwargs)
                
            t.start()
            
            return 0
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)
