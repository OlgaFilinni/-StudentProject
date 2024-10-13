def super_sum(mass):
    elem_sum = 0
    for elem in mass:
        if isinstance(elem, int):
            elem_sum += elem

        else:
            elem_sum += super_sum(elem)

            # print(elem_sum)
    return elem_sum

# mass = [1,2,3,[6,7,8,5],(4,5,7), 77]
# elem_sum = 0

# resul = super_sum(mass)
# print(resul)
