class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon object")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning"
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust." and "Somewhat mire dangerous than a rock."
        self.damage = 10
        self.value = 20

class Rustysword(Weapon):
    def __init__(self):
        self.name = "Rustysword"
        self.description = "This sword is showing its age," and "but still has some fight in it"
        self.damage = 20
        self.value = 100

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing_value)

class CrustyBread(Consumable):
    def __init__(self):
        self.name = "CrustyBread"
        self.healing_value = 10
        self.value = 12

class Apple(Consumable):
    def __init__(self):
        self.name = "Apple"
        self.healing_value = 5
        self.value = 6

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 50

class Sellable:
    def __init__(self):
        raise NotImplementedError("Do not creat Raw Sellable")
    
    def __str__(self):
        return self.name

class Jewelry(Sellable):
    def __init__(self):
        self.name = "Gold ring"
        self.value = 150