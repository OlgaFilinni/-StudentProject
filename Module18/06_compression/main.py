s_user = input("Введите строку: ")
s_code = []
count_i = 1
for i in range(len(s_user) - 1):
    if s_user[i] == s_user[i + 1]:
        count_i += 1
    else:
        s_code.append(s_user[i] + str(count_i))
        count_i = 1

s_code.append(s_user[-1] + str(count_i))
print("Закодированная строка: ", "".join(s_code))