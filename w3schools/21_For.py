
print("For Loops")

print("Array Loop")
fruits = ['apple', 'orange', 'banana', 'cherry']

for x in fruits :
    print(x)

print("String Loop")

for x in "asdfqwer" :
    print(x)

print("Break out of loop")

for x in fruits :
    if x == 'banana' :
        break
    print(x)

print("Continue past")

for x in fruits :
    if x == "banana" :
        continue
    print(x)

print("Range function")

print("Zero to limit, not including.")
for x in range(6) :
    print(x)

print("From start to limit, not including.")
for x in range(3,7) :
    print (x)

print("From start to limit, not including, with step.")
for x in range(2, 20, 2) :
    print (x)

print("Else at the end")
for x in range(3) :
    print(x)
else :
    print("it's over man")