# Takrorlanish operatorlari
# loop - sikl
# 1. for loop
# 2. while loop
# students = ['Elbek', 'Maftuna', "G'ulomjon", "Mahliyo", "Dilbek"],
# hard coding
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# for student in students:
#     print(student)

# students = ["Alice", "Bob", "Charlie", "David", "Eve"]
# for student in students:    
#     print(student)

# 1-iteratsiya student = "Alice"
# 2-iteratsiya student = "Bob"
# 3-iteratsiya student = "Charlie"
# 4-iteratsiya student = "David"    
# 5-iteratsiya student = "Eve"

# for guest in students:
#     print(f"Hurmatli {guest}, sizni interviewga taklif qilmoqchiman.")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.")

# # Sonlar ro'yxati uchun for loop
# even_numbers = list(range(2, 51, 2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'yxati
# for number in even_numbers:
#     print(number)

# print("Dastur tugadi.")

# 1 ning kvadrati 1 ga teng.
# 2 ning kvadrati 4 ga teng.
# 3 ning kvadrati 9 ga teng. 
# sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.")

# numbers = list(range(20))
# start_default_value = 0
# stop = 20
# step_default_value = 1
# print(numbers)
# for number in numbers:
#     print(number)

# names = ['Elbek', 'Maftuna', "G'ulomjon", "Mahliyo", "Dilbek", 'Sherzodbek'],
# for name in names:
#     print(name)

# 1 dan 100 gacha chiqarish
# 1-usul:
sonlar2 = list(range(1, 100))
for son in sonlar2:
    print(son)
# 2-usul:
for son in range(1, 100):
    print(son)

# ro'yxat elementlarini index orqali olish:
for index in range(len(sonlar2)):
    print(index)
    print(sonlar2[index])

# 1-marta: index = 0 => sonlar[0] = 1
# 2-marta: index = 1 => sonlar[1] = 2
# ...
# 99-marta: index = 98 => sonlar[98] = 99

# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng
for number in range(1, 20):
    print(f"{number} ning kvadrati {number ** 2} ga teng")

number_of_friends = int(input("Do'stlaringiz sonini kiriting: "))
friends = []
if (number_of_friends == 0):
    print("Sizning do'stingiz yo'qmi? ")
else:
    for n in range(number_of_friends):
        friend = input(f"{n + 1}-do'stingizni kiriting: ")
        friends.append(friend)
    print(friends)