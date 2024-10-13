def is_valid_goods(list):
    for nested_list in range(len(list)):
        if list[nested_list][0] == search_goods:

            return True


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
search_goods = input("Название детали: ")
if is_valid_goods(shop):
    count_goods = 0
    amt_goods = 0
    for elem in range(len(shop)):
        if shop[elem][0] == search_goods:
            count_goods += 1
            amt_goods += shop[elem][1]
    print("Кол-во деталей — ", count_goods)
    print("Общая стоимость — ", amt_goods)

else:
    print("У нас такой детали нет")








