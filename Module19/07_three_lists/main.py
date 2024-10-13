array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 100]
array_3 = [3, 4, 15, 20, 30, 40, 70, 80, 120]

print("Задача 1.\nРешение с множествами:")
#print(set(array_1).intersection(set(array_2), set(array_3)))
print(set(array_1) & set(array_2) & set(array_3)) #амперсант

print("Решение без множеств:")
list_1 = []
for elem in array_1:
    if elem in array_2 and elem in array_3:
        list_1.append(elem)
print(list_1)

print("\nЗадача 2.\nРешение с множествами:")
print(list(set(array_1) - set(array_2 + array_3)))

print("Решение без множеств:")
list_2 = []
for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        list_2.append(elem)

print(list_2)
