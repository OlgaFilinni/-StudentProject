class Student:
    grades = [1, 2, 3, 4, 5]

    def __init__(self, name, grade, number_group):
        self.name = name
        self.grade = grade
        self.number_group = number_group

    def grade_value(self):
        if self.grade in self.grades:
            
            return True
        return False
    

    def __repr__(self):
        return f"ФИ студента: {self.name}\n" \
               f"Успеваемость в баллах: {self.grade}\n" \
               f"Группа {self.number_group}"

    def __str__(self):
        return f"Студент: {self.name}\n" \
           f"Успеваемость в баллах: {self.grade}\n" \
           f"Номер группы: {self.number_group}"


students = []

while len(students) < 3:
        n_student = Student(
            name=input("ФИ студента: "),
            grade=int(input("Оценка успеваемости по 5 бальной школе: ")),
            number_group=int(input("Номер группы: "))
        ) 
        if n_student.grade_value():
            students.append((n_student))
            print(f"\n*** {n_student} добавлен в список***\n")
        else:
            print(f"Оцените по ПЯТИБАЛЬНОЙ шкале.Введите данные студента {n_student.name} заново.")

sorted_data_list = sorted(students, key=lambda x: x.grade)

def print_students(all_student):
    for student in all_student:
        print(student, "\n")
print("Список студентов по возрастанию успеваемости:\n")
print_students(sorted_data_list)


