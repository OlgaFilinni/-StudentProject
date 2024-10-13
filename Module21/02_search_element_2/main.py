site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_param(mass, key, max_level=None, actual_level=None):
    if max_level is not None:
        actual_level += 1

        if actual_level >= max_level:
            return None

    if key in mass:
        return mass[key]

    for sub_mass in mass.values():
        if isinstance(sub_mass, dict):
            result = find_param(sub_mass, key, max_level, actual_level)

            if result:
                break
    else:
        result = None

    return result


actual_level = -1
user_key = input("Какой ключ ищем? ")
level_search = input("Хотите ввести максимальную глубину? y/n: ").lower()
# level_search not in "y", "n":
while level_search != "y" and level_search != "n":
    level_search = input("Ошибка ввода: выберите y/n! Хотите ввести максимальную глубину? ").lower()


if level_search == "y":
    user_level = int(input("Введите максимальную глубину: "))
    value = find_param(site, user_key, user_level, actual_level)
if level_search == "n":
    value = find_param(site, user_key)


if value:
    print(value)
else:
    print("Такого ключа в структуре нет")

