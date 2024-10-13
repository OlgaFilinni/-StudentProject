def count_uppercase_lowercase(comments):
    count_uppercase = 0
    count_lowercase = 0
    for letter in comments:
        if letter.isupper():
            count_uppercase += 1
        elif letter.islower():
            count_lowercase += 1
    return count_uppercase, count_lowercase


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
