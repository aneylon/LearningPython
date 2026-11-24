print("Lambda Functions")

x = lambda a : a + 10
print(x(4))

x = lambda a, b : a * b
print(x(2,3))

x = lambda a, b, c : a + b + c
print(x( 2, 3, 4))

def multiplier(n) :
    return lambda a : a * n

doubler = multiplier(2)

print(doubler(5))

tripler = multiplier(3)

print(tripler(5))

numbers = [1,2,3,4,5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)