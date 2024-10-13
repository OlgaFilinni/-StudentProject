def code(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != " " else " ") for sym in string]
    new_str = ""
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
input_str = input("Введите строку: ")
shift = int(input("Введите сдвиг: "))

output_str = code(input_str, shift)

print("Зашифрванная строка: ", output_str)