class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.all_babys = []

    def make_calm(self):
        for baby in self.all_babys:
            if baby.mood == 0:
                print("Настроение {}: {}".format(baby.name, baby.state_mood[baby.mood]))
                baby.mood = 1
                print("Вы успокоили ребенка")

    def to_feed(self):
        for baby in self.all_babys:
            if baby.hunger == 1:
                print("Состояние голода у {}: {}".format(baby.name, baby.state_hunger[baby.hunger]))
                baby.hunger = 0
                print("Вы покормили ребенка")

    def add_baby(self, baby):
        if int(self.age) - int(baby.age) > 16:
            self.all_babys.append(baby)
        else:
            raise ValueError("Ошибка возраста! Родитель должен быть старше ребенка минимум на 16 лет.")

    def print_info(self):
        print("Меня зовут {}.\n"
              "Мне {} лет\n"
              "У меня {} детей".format(self.name, self.age, len(self.all_babys)))


class Baby:
    state_mood = {0: "встревожен", 1: "спокоен"}
    state_hunger = {1: "голоден", 0: "сыт"}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mood = 0
        self.hunger = 1


parent1 = Parent("Лиля", 33)

for _ in range(2):
    name = input("Введите имя ребенка: ")
    age = input("Введите возраст ребенка: ")
    baby = Baby(name, age)
    parent1.add_baby(baby)
parent1.print_info()
parent1.make_calm()
parent1.to_feed()
