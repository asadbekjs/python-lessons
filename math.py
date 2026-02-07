# Python math Module
import math
# constants
print(math.e) # 2.71
print(math.pi) # 3.1415

# methods
print(math.fabs(-5))
print(math.fabs(8))

square_root = math.sqrt(25)
print(square_root)

print(math.pow(2, 5))
print(math.pow(11, 3))

# n! = 1 * 2 * 3 ... (n - 1) * n
print(math.factorial(5))

# up(yuqoriga) rounding
print(math.ceil(4.3)) # 5
print(math.ceil(4.7)) # 5

# down(pastga) rounding
print(math.floor(4.7)) # 4
print(math.floor(4.3)) # 4

# sin/cos/tg/ctg
print(math.sin(math.radians(90)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(45)))
print(math.sin(1.2))

print(math.exp(5))