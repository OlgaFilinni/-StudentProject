synonym_dict = {'красиво': 'превосходно', 'печально': 'грустно', 'весело': 'радостно'}
# for i in range(int(input('Введите количество пар слов: '))):
#     word_a, word_b = input('{} пара: '.format(i + 1)).lower().split(' - ')
#     synonym_dict[word_a] = word_b
print(synonym_dict)

while True:
    word = input('Введите слово ').lower()
    for key in synonym_dict:
        if word == key:
            print('Синоним:', synonym_dict[key])
            break
        elif synonym_dict[key] == word:
            print('Синоним:', key)
            break

    else:
        print("Такого слова нет!")





