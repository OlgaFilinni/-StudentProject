
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10,11]
def merge_lists(list1, list2):
   res1 = []
   while list1 and list2:
      if list1[0] < list2[0]:
         res1.append(list1.pop(0))
      else:
         res1.append(list2.pop(0))

   res1 += list1
   res1 += list2

   return res1

def merge_sorted_lists(list1, list2):
   res1 = merge_lists(list1, list2)
   res2 = []

   for i in range(len(res1) - 1):
      if res1[i] != res1[i + 1]:
         res2.append(res1[i])

   res2.append(res1[-1])

   return res2


merged = merge_sorted_lists(list1, list2)
print(merged)