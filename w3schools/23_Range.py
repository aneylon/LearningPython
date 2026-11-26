print("Range")
print("range(start, stop, step)")

range_one = range(5)
print(range_one)

range_two = range(3, 6)
print(range_two)

range_three = range( 2, 8, 2)
print(range_three)

print("range to list")
print(list(range_one))
print(list(range_two))
print(list(range_three))

print("range length")
print(len(range_one))
print(len(range_two))
print(len(range_three))

print("Membership testing")
print( 3 in range_one)
print( 5 in range_two)
print( 4 in range_three)

print("slices")
print(range_one[2])
print(range_two[:3])
print(range_three[-1])

print("Loops")
print("range one")
for i in range_one :
    print(i)

print("range two")
for i in range_two :
    print(i)

print("range three")
for i in range_three :
    print(i)