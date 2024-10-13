password = input("Введите пароль: ")
count_digit = 0
count_upper = 0
for i in password:
    if i.isdigit():
        count_digit += 1
    if i.isupper():
        count_upper += 1

if count_digit < 3 or count_upper < 1 or len(password) < 8:
    print("Пароль ненадёжный. Попробуйте ещё раз")
else:
    print("Это надёжный пароль!")
