"""
This project defines a decorator called memoize which takes a function as an argument and returns a new function that 
caches the results of the original function for future calls with the same arguments.It also defines a function called
fibonacci which recursively computes the Fibonacci sequence up to the nth number.

"""

#1. Create a decorator called memoize which takes a function as an argument and returns a new function that caches the results of the original function inside a dictionary. wrapper checks if the argument does not exist in dictionary, it adds to cache it.

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
  
#2.  Apply  @memoize decorator  to the fibonacci function, which means that whenever fibonacci is called with a particular argument, the decorator will first check if that argument has already been computed and cached. If it has, the cached result is returned instead of recomputing the value.

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
#3. Full Code

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
 
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
