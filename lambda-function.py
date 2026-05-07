# lambda function - anonymous(maxfiy, noma'lum) function
# syntax:
# lambda arguments : expression(ifoda)
# x = lambda a : a % 5
# print(x(12))

# import math as m
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(m.pi, 5))

# product = lambda x, y : x ** y
# print(product(3, 2))
# print(product(8, 3))

# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# print(kvadrat(5)) # 5 ** 2 = 25
# kub = daraja(3)
# print(kub(7)) # 7 ** 3 = 343

# map() va filter()
# numbers = list(map(int, input().split()))
sonlar = [5, 8, -8, 0, 13]
# sonlar2 = []
# for son in sonlar:
#     sonlar2.append(son * 2)

# print(sonlar2)

# map(func, iterable)
print(list(map(lambda x : x * 2, sonlar)))
print(list(map(lambda x: x % 3, sonlar)))

# filter(func, iterable)
print(list(filter(lambda x: x > 5, sonlar)))
students = ['Elbek', 'Lobar', "G'ulomjon", "Behruz", "Lola"]
new_list = list(map(lambda ism: ism.lower() , students))
print(list(filter(lambda ism: ism.startswith('l'), new_list)))

def func(x):
    return x + 5

print(list(map(func, sonlar)))
