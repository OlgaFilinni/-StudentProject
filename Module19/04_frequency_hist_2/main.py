inverted_data = {}

text = input("Введите текст: ")
data = {letter: text.count(letter) for letter in text}

for letter, count in data.items():
    print(letter, ":", count)
    if count not in inverted_data:
        inverted_data[count] = []

    inverted_data[count].append(letter)

print("Инвертированный словарь частот:")

for key_count, list_letter in inverted_data.items():
    print(key_count, ":", list_letter)
