
print("Join lists")


listOne = [1,2,3]
listTwo = ['a', 'b','c']

listThree = listOne + listTwo

print(listThree)

print("Append")

for x in listTwo : 
    listOne.append(x)

print(listOne)

print("Concatenate")

aList = ["one", 2, True]
bList = [2, "Three", False]

aList.extend(bList)

print(aList)