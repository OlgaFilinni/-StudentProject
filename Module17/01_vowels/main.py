def is_letter_vowel(letter, list_vowel):
    for i in list_vowel:
        if i == letter:
            return True

    return False


list_vowel = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
text = input("Введите текст: ")
new_text = [x for x in text if is_letter_vowel(x, list_vowel)]


print("Список гласных букв:", new_text)
print("Длина списка: ", len(new_text))