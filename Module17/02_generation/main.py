import random


number = int(input("Введите длину списка: "))
list_numbers = [(1 if x % 2 == 0 else x % 5) for x in list(range(0, number))]

print(list_numbers)