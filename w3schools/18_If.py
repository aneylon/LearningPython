print("If")

if(True) :
    print("True")

print("elif = else if")

a = 22
b = 22

if a < b :
    print("A less than B")
elif a > b :
    print("A greater than B")
elif a == b :
    print("A equals B")

print("Else")

if a != b :
    print("A not equal to B")
else : 
    print("No conditions met.")

print("Short hand")

if( a == b) : print("a equals b")

print("A 23") if a == 23 else print("it don't")

print("Assign with conditional")

a = 10
b = 20

bigger = a if(a > b) else b

print(bigger)

print("Multiple one liners")

a = 30

print("A") if a > b else print("=") if a == b else print("B")