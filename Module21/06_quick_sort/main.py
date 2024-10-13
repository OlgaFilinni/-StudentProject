nums = [5, 8, 9, 4, 2, 9, 1, 8]


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       last_num = nums[-1]
       small_nums = []
       max_nums = []
       equal_nums = []
       for n in nums:
           if n < last_num:
               small_nums.append(n)
           elif n > last_num:
               max_nums.append(n)
           else:
               equal_nums.append(n)
       return quicksort(small_nums) + equal_nums + quicksort(max_nums)


print(quicksort(nums))