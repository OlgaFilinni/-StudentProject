user_str = input("Введите строку: ").split()
list_len_word = [len(i) for i in user_str]
max_len = 0
for i in list_len_word:
    if i > max_len:
        max_len = i
print("Самое длинное слово:", user_str[list_len_word.index(max_len)])
print("Длина этого слова:", max_len)

