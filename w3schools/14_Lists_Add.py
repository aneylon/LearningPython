
thisList = ['one', 2, False, 'asdf', 3, True]

thisList.append("orange")

print(thisList)

thisList.insert(2,3)

print(thisList)

thatList = [1,2,3,4]

thisList.extend(thatList)

print(thisList)

thisTuple = ("three", "four")

thisList.extend(thisTuple)

print(thisList)
