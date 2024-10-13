guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guest_control = ""

while guest_control != "пора спать":
    print("Сейчас на вечеринке ", len(guests), "человек: ", guests)
    guest_control = input("Гость пришел или ушел? ")
    if guest_control == "пришел":
        new_guest = input("Имя гостя: ")
        if len(guests) == 6:
            print("Прости", new_guest, "но мест нет.")

        else:
            print("Привет,", new_guest)
            guests.append(new_guest)
            print()

    if guest_control == "ушел":
        leave_guest = input("Имя гостя: ")
        print("Пока,", leave_guest)
        guests.remove(leave_guest)
        print()
    else:
        print("Кажется, вы ввели что-то не то...")

print("Вечеринка закончилась, все легли спать.")


