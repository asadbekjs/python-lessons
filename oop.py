# OOP - Object Oriented Programming(Obyektga yo'naltirilgan dasturlash)
# 1. Class(Object uchun shablon, qolip) va Object
# 2. OOP ustunlari:
    # 1. Encapsulation
    # 2. Inheritance(Meros, vorislik)
    # 3. Polymorphism
    # 4. Abstraction

class Car:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def start(self):
        print(f"{self.model} is starting...")

car1 = Car("gentra", 'black', 15000)
print(car1)
car1.start()
car2 = Car("cobalt", 'white', 13000)
car2.start()
