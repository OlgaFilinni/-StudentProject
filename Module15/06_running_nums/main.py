# РЕШЕНИЕ 1
list_a = [1, 4, -3, 0, 10]
new_list = []
shift = int(input("СДВИГ: "))

for i in range(shift - 1, len(list_a)):
    new_list.append(list_a[i])

for i in range(shift - 1):
    new_list.append(list_a[i])

print(new_list)

# РЕШЕНИЕ 2
# a = [1, 4, -3, 0, 10]
# new_list = [] # new list

# shift = int(input("СДВИГ: ")) #3
# for i in range(len(a)):   # 5 01234
#     if i >= shift - 1:
#         new_list.append(a[i])

# for i in range(len(a)):
#     if i < shift - 1:
#         new_list.append(a[i])

# print(new_list)


# РЕШЕНИЕ 3
# def shift(list):
#     new_list = []
#     new_list.append(list[-1])
#     for i in range(len(list) - 1):
#          new_list.append(list[i])
#     return new_list


# user_shift = int(input("СДВИГ: "))
# for _ in range(user_shift):
#     a = shift(a)
# print(a)