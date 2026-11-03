thisList = ['one', 2, False, "test"]
print(thisList)

# change a single item
thisList[0] = "changed"
print(thisList)

# change multiple items
thisList[1:3] = [3,True]
print(thisList)

# insert multiple values

thisList[1:2] = [1,2,4]
print(thisList)

# remove multiple and replace with one
thisList[1:4] = [5]
print(thisList)

# insert at specified index
thisList.insert(2, "Inserted!")
print(thisList)


