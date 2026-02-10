# Takrorlanish operatorlari
# loop - sikl
# 1. for loop
# 2. while loop
students = ['Elbek', 'Maftuna', "G'ulomjon", "Mahliyo", "Dilbek"],
# hard coding
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
for student in students:
    print(student)

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
for student in students:    
    print(student)

# 1-iteratsiya student = "Alice"
# 2-iteratsiya student = "Bob"
# 3-iteratsiya student = "Charlie"
# 4-iteratsiya student = "David"    
# 5-iteratsiya student = "Eve"

for guest in students:
    print(f"Hurmatli {guest}, sizni interviewga taklif qilmoqchiman.")
    print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.")

# Sonlar ro'yxati uchun for loop
even_numbers = list(range(2, 51, 2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'yxati
for number in even_numbers:
    print(number)

print("Dastur tugadi.")

# 1 ning kvadrati 1 ga teng.
# 2 ning kvadrati 4 ga teng.
# 3 ning kvadrati 9 ga teng. 
sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
for son in sonlar:
    print(f"{son} ning kvadrati {son ** 2} ga teng.")