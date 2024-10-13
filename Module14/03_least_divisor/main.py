import math
number = int(input("Введите число: "))
for dev in range(2, int(math.sqrt(number))+1):
    if not number % dev:
        print("Наименьший делитель: ", dev)
        break
else:
    print("Наименьший делитель: ", number)
