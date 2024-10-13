import os


def count_dict_and_file(cur_path):
    dict_count = 0
    file_count = 0
    file_size = 0
    for run_object in os.listdir(cur_path):
        path = os.path.join(cur_path, run_object)
        if os.path.isfile(path):
            file_count += 1
            file_size += os.path.getsize(path)
        elif os.path.isdir(path):
            dict_count += 1
            res_dict_count, res_file_count, res_file_size = count_dict_and_file(path)
            dict_count += res_dict_count
            file_count += res_file_count
            file_size += res_file_size

    return dict_count, file_count, file_size

test_path = r"C:\Users\admin\PycharmProjects\Python_Basic"
end_dict_count, end_file_count, end_file_size = count_dict_and_file(test_path)
print("Путь", test_path)
print("Размер каталога (в Кб):", round(end_file_size / 1024, 1))
print("Количество подкаталогов:", end_dict_count)
print("Количество файлов:", end_file_count)


