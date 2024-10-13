import random


class KarmaException(Exception):
   pass


class KillError(KarmaException):
   pass


class DrunkError(KarmaException):
   pass


class CarCrashError(KarmaException):
   pass


class GluttonyError(KarmaException):
   pass


class DepressionError(KarmaException):
   pass


TARGET = 500
current_value = 0
kill = KillError("Ипортил карму, совершил убийство")
drunk = DrunkError("Ипортил карму, напился")
car_crash = CarCrashError("Ипортил карму, стал причиной автокатастрофы")
cluttony = CarCrashError("Ипортил карму, поддался чревоугодию")
depression = DepressionError("Ипортил карму, впал в депрессию")
sins = [kill, drunk, car_crash, cluttony, depression]

def one_day():
   num_error = 5
   num = random.randint(1, 10)
   bonus = random.randint(1, 7)
   if num == num_error:
      raise random.choice(sins)
   else: 
      return bonus

with open("karma.log", "w") as my_file:

   while TARGET > current_value:
         try:
            new_bonus = one_day()
            current_value += new_bonus
            my_file.write(f"Текущее значение кармы: {current_value}\n")
         except KarmaException as error:
            my_file.write(f"{error.__class__.__name__}: {str(error)}\n")

print("Достиг просветления!")
      
