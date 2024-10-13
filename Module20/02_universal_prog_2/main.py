def crypto(lst):
    return [elem for i_index, elem in enumerate(lst) if is_prime(i_index)]


def is_prime(number):
    if number == 0 or number == 1:
        return False


    # Если хотя бы один делитель есть, то число непростое
    # Отличные от 1 и самого числа
    for dev in range(2, number // 2 + 1):
        if number % dev == 0:
            return True

    return False


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


