from string import ascii_letters


def is_english_alpha(sym: str) -> bool:
        return sym in ascii_letters


def ascii_only(text):
    new_str = ""
    for sym in text:
        if is_english_alpha(sym):
            new_str += sym

    return new_str

def count_char(line):
    count_letter = {}
    for char in line:
        if char in count_letter:
            count_letter[char] += 1
        else:
            count_letter[char] = 1


    return count_letter


def frequency_analysis(letter_data, lenght):
    for key, value in letter_data.items():
        letter_data[key] = round(value / lenght, 3)

    return letter_data




file = open('text.txt')
text = file.read()
new_text = ascii_only(text)
len_new_text = len(new_text)

print(new_text)
letters = count_char(new_text)

freg_letters = frequency_analysis(letters, len_new_text)

sorted_freg_letter = sorted(freg_letters.items(), key=lambda x: (-x[-1], x[0]))

analysis_and_sort = dict(sorted_freg_letter)
elem_file = open("analysis.txt", "w", encoding="utf-8")
elem_file.write("Содержимое файла 'analysis.txt'\n")
text = ""
for key, value in analysis_and_sort.items():
    text += f"{key}: {value}\n"

elem_file.write(text)

