def is_valid_line(line):
    name, mail, age = line.split(" ")

    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы:")
    if "@" not in mail or "." not in mail:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку: SyntaxError")
    if not 10 <= int(age) <= 99:
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99: ")

    return True


file_original = open("registrations.txt", "r", encoding="utf-8")
file_log = open("registrations_bad.log", "w", encoding="utf-8")
file_good = open("registrations_good.log", "w", encoding="utf-8")

for line in file_original:
    line = line.strip()
    try:
        if is_valid_line(line):
            file_good.write(f"{line}\n")
    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        text = f'{line} {exc}\n'
        file_log.write(text)

file_original.close()
file_log.close()
file_good.close()
