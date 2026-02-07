# List - ro'yxat // Array, massiv
user1 = "Bekhruz"
user2 = "Maftuna"
print(user1)
print(type(user2)) # str
user2 = 'Alex'
users = ['Gulyora', "G'ulomjon", 'John', 'Margaritta']
# List elementlari indekslanadi
# Dasturlashda indekslash 0 dan boshlanadi
# List elementini olish(element indeksi orqali olinadi)
first_element = users[0]
third_element = users[2]
print(first_element, third_element, users[3])
print(type(users)) # list
mixed_data = ['test', 12, True, -5.75, False, ['hey', 'hi'], 'py', 'js', 'c++', 25]
# List uzunligi (length of list) - ro'yxatdagi elementlar soni
print(len(users))
print(len(mixed_data))
print(mixed_data[5])
# first element
print(mixed_data[0])
# last element
length = len(mixed_data)
last_index = length - 1
print(mixed_data[last_index])
print(mixed_data[2])
# List elementini o'zgartirish
mixed_data[2] = False
print(mixed_data[2])
# Element qo'shish
# 1. list.append(element)
users.append('Valeriy')
print(users)
# ['Gulyora', "G'ulomjon", 'John', 'Margaritta', "Valeriy"]
# 2. list.insert(index, element)
users.insert(0, 'Mahliyoxon')
# ['Mahliyoxon', 'Gulyora', "G'ulomjon", 'John', 'Margaritta', "Valeriy"]
print(users)
users.insert(2, 'Cristiano')
print(users)
users.insert(len(users) - 1, 'Nodir')
print(users)
# Element o'chirish
# 1. del operator
del users[4]
print(users)
# 2. list.remove(element)
users.remove("Mahliyoxon")
print(users)
users.remove(users[2])
print(users)

# Listdan element sug'urib olish
# list.pop(index?)
deletedElement = users.pop(1)
print(deletedElement)
print(users)

lastElement = users.pop()
print(lastElement)
print(users)