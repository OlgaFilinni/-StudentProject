import copy
import json

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def deep_copy(structure):
    if isinstance(structure, (int, float, str, bool)):
        return structure
    elif isinstance(structure, list):
        return [deep_copy(item) for item in structure]
    elif isinstance(structure, dict):
        return {key: deep_copy(value) for key, value in structure.items()}
    else:
        return copy.deepcopy(structure)


def find_param(mass, key, new_value):
    if key in mass:
        mass[key] = new_value
        return True

    for sub_mass in mass.values():
        if isinstance(sub_mass, dict):
            result = find_param(sub_mass, key, new_value)
            if result:
                break
    else:
        result = None

    return result


dict_site = {}
count_site = int(input("Введите количество сайтов: "))
for _ in range(count_site):
    name_site = input("Введите название продукта для нового сайта: ")
    copy_site = deep_copy(site)
    find_param(copy_site, key='h2', new_value="У нас самая низкая цена на {}".format(name_site))
    find_param(copy_site, key='title', new_value="Куплю/продам {} недорого".format(name_site))

    dict_site["Сайт для {}".format(name_site)] = copy_site
    json_site = json.dumps(dict_site, indent=4, ensure_ascii=False)

    print(json_site)

# from pprint import pprint


