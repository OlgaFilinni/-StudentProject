people = int(input("Кол-во человек: "))
leave = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", str(leave) + "-й человек")

list_people = list(range(1, people + 1))
print("")
index = 0
while len(list_people) > 1:
    print("Текущий круг людей: ", list_people)
    print("Начало счёта с номера", list_people[index])
    index = (index + leave - 1) % len(list_people)
    print("выбывает человек под номером: ", list_people.pop(index))
    print("")
    if index == len(list_people):
        index = 0

print("Остался человек под номером",  list_people[0])
