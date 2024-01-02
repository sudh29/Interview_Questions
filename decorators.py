# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper
  
# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper
  
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
hello()   # output => [ 'hello' , 'world' ]


# with arguments

def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_n_times(n=3)
def greet(name):
    print(f"Hello, {name}!")

# Equivalent to greet = repeat_n_times(n=3)(greet)
# Now, calling greet will repeat the greeting three times
greet("Alice")

# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
