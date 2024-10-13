import random

class Berserk:
    name = "Воин"
    health_status = 100

    def __init__(self, number=0):
        self.number = number

    def damage(self):
        self.health_status -= 20

    def info_hit(self):
        print("\tАтаковал {} - {} ----->".format(self.name, self.number))

    def info_health(self):
        print("Состояние здоровья юнита {} - {}: {}".format(self.name, self.number, self.health_status))

    def victory_ode(self):
        print("***** Победил {} - {} *****".format(self.name, self.number))


print(r"/\/\/\/\/ Битва началась! /\/\/\/\/")
units = [Berserk(1), Berserk(2)]
while True:
    rand_int = random.randint(0, 1)
    print(rand_int)
    hitten = units[rand_int]
    damaged = units[1 - rand_int]
    hitten.info_hit()
    damaged.damage()
    damaged.info_health()
    if damaged.health_status <= 0:
        hitten.victory_ode()
        break


