# Function - ma'lum vazifani bajaruvchi kod bloki. 
# Funksiya yaratish uchun def kalit so'zidan foydalanamiz
# Pythondagi tayyor funksiyalar - print(), input(), len(), list() va boshqalar.
print("Hello World")
# Funksiyani e'lon qilish(declaration)
# def salom_ber():
#     print("Salom, dunyo!")

# # Funksiyani chaqirish(call)
# salom_ber() # Natija: Salom, dunyo!
# salom_ber() # Natija: Salom, dunyo!

# Funksiyada parameterlar, argumentlar
def salom_ber(ism):
    print(f"Assalomu alaykum, {ism}!")

salom_ber("Ali")
salom_ber("Vali")
salom_ber("Olim")
salom_ber("Gulbahor ammam")

def yigindi(a, b):
    print(a + b)

yigindi(7, 8) # Natija: 15
yigindi(10, 20) # Natija: 30

# default parameterlar va default argumentlar
def calculate_age(birth_year=1995, name="Olim"):
    age = 2026 - birth_year
    print(f"{name}ning yoshi: {age}")

calculate_age(2005, "Ismoil")
calculate_age(2010, "Jumagul")
calculate_age()

def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1995, 2020)
