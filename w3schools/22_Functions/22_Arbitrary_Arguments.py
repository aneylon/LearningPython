
print("Arbitrary Arguments")

def arbitrary_args(*things) : {
    print('the last thing :', things[-1])
}

arbitrary_args("one", "two", "three")

def args(*things) :
    print("all args : ", things)

args("four", "Three", 2)

def mix_args(greeting, *names) :
    print(greeting, names)

mix_args("Hey", "one", "Two", True, 1)

def numbers_total (*numbers) :
    total = 0
    for num in numbers :
        total += num
    return total

print(numbers_total(3,6,1,8))

def keyword_args(**args) :
    print("Type :", type(args))
    print("Name :", args['name'])
    print("Age :", args['age'])
    print("All :", args)

keyword_args(age=32, name="steve", other=False)

def unpack(a,b,c) :
    return a + b + c

nums = [6, 3, 8]

print(unpack(*nums))