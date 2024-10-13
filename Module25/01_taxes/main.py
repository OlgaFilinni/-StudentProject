class Property:
    """Базовый класс, описывающий имущество"""

    def __init__(self, worth):
        self.set_worth(worth)

    def __str__(self):
        return f"Налог на имущество рассчитан: {self.tax_calculation()}"

    def set_worth(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def tax_calculation(self, ratio=1):
        tax = 1 / ratio * self.get_worth()
        return tax


class Apartment(Property):

    def __str__(self):
        return f"Налог на дом рассчитан: {self.tax_calculation()}"

    def tax_calculation(self, ratio=1000):
        tax = 1 / ratio * self.get_worth()
        return tax


class Car(Property):

    def __str__(self):
        return f"Налог на машину рассчитан: {self.tax_calculation()}"

    def tax_calculation(self, ratio=200):
        tax = 1 / ratio * self.get_worth()
        return tax


class CountryHouse(Property):
    def __str__(self):
        return f"Налог на загородный дом рассчитан: {self.tax_calculation()}"

    def tax_calculation(self, ratio=500):
        tax = 1 / ratio * self.get_worth()
        return tax


print("Добро пожаловать в Налоговую! \n"
      "Вам необходимо оплатить налог за: \nДом \nМашину \nЗагородный дом")
worth_apartment = float(input("Укажите стоимость дома: "))
worth_car = float(input("Укажите стоимость машины: "))
worth_сountry_house = float(input("Укажите стоимость загородного дома: "))
money_taxpayer = 80000000000
apartment, car, country_house = Apartment(worth_apartment), \
    Car(worth_car), \
    CountryHouse(worth_сountry_house)
print(apartment)
print(car)
print(country_house)
total_tax = apartment.tax_calculation() \
            + car.tax_calculation() \
            + country_house.tax_calculation()
print(f"Итого необходимо заплатить: {total_tax}. На вашем счете {money_taxpayer}")
if money_taxpayer - total_tax < 0:
    print("Денег не хвататает")
else:
    print("Налог оплачен!")
