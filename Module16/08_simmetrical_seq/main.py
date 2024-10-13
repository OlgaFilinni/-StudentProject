def is_symmetry_list(list):
    for i in range(len(list) // 2):
        if list[i] != list[-i - 1]:
            return False
    return True


nums = []
new_nums = []
answer = []
count_number = int(input("Кол-во чисел: "))
for i in range(count_number):
    print("Число: ", i + 1, end = " ")
    number = int(input())
    nums.append(number)

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_symmetry_list(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print("Последовательность: ", nums)
print("Нужно приписать чисел: ", len(answer))
print("Сами числа: ", answer)




