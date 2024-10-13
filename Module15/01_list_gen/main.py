number = int(input("Введите целое число: "))
list_odd_integer = []

for digit in range(number + 1):
    if digit % 2 != 0:
        list_odd_integer.append(digit)

print("Список из нечётных чисел от одного до", number, ":", list_odd_integer)


