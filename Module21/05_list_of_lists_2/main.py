nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unpacking_list(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(unpacking_list(elem))
        else:
            result.append(elem)
    return result


print(unpacking_list(nice_list))
