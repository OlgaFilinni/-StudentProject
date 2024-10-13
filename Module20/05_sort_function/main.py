def has_only_int(tpl):
    for elem in tpl:
        if not isinstance(elem, int):
            return False

    return True


def tpl_bubble_sort(tpl):
    if has_only_int(tpl):
        mas, len_mas = list(tpl), len(tpl)
        for _ in range(len_mas - 1):
            for i in range(len_mas - 1):
                if mas[i] > mas[i + 1]:
                    mas[i], mas[i + 1] = mas[i + 1], mas[i]
        return tuple(mas)

    return tpl


print(tpl_bubble_sort((5, 8, 4, 1, 11, 8, 2)))
