def is_poly(string):
    char_dict = {}
    for sym in string:
        char_dict[sym] = char_dict.get(sym, 0) + 1

    odd_count = 0
    for value in char_dict.values():
        if value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


my_string = input("Введите строку: ")
if is_poly(my_string):
    print("Можно сделать палиндром")
else:
    print("Нельзя сделать палиндром")
