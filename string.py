# String - matn
# Data types(Ma'lumot turlari): 1. string(matn) 2. number(son) 3. Boolean(Mantiqiy)
region = "Xorazm"
city = 'Shovot'
street = "Al-Xorazmiy"
emoji = "🔥"
firstname = "Asadbek"
lastname = "Raximov"

# Matnlarni qo'shish(birlashtirish)
# "Men Xorazm viloyati Shovot tumanida yashayman"
address = "Men " + region + " viloyati " + city + " tumanida yashayman"
text = "Mening ismim " + firstname
full_name = "Mening to'liq ism familyam " + firstname + " " + lastname
print(full_name)
print(address)
print(text)

# f-string
name = f"Mening to'liq ism familyam {firstname} {lastname}"
full_address = f"Men {region} viloyati {city} tumanida yashayman"
print(name)
print(full_address)

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

# String metodlari(methods)
firstname = "John"
lastname = "Doe"
fullname = f"{firstname} {lastname}" # John Doe
# upper() / lower()
print(fullname.upper()) # JOHN DOE
print(fullname.lower()) # john doe
print(fullname) # John Doe
print('Adminjon'.upper())
# title() / capitalize()
print('Welcome to uzbekistan'.title()) # Welcome To Uzbekistan
print("Where are you from?".title())
print('manual tester'.capitalize())
fullname = fullname.capitalize() # John doe
print(fullname) 

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

# input()
# nickname1 = 'rajabboyeva1'
# nickname2 = input("Iltimos, instagram nicknameni kiriting:")
# print("1-account:", nickname1)
# print("Foydalanuvchi accounti:", nickname2)

# Amaliyot
kocha = input("Iltimos, ko'changizni kiriting: ")
mahalla = input("Iltimos mahallangizni kiriting: ")
tuman = input("Iltimos tumaningizni kiriting: ")
viloyat = input("Iltimos viloyatingizni kiriting: ")
manzil = f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

