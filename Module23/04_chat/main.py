name_user = input("Как Вас зовут? ")
while True:
    print("Чтобы увидеть текущий текс чата введите 1, чтобы написать сообщение введите 2")
    response = input("Введите 1 или 2: ")
    if response == "1":
        try:
            with open("chat.txt", "r", encoding="utf-8") as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока ничего нет\n")
    elif response == "2":
        new_messeges = input("Введите сообщение: ")
        with open("chat.txt", "a", encoding="utf-8") as file:
            file.write("{name}: {messages}\n".format(
                name=name_user, messages=new_messeges))
    else:
        print("Неизвестная команда\n")
