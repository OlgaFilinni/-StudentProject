# list_2 =[]
#
# for i in range(1, 5):
#     for j in range(1):
#         list_2.append(list(range(i, 13, 4)))


#print(list_2)

list_3 = [[j for j in range(i, 13, 4)] for i in range(1, 5)]
print(list_3)

