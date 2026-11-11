
print("Append an element to the end of a list")

listOne = [1,'a', True]

listOne.append('two')

print(listOne)

print("Clear a list of it's contents")

listOne.clear()

print(listOne)

print("Copy a list to a new variable")

listOne = ['a', 2, False]
listTwo = listOne.copy()

print(listOne, listTwo)
print(listOne is listTwo)

print("Count the number of elements in a list that match the argument.")

print(listOne.count(False))

print("Extend a list with another list")

listOne.extend(listTwo)
print(listOne)

print("Index of a specific item in a list")

print(listOne.index(2))

print("Insert a value at a specific index in a list")

listOne.insert(2, 3)

print(listOne)

print("Pop an element at a specific index out of a list or the last item if no index is provided.")

popped = listOne.pop(2)
print(listOne, popped)

print("Remove a specific value from a list")

removed = listOne.remove(False)

print(listOne, removed)

print("Reverse a list")

listOne.reverse()

print(listOne)

print("Sort a list")

letters = ['d', 'b', 'a', 'c']
numbers = [4,7,2,9,1]

letters.sort()
numbers.sort()

print(letters, numbers)