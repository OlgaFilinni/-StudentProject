list_roller = []
list_people = []
count_relevant = 0

count_roller = int(input("Кол-во коньков: "))
for i in range(count_roller):
    print("Размер", str(i + 1) + "-й", "пары: ", end = "")
    size_roller = int(input())
    list_roller.append(size_roller)
print()
count_people = int(input("Кол-во людей: "))
for j in range(count_people):
    print("Размер ноги", str(j + 1) + "-ого", "человека: ", end = "")
    size_foot = int(input())
    list_people.append(size_foot)


while list_people and list_roller:
        found = False
        for i in list_people:
            for j in list_roller:
                if i == j:
                    list_people.remove(i)
                    list_roller.remove(j)
                    count_relevant += 1
                    found = True
                    break
            if found:
                break
        if not found:
            break

print("Наибольшее кол-во людей, которые могут взять ролики: ", count_relevant)



