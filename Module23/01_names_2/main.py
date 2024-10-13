def len_char(line):
    return len(line.strip())


count_char = 0
number_line = 0
with open("people.txt", "r", encoding="utf-8") as file_name:
    for name in file_name:
        number_line += 1
        count_char += len_char(name)
        try:
            if len_char(name) < 3:
                raise ValueError
        except ValueError:
            print(f"Ошибка: менее трёх символов в строке {number_line}")

print(f"Общее количество символов: {count_char}")
