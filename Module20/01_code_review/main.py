students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
# TODO:

#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

def len_surname(students_info):
    surname_len_sum = 0
    for student in students_info.values():
        surname_len_sum += len(student["surname"])

    return surname_len_sum


def list_interests(students_info):
    res = []
    for student in students_info.values():
        res.extend(student["interests"])

    return res


pair_id_age = [(key, students[key]["age"]) for key in students]

sum_surname_students, list_interests_students = len_surname(students), list_interests(students)

print("Список пар 'ID студента — возраст': ", pair_id_age)
print("Полный список интересов всех студентов: ", list_interests_students)
print("Общая длина всех фамилий студентов: ", sum_surname_students)
