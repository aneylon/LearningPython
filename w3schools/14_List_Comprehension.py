
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newList = []

# No list comprehension

for x in fruits :
    if "a" in x :
        newList.append(x)

print(newList)

# Yes list comprehension

newerList = [x for x in fruits if "a" in x]

print(newerList)

upperCase = [x.upper() for x in fruits]

print(upperCase)

