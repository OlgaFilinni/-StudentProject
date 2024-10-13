count_containers = int(input("Введите количество контейнеров: "))
list_container = []
new_list_container = []
for i in range(count_containers):
    weight = int(input("Введите вес контейнера в порядке невозростания: "))
    if weight > 200:
        weight = int(input("Вес не может превышать 200 кг. Введите вес следующего контейнера: "))
    else:
        list_container.append(weight)

# print(list_container)

new_weight = int(input("Введите вес нового контейнера: "))
if new_weight > 200:
    new_weight = int(input("Вес не может превышать 200 кг. Введите вес следующего контейнера: "))
count = 0
for i in list_container:
    if i > new_weight or i == new_weight:
        count +=1

print("Номер, который получит новый контейнер: ", count + 1)








