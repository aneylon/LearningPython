
thisList = ['a', 'b', 1, False, "one", ]
print(thisList)

# select the exact index
print(thisList[0])

# Negative = start from the end
print(thisList[-1])

# Range between but not including last
print(thisList[1:3])

# From beginning to before 
print(thisList[:4])

# From index to end
print(thisList[2:])

# Range of negative indexes
print(thisList[-4: -1])

# Check existence
print('"one" in thisList :', "one" in thisList)