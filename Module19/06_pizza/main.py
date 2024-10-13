count_order = int(input("Введите количество заказов: "))

# remove i
# Не рекомендуется использовать название типа в переменных. Это избыточно
parsed_order = {}
for order in range(count_order):  
    print("Заказ {}:".format(order + 1))
    name, pizza, count = input().split()

    if name not in parsed_order:
        parsed_order[name] = {}
    user_orders = parsed_order[name]
    # if pizza not in parsed_dict_order[name]:
    #     parsed_dict_order[name][pizza] = 0
    user_orders[pizza] = user_orders.get(pizza, 0) + int(count)

parsed_list_order = sorted([(key, value) for key, value in parsed_order.items()])
# parsed_dict_order = {k: v for k, v in parsed_list_order}
parsed_order = dict(list(parsed_list_order))
# print(parsed_dict_order)

for user in parsed_order:
    print("{}:".format(user))

    for pizza, count in parsed_order[user].items():
        print('{}: {}'.format(pizza, count))
