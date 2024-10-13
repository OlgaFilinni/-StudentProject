import math


def get_sage_sqrt(num):
    try:
        math.sqrt(num)
    except ValueError:
        print(f"Нельзя передавать отрицитальное число: {num}")
    except TypeError:
        print(f"Ошибка. Вы ничего не ввели или ввели символы: {num}")
    except Exception as error:
        print(f"При обработке {num} произошла непредвиденная ошибка {error}")
    else:
        return math.sqrt(num)


numbers = [16, 25, -9, 0, 4.5, "abc", '']
for number in numbers:
    result = get_sage_sqrt(number)
    if result is not None:
        print(f"Квадратный корень numbers {number}: {result}")
