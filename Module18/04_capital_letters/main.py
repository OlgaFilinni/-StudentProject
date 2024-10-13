user_str = input("Введите строку: ").split()
new_str = ''
for word in user_str:
    new_word = word[0].upper() + word[1:]
    new_str = new_str + ' ' + new_word

print(new_str)














