def print_nums(num):
    if num <= 0:
        return num

    print_nums(num - 1)
    print(num)


print_nums(10)
