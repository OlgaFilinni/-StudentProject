import random

stop_number = 777
start_number = 0
fail_number = 2
while start_number < stop_number:
    user_number = int(input("Введите число: "))
    random_number = random.randint(1, 13)

    if random_number == fail_number:
        print("Вас постигла неудача!")
        raise BaseException
    start_number += user_number
    with open("out_file.txt", "a") as out_file_user:
        format_number = str(user_number)+"\n"
        out_file_user.write(format_number)

print("Вы успешно выполнили условие для выхода из порочного цикла!")
