thisList = ["one", 2, False, "Steve", "one"]

print(thisList)

# Remove specific item, only the first instance
thisList.remove("one")

print(thisList)

# Remove item at specified index
thisList.pop(1)

print(thisList)

# Remove the last item

thisList.pop()

print(thisList)

# remove item at index
del thisList[0]

print(thisList)

# delete the entire list
# del thisList

# Empty the list but do not remove it.
thisList.clear()

print(thisList)