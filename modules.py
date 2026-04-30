# Pythonda modullar
# import math
# print(math.sqrt(16))
# print(math.pi)
# 1. as operator - modul nomini qisqartirish
# m = 5
# import math_operators as m
# print(math_operators.addition(7, 8))
# print(math_operators.multiplication(7, 5))
# print(math_operators.PI)
# print(math_operators.find_max(18, -8, 9, 77, 12))
# print(m.subtraction(7, 5))

# 2. modul ichidan faqatgina kerakli function, variablelarni chiqarish olish
# from math_operators import addition, subtraction, PI
# print(addition(4, 5))
# print(subtraction(4, 2))
# print(PI)

# 3. * - moduldan barcha functions, variablesni chiqarib olish
# from math_operators import *
# print(multiplication(4, 7))
# print(addition(5, 4))
# print(PI)

# 4. python random modul
import random as r
print(r.random()) # 0 va 1 oraliqdagi tasodifiy sonni qaytaradi
print(r.randint(0, 100))

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(11))
print(x)
r.shuffle(x)
print(x)

