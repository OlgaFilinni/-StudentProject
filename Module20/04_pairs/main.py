import random

RANDOM_LIST_LEN = 10

random_list = [random.randint(1,100) for i in range(RANDOM_LIST_LEN)]
print(random_list)

list_tuple = [(random_list[i], random_list[i + 1]) for i in range(0, RANDOM_LIST_LEN, 2)]

print(list_tuple)

# решение 2
list_tuple_2 = [(number, random_list[i_index + 1]) for i_index, number in enumerate(random_list)
                if i_index % 2 == 0]

print(list_tuple_2)
