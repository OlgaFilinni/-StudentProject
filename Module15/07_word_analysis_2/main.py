word = input("Введите слово: ")
reversed_word = ""
for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]

if reversed_word == word:
    print("Слово является палиндромом")

