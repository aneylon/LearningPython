
thisList = [
    'one', 2, True, 'Steve'
]

print("for in")
for x in thisList : 
    print(x)

print("\n")

print("for, in, range")
for i in range(len(thisList)) :
    print(thisList[i])

print("\n")

print('while')
i = 0
while i < len(thisList) :
    print(thisList[i])
    i += 1

print("\n")

print("list comprehension")

[print(x) for x in thisList]
