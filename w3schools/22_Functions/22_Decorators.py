
print("Function Decorators")

def change_case (func) :
    def inner () :
        return func().upper()
    return inner

@change_case
def some_func() :
    return "An Example."

print(some_func())

print("Decorator Arguments")

def decorator_arguments(func) :
    def inner(x) :
        return func(x).upper()
    return inner

@decorator_arguments
def case_and_args(name):
    return "Hey " + name

print(case_and_args("steve"))

print("Decorator arguments")

def another_case(n) :
    def change_case(func) :
        def inner () :
            if(n == 1) :
                a = func().lower()
            else : 
                a = func().upper()
            return a
        return inner
    return change_case

@another_case(1)
def example() :
    return "Hey Dude"
print(example())

@another_case(2)
def example_two() :
    return "Yo Bro"
print(example_two())

print("Multiple Decorators")

def to_upper (func) :
    def inner() :
        return func().upper()
    return inner

def add_greeting (func) :
    def inner() :
        return "Hey " + func() + ", how you doin'?"
    return inner

@to_upper
@add_greeting
def two_decorators() : 
    return "Dude"

print(two_decorators())

print("Metadata")

def meta_one() :
    return "Meta One"

print (meta_one.__name__)

def meta_case(func) :
    def inner () :
        return func().upper()
    return inner

@meta_case
def meta_two() :
    return "Meta Two"

print(meta_two.__name__)

import functools

def meta_wrap(func) :
    @functools.wraps(func)
    def inner() :
        return func().upper()
    return inner

@meta_wrap
def meta_keep():
    return "Meta Keep"

print(meta_keep.__name__)