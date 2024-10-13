ip_user = input("Введите IP: ").split(".")
if len(ip_user) != 4:
    print("Адрес — это четыре числа в пределах от 0 до 255, разделённые точками.")
else:
    for elem in ip_user:
        if not elem.isdigit():
            print(elem, "— это не целое число.")
            break
        if int(elem) < 0 or int(elem) > 255:
            print(elem, "превышает 255.")
            break
    else:
        print("IP-адрес корректен.")

