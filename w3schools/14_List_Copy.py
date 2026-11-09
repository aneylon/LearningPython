
thisList = ["one", 2, False, "Things"]

newList = thisList.copy()
badCopy = thisList
print(newList, thisList)

print(newList is thisList)
print(thisList is badCopy)

# Use List method

listList = list(thisList)

print(listList)

# Slice copy

sliceList = thisList[:]
print(sliceList)

