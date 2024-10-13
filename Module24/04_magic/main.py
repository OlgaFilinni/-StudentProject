class Storm:
    
    def __str__(self):
        return "Шторм"
    


class Steam:
    
    def __str__(self):
        return "Пар"


class Mud:
    
    def __str__(self):
        return "Грязь"


class Lightning:
    
    def __str__(self):
        return "Молния"


class Dust:
    
    def __str__(self):
        return "Пыль"

class Lava:
    
    def __str__(self):
        return "Лава"

class Water:
    
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mud()
        return None


class Air:
    
    def __str__(self):
        return "Воздух"
        
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        return None


class Fire:
    
    def __str__(self):
        return "Огонь"
    
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        return None


class Earth:
    
    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        return None
    

fire = Fire()
air = Air()
earth = Earth()
water = Water()
print(water + air)
print(water + fire)
print(water + earth)
print(air + fire)
print(air + earth)
print(fire + earth)


