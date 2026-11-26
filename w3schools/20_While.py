
print("While loop")

i = 1
while i < 6 :
    print(i)
    i += 1

print("Break")

j = 1
while j < 4 :
    print(j)
    if j == 3 :
        break
    j += 1

print("Continue")

k = 1
while k < 5 :
    k += 1
    if k == 3 :
        continue
    print(k)

print("Else")

l = 1
while l < 3 :
    print(l)
    l += 1
else : 
    print("No more l")