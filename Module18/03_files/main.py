def checking_start(file_path):
    no_char = r"@№$%^&\*()"
    for char in no_char:
        if file_path.startswith(char):
            print("Ошибка: название начинается на один из специальных символов.")
            return False
        else:
            return True


user_file_path = input("Введите путь к файлу: ")
start_file_path = checking_start(user_file_path)
if start_file_path:
    if user_file_path.endswith(".txt") or user_file_path.endswith(".docx"):
        print("Файл назван верно.")
    else:
        print("неверное расширение файла. Ожидалось .txt или .docx.")