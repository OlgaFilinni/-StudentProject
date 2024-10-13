import random

class Human():

    def __init__(self, name, home):
        self.name = name
        self.food_level = 50
        self.home = home

    def to_food(self):
        print("{} кушает(уровень сытости {})".format(self.name, self.food_level))
        self.food_level += 10
        self.home.full_refrigerator -= 10

    def to_work(self):
        print("{} ушёл на работу(уровень сытости {})".format(self.name, self.food_level))
        self.food_level -= 10
        self.home.money += 10

    def to_play(self):
        print("{} играет(уровень сытости {})".format(self.name, self.food_level))
        self.food_level -= 10

    def go_to_magazin(self):
        print("{} ушёл в магазин(уровень сытости {})".format(self.name, self.food_level))
        self.food_level += 10
        self.home.money -= 10

    def one_day_of_life(self):
        if self.food_level > 0:
            roll_the_dice = random.randint(1, 6)
            if self.food_level < 20 and home.full_refrigerator >= 10:
                self.to_food()
            elif home.money > 50:
                self.go_to_magazin()
            elif home.money < 50:
                self.to_work()
            elif roll_the_dice == 1:
                self.to_work()
            elif roll_the_dice == 2:
                self.to_food()
            else:
                self.to_play()
        else:
            print("{} RIP".format(self.name))
            return True


class Home:

    def __init__(self):
        self.full_refrigerator = 50
        self.money = 0


home = Home()
one_human = Human("Иван", home)
two_human = Human("Толик", home)

for _ in range(365):
    if one_human.one_day_of_life() or two_human.one_day_of_life():
        break



