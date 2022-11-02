import main as decorators

@decorators.debugger
def divide(a,b):
    return a/b


divide(7,4)
# [+]: divide returned 1.75 (exit status:0)
divide(14.3,4)
# [+]: divide returned 3.575 (exit status:0)
divide(7,0)
# [!]: divide returned 'Error' (exit status:division by zero)


@decorators.debugger(raise_error=True)
def divide(a,b):
    return a/b

divide(7,0)
'''
[!]: divide returned 'Error' (exit status:division by zero)
Traceback (most recent call last):
  File ".\decorators\src\examples.py", line 20, in <module>
    divide(7,0)
  File ".\decorators\src\main.py", line 54, in wrapper
    if raise_error and exit_status: raise exit_status
  File ".\decorators\src\main.py", line 43, in wrapper
    value=func(*args,**kwargs)
  File ".\decorators\src\examples.py", line 18, in divide
    return a/b
ZeroDivisionError: division by zero
'''

@decorators.timer
def foo(a,b,c):
    for _ in range(c):
        a**b
        
foo(400,349,890)
#[1] Calling foo(400, 349, 890): returned None
#[+] foo Executed in 2_573_200 nanoseconds.

@decorators.timer(repeat=10)
def foo(a,b,c):
    for _ in range(c):
        a**b
        
foo(400,349,890)
'''
[10] Calling foo(400, 349, 890): returned None
[9] Calling foo(400, 349, 890): returned None
[8] Calling foo(400, 349, 890): returned None
[7] Calling foo(400, 349, 890): returned None
[6] Calling foo(400, 349, 890): returned None
[5] Calling foo(400, 349, 890): returned None
[4] Calling foo(400, 349, 890): returned None
[3] Calling foo(400, 349, 890): returned None
[2] Calling foo(400, 349, 890): returned None
[1] Calling foo(400, 349, 890): returned None
[+] foo Executed in 2_450_870.0 nanosec average. (Max:2_711_000ns, Min:2_353_400ns)
'''



@decorators.debugger
@decorators.timer(verbose=False)
def do_something(a,b,c):
    return [a/d for d in range(b,c,-1)]
        
        
do_something(100,500,-1)
#[!]: wrapper returned 'Error' (exit status:division by zero)

do_something(132,14,7)
#[+] do_something Executed in 2_400 nanoseconds.
#[+]: wrapper returned [9.428571428571429, 10.153846153846153, 11.0, 12.0, 13.2, 14.666666666666666, 16.5] (exit status:0)

    