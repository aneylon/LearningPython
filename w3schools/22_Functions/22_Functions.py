
print("Functions")

print("Pass")

# a function body cannot be empty. 
# You can use the "pass" statement as a placeholder
def pass_function() :
    pass
pass_function()

print("Returns")

def print_hello() :
    print("hello")

# If no if nothing is returned "None" is returned by default

hello_result = print_hello()
print(hello_result)

def return_hello() :
    return "hello"

print(return_hello())