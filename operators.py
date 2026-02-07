# Python operators
# 1. Arithmetic Operators (+, -, *, /, %, **, //)
# x = 8
# y = 2
# # modules(%) - qoldiqni hisoblash
# print(x % y)
# print(3 % 8)
# print(4 // 2, 12 // 5)

# Comparison(solishtirish) Operators => Boolean values(True, False)
# ==  
# print(3 == 4) # False
# print(5.5 == 5.50) # True
# print(8.5 == 8) # False
# # !=
# print(3 != 4) # True
# print(5 != 5) # False
# print(8 != 8) # False
# >
# print(x > y, 5 > 5.0) # True
# print(x < y, 10 < 10.01) # False
# # >=
# print(5 >= 3, 5 >= 5)
# print(5 <= 3, 8.2 <= 8.20)

# Logical(Mantiqiy) Operators
# and operator
# score = 45
# print(score > 69 and score < 86)
# print(8 == 8 and 8 < 7)

# # or operator
# print(8 == 8 or 8 < 7)
# print(score > 69 or score > 86)

# # not (True => False)
# print(not(12 > 18))
# print(not(8 == 8 or 8 < 7))
z = 12
print(z > 10 and z < 5 or not(z > 8)) # True and False or False => False or False => False
# Assignment(tayinlash) operators
# = 
y = 5
# +=
z += 3 # z = z + 3
print(z)
y += 5 # y = y + 5
print(y)
z -= 2 # z = z - 2
print(z)
y *= 2 # y = y * 2
print(y)
y /= 2 # y = y / 2
print(y) # 10
y %= 2 # y = y % 2
print(y)