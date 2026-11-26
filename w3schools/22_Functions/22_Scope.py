
print("Function Scope")

global_variable = "Global"

def scope_example () :
    local_variable = "Local"
    print(local_variable)

print(global_variable)
scope_example()

def declare_global () :
    global stuff
    stuff = "Global in function"
    print(stuff)

declare_global()

def declare_nonlocal ( ) :
    example = "stuff"
    
    def inner () :
        nonlocal example
        example = "things"

    inner()

    return example

print(declare_nonlocal)

x = 200

def basic_example() :
    x = 300
    print(x)

basic_example () 

print(x)