print("List Sorting")

thisList = ['orange', 2, False, 'four']

numberList = [4,7,2,9,5,1,8]

lettersList = ['c','g','a','n','b','q']

# Cannot sort mixed list
# thisList.sort()
# print(thisList)

numberList.sort()
print(numberList)

lettersList.sort()
print(lettersList)

# Reverse sort

numberList.sort(reverse=True)
print(numberList)

lettersList.sort(reverse=True)
print(lettersList)

print("Reverse a list")
print(thisList)
thisList.reverse()
print(thisList)

# Case insensitive sort

casedList = ["one", "Two", 'three', "Four"]
print(casedList)
casedList.sort()
print(casedList)
casedList.sort(key = str.lower)
print(casedList)

# Custom sort function

def someFunc(n) :
    return abs(n - 50)

someList = [100, 50, 65, 82, 23]
print(someList)
someList.sort(key = someFunc)
print(someList)
