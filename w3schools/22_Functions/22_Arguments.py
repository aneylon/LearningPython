
print("Arguments")

def function_argument(name) :
    print("hello", name)

function_argument("steve")

def function_multiple_arguments(one, two) :
    print(one, two)

function_multiple_arguments(1,3)

def function_default(name = "bro") :
    print("hey", name)

function_default()

def keyword_arguments(type, name) :
    print("Type is : ", type)
    print("Name is : ", name)

keyword_arguments(name="steve", type="some guy")

def positional_only(name, /) :
    print("hey", name)

positional_only("yo")
# positional_only(name = "yo") # no good

def keyword_only(*, name) :
    print("hey", name)

# keyword_only('test')
keyword_only(name = "bro")

def position_and_keyword(a,b,/,*,c,d) :
    print(a,b,c,d)

position_and_keyword(1,2, d=4, c=3)