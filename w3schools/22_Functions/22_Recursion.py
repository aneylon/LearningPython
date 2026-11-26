print("Recursion")

print("Countdown")
def countdown(n) :
    if n < 0:
        print("Blast off!")
    else :
        print(n)
        countdown(n -1)

countdown(5)

print("Factorial")

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial(n - 1)

print(factorial(5))

print("Fibonacci")

def fibonacci(n) :
    if n <= 1 :
        return n
    else :
        return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(7))

print("Sum list") 

def sum_list(numbers) :
    if len(numbers) == 0 :
        return 0
    else :
        return numbers[0] + sum_list(numbers[1:])

a_list = [1, 2, 3, 4, 5]

print(sum_list(a_list))


def  find_max(numbers) :
    if len(numbers) == 1 :
        return numbers[0]
    else :
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest

some_numbers = [5,3,8,6,9,1]

print(find_max(some_numbers))

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
