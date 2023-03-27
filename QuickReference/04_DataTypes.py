# variable data types can be set explicitly 

myString = str("This a string")

myInt = int(42)

myFloat = float(3.142)

myComplex = complex(1j)

myList = list(('one', 'two', 'three'))

myTuple = tuple(('four', 'five', 'six'))

myRange = range(7)

myDict = dict(name='Alex', age=37)

mySet = set(('thing', 'stuff','whatever'))

myFrozenSet = frozenset(('something', 'nothing', 'the thing'))

myBool = bool(5)

myBytes = bytes(5)

myByteArray = bytearray(5)

myMemoryView = memoryview(bytes(5))

# The type of a variable can be determined 

print(myString, type(myString))
print(myInt, type(myInt))
print(myFloat, type(myFloat))
print(myComplex, type(myComplex))
print(myList, type(myList))
print(myTuple, type(myTuple))
print(myRange, type(myRange))
print(myDict, type(myDict))
print(mySet, type(mySet))
print(myFrozenSet, type(myFrozenSet))
print(myBool, type(myBool))
print(myBytes, type(myBytes))
print(myByteArray, type(myByteArray))
print(myMemoryView, type(myMemoryView))

# type is it's own type
print(type(type(myString)))