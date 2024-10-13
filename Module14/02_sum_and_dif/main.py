def sum_digit(number):
    count_sum = 0
    while number > 0:
        count_sum += number % 10
        number //= 10

    return count_sum


def count_digit(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

number_user = int(input("Введите число: "))
sum = sum_digit(number_user)
general_count = count_digit(number_user)
print("Сумма цифр равна: ", sum)
print("Количество цифр равно: ", general_count)
print("Разность: ", sum - general_count)
