
print("Tuples")

# With or without parentheses

thisTuple = ("one", "two", "Three")
thatTuple = 1,2,3

print(thisTuple, thatTuple)

# Duplicates are allowed
# Any mix of types is allowed
doubles = ("a", "a", "B", "B", 3, 3)

print(doubles)

# Find the length of a tuple

print(len(doubles))

# Can include one item but must use a comma

isATuple = ("one",)
notATuple = ("two")

print(type(isATuple))
print(type(notATuple))

# Empty tuples

empty = ()
print(type(empty))

# Create with a constructor

constructed = tuple(("con", "struct", 'ed'))

print(constructed, type(constructed))