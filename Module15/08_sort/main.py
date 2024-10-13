list_a = [1, 4, -3, 0, 10]
def sortt(list_a):  #пузырьковая сортировка
    for i in range(len(list_a)-1):
        for j in range(len(list_a) - 1):
            if list_a[j] > list_a[j + 1]:
                list_a[j + 1], list_a[j] = list_a[j], list_a[j + 1]
    return list_a


print("Отсортиррованный список: ", sortt(list_a))

