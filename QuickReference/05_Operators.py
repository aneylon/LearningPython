#Operators

# Arithmetic
addition = 1 + 2
subtraction = 3 - 2
multiplication = 2 * 4
division = 8 / 4 # returns a float
modulus = 8 % 3 # returns remainder
exponent = 2 ** 3
floorDivision = 9 // 2

# Comparison
equal = 5 == 4
notEqual = 5 != 5
greaterThan = 5 > 4
lessThan = 5 < 4
greaterThanOrEqual = 5 >= 4
lessThanOrEqual = 5 <= 4

# Assignment
a = 1

a += 5 # Addition Assignment
a -= 5 # Subtraction Assignment
a *= 5 # Multiplication Assignment
a /= 5 # Division Assignment
a %= 5 # Remainder Assignment
a **= 5 # Exponent Assignment
a //= 5 # Floor Division Assignment

# Logical
logicalAnd = True and False
logicalOr = True or False
logicalNot = not(True and False)

# Membership
things = ['one', 'two', 'three']
membershipIn = 'one' in things
membershipNotIn = 'something' not in things

# Identity
x = ['one', 'two']
y = ['three', 'four']
z = x
identityIs = x is z
identityIsNot = x is not y

# Bitwise
bitWiseAnd = 60 & 13
bitWiseOr = 60 | 13
bitWiseXOr = 60 ^ 13
bitWiseNot = ~60 
zeroFillLeftShift = 60 << 2
signedRightShift = 60 >> 2