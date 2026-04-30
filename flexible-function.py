# Return function
# def sum_list(lst):
#     s = 0
#     for element in lst:
#         s += element

#     return s

# print(sum_list([18, 75, -89, 7, 10]))

# Flexible(moslashuvchan) function
# *args usuli
# def summa(*numbers):
#     # print(numbers) (a, b, c, ...)
#     # print(type(numbers)) tuple
#     s = 0
#     for number in numbers:
#         s += number
#     return s

# print(summa(12, 50, 89, -89, 0, -77))
# print(summa(15, 52, 82))

# def my_func(*people):
#     print(f"The youngest person is {people[1]}")

# my_func("Jumagul", "Akmal", "Ahror")
# my_func("Oysara", "Tojivoy", "Qo'zivoy", "Gulbahor")

# def summa(x, y = 5, *sonlar):
#     return x + y + sum(sonlar)

# print(summa(1, 7, 8, -26, -5, 18, 74, -100))
# print(summa(5, 12))

# **kwargs(keyword arguments) usuli
def avto_info(kompaniya, model, **malumotlar):
    # print(malumotlar) {'key': value}
    # print(type(malumotlar)) dict
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model

    return malumotlar

print(avto_info("GM Uzbekistan", "Cobalt", rangi="Oq", narhi=120000))
print(avto_info("Merc", "Gelikvogen", rangi="Qora", narhi=350000))

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# Amaliyot
# 1.
# def multiply(*numbers):
#    s = 1
#    for number in numbers:
#       s *= number

#    return s
   
# print(multiply(2, 4, 7))
# 2.
# def student_info(name, lastname, **data):
#     data['name'] = name
#     data['lastname'] = lastname
    
#     return data
# print(student_info('Jumagul', 'Umrzoqova', year = 2005, height = 1.65))

# find_max()
def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value

print(find_max(8, 15, -3, 0, 9, 12))
print(find_max(-2, -5, -7))
print(find_max())