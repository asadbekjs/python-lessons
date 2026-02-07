# if-else => tarmoqlanish operatori
# age = int(input("Yoshingizni kiriting: "))
# if age > 18:
#     print("Kirish huquqiga egasiz")
# else: 
#     print("Siz hali yoshsiz")

# ball = int(input("Ballingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("Siz imtihondan 3 baho bilan o'tdingiz")
# elif ball >= 70 and ball < 86:
#     print("Siz imtihondan 4 baho bilan o'tdingiz")
# elif ball >= 86 and ball <= 100:
#     print("Siz imtihondan 5 baho bilan o'tdingiz")
# else:
#     print("Iltimos, 0 dan 100 gacha ball kiriting")

# age = int(input("Iltimos yoshingizni kiriting : "))
# if age >= 16:
#     print("Siz passport olishingiz mumkin")
# else:
#     print("Siz hali yoshsiz")

# number = int(input("Son kiriting: "))
# if number > 0:
#     print("Bu musbat son.")
# else:
#     print("Bu manfiy son.")

# son = int(input("Sonni kiriting"))
# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")

# Amaliyot
# 1-mashq
# son = int(input("Sonni kiriting"))
# if son % 2 == 0 and son % 3 == 0:
#     print("6 ga bo'linadi")
# else:
#     print("6 ga bo'linmaydi")

# 2-mashq
# a = int(input("Uchburchakning 1-tomoni kiriting: "))
# b = int(input("Uchburchakning 2-tomoni kiriting: "))
# c = int(input("Uchburchakning 3-tomoni kiriting: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasab bo'ladi")
# else:
#     print("Uchburchak yasab bo'lmaydi")

# 3-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a < b < c:
#     print("YES")
# else:
#     print("NO")

# 4-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a > b:
#     print(a)
# else:
#     print(a, b)

# 5-mashq
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a <= b:
#     a = 0
#     print(a, b)
# else:
#     print(a, b)

# 6-mashq
# import math
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a >= b >= c:
#     print(2 * a, 2 * b, 2 * c)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))

# 7-mashq
# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# a = 2 * x * 2 * y
# b = (x + y) / 2
# if x > y:
#     x = a
#     y = b
# else:
#     x = b
#     y = a

# print("%.1f" % x, "%.1f" % y)

# 8-mashq
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# if x < 0 and y < 0:
#     print(abs(x), abs(y))
# elif x < 0 or y < 0:
#     print(x + 0.5, y + 0.5)
# elif x > 0 and y > 0:
#     print(x, y)

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)
# else:
#     print("hech biri kirmaydi")

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2

# print(x, y, z)

# 12.77, 15.88, -75, 18, 0, 89, 25
# max - eng katta => 89
# min -eng kichik => -75 
# print(max(12.77, 15.88, -75, 18, 0, 89, 25))
# print(min(12.77, 15.88, -75, 18, 0, 89, 25))

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# print(max(x, y, z), min(x, y, z))

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# print(max(x + y + z, x, y, z), min(x + y / 2, x, y, z) ** 2)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = float(input("3-sonni kiriting: "))
# d = float(input("4-sonni kiriting: "))
# max_value = max(a, b, c, d)
# min_value = min(a, b, c, d)
# if a <= b <= c <= d:
#     a = b = c = d = max_value
# else:
#     a = b = c = d = min_value
# print(a, b, c, d)

# homework
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# a = (x + y) / 2
# b = 2 * x * y
# if x < y:
#     x = a
#     y = b
# elif x > y:
#     x = b
#     y = a

# print(int(x), int(y))

#
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# min_value = min(x, y, z)
# if x < 1 and y < 1 and z < 1:
#     if min_value == x:
#         x = (y + z) / 2
#     elif min_value == y:
#         y = (x + z) / 2
#     else:
#         z = (x + y) / 2

# print(x, y, z) 

