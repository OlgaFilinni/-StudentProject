# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
def sortt(list_a):
    for i in range(len(list_a)-1):
        for j in range(len(list_a) - 1):
            if list_a[j] < list_a[j + 1]:
                list_a[j + 1], list_a[j] = list_a[j], list_a[j + 1]
    return list_a


for i in numbers_list:
    if i % 2 != 0:
        numbers_list.remove(i)

print(sortt(numbers_list))