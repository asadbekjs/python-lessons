# QIYMAT QAYTARUVCHI FUNKSIYA
# def add_1(a, b):
#     print(a + b)

# add_1(4, 5)

# def add_2(a, b):
#     return a + b

# print(add_2(3, 4))
# value = add_2(5, 8)
# print(value)

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

# # local variable - funksiya ichida e'lon qilingan o'zgaruvchi
# # print(toliq_ism) 
# """
# NameError: name 'toliq_ism' is not defined - toliq_ism o'zgaruvchisi funksiya 
# ichida e'lon qilingan va faqat shu funksiya ichida mavjud, tashqarida 
# esa mavjud emas
# """

# print(toliq_ism_yasa("Maftuna", "Ozodboyeva"))
# print(toliq_ism_yasa("Olim", "Xolmatov"))

# print("a" * 3) # a harfini 3 marta takrorlaydi => "aaa"
# print("abc" * 5) # abc matnini 5 marta takrorlaydi => "abcabcabcabcabc"
# # print("abc" + 2) # TypeError: can only concatenate str (not "int") to str - matn va sonni qo'shish mumkin emas
# print("abc" / 5)

# def is_even(number = 8):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"
    
# print(is_even(4)) # Juft
# result = is_even(7)
# print(result) # Toq
# print(is_even()) # Juft

# Ternary operator yordamida yuqoridagi if/else codelarini qisqartirish mumkin
# syntax: value_if_true if condition else value_if_false
# def is_even(number):
#     return "Juft" if number % 2 == 0 else "Toq"

# print(is_even(4)) # Juft
# print(is_even(7)) # Toq

vowels = ["a", "o", "i", "u", "e"]
def count_vowels(text):
    count = 0
    for char in text:
        if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
            count += 1

    return count

print(count_vowels("javascript")) # 3
print(count_vowels("frontender")) # 3
print(count_vowels("bbbb")) # 0

# string bo'yicha for loop ishlatish
# text = "Hello"
# for char in text:
#     print(char)