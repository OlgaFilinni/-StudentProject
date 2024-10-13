# Значащие имена функций



def add_contact(book_contact):
    name = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").split())
    if name in book_contact:
        print("Такой человек уже есть в контактах.")
    else:
        number = input("Введите номер телефона: ")
        book_contact[name] = number

    # return data


# see 1
def find_contact(book_contact):
    search_user = input("Введите фамилию для поиска: ").lower()
    for contact, number in book_contact.items():
        _, last_name = contact
        if search_user == last_name.lower():
            print(contact, number)


phonebook_dict = dict()

while True:
    print("Введите номер действия: \n 1. Добавить контакт \n 2. Найти человека")
    choice_user = int(input())
    if choice_user == 1:
        add_contact(phonebook_dict)
        print("Текущий словарь контактов: ", phonebook_dict)

    if choice_user == 2:
        find_contact(phonebook_dict)


