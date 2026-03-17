# Dictionary elementlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 Pro Max',
    'year': 2025,
    'color': 'Silver',
    'price': 1500
}
# 1. get() metodi - kalit orqali qiymatni olish
print(phone.get('model')) # iPhone 17 Pro Max
print(phone.get('price', "Narx topilmadi")) # 1500
print(phone.get('battery')) # None (kalit mavjud emas)
print(phone.get("battery", "Kalit topilmadi")) # Kalit topilmadi

# 2. items() metodi - lug'at elementlarini (kalit, qiymat) juftlari sifatida olish
print(phone.items()) # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 Pro Max'), ('year', 2025), ('color', 'Silver'), ('price', 1500)])
for key, value in phone.items():
    print(f"{key}: {value}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# 3. keys() metodi - lug'atning barcha kalitlarini olish
print(phone.keys()) # dict_keys(['brand', 'model', 'year', 'color', 'price'])
# print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
}
# print(mahsulotlar.keys())
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# 1. listda in operatori qiymatning mavjudligini tekshiradi
fruits = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']
print('olma' in fruits) # True
print('tarvuz' in fruits) # False

# fruit = input("Qaysi meva yoqadi? ")
# if fruit in fruits:
#     print(f"{fruit.title()} do'konimizda bor.")
# else:
#     print(f"{fruit.title()} do'konimizda yo'q.")

bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     print(mahsulot) # lug'atning kalitlari bo'ladi

# mahsulotlar - lug'at, bozorlik - ro'yxat, mahsulot - lug'atning kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

print(sorted(mahsulotlar.keys())) # ['anjir', 'anor', 'olma', 'shaftoli', 'uzum']
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# 5. values() metodi - lug'atning barcha qiymatlarini olish
print(phone.values()) # dict_values(['Apple', 'iPhone 17 Pro Max', 2025, 'Silver', 1500])
# print(telefonlar.values()) # dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokia 3310'])

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)