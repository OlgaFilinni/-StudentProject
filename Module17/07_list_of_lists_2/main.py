nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list_2 = [v for l1 in nice_list for l2 in l1 for v in l2]
print(nice_list_2)

