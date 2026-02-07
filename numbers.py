# Ma'lumot turlari (Data types)
# 1. String(matn)
# 2. Number(son) => 1. Integer(butun son) 5 -5 10; 2. Float(O'nlik son) 5.78 -8.99 0.75
# 3. Boolean(Manqitiy qiymat) => 1. True(Haqiqat); 2. False(Yolg'on)
# text = "lorem ipsum"
# age = 28
# is_student = True
# # type() - data type checking
# print(type(text)) # str
# print(type(-78)) # int
# print(type(8.97)) # float
# print(type(is_student)) # bool
# a = 20 
# b = -30
# c = a + b
# print(c) # 10

# pi = 3.1415
# radius = 10
# diametr = 2 * radius
# yuza = pi * radius ** 2
# print(diametr)
# print(yuza)

# print(50 / 10) # 5.0

# a = 2
# b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shunday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

PI = 3.1415
G = 9.81
print(PI, G)

# x = 7
# y = -5
# z = 10


kv_tomon = int(input("Kvadrat tomoni kiriting: ")) # 5 => "5" => 5
print(kv_tomon ** 2)

# typecasting - bir turdagi ma'lumotni boshqa turga o'zgartirish
ism = "Jobir"
yosh = 36 # "36"
# Jobir 36 yoshda
xabar = ism + " " + str(yosh) + " yoshda"
print(xabar)
print(type(yosh)) # int
yosh = str(yosh) # str
print(type(yosh))

print(int(5.36)) # 5
print(int(5.5)) # 5
print(float('8.87')) # 8.87 => float
print(float(5)) # 5.0
