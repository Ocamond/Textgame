class Weapon:
    def __init__(self,name,description,damage,value):
        self.name = name 
        self.description = description
        self.damage = damage
        self.value = value

    def __str__(self):
        return self.name

Rock = Weapon("Rock", 
             "Its a big rock you can hit enemies with it",
             5,5)

Dagger = Weapon("Dagger",
                "A small dagger woth some rust." and "Somewhat mire dangerous than a rock.",
                10,20)

Rustysword = Weapon("Rustysword",
                    "This sword is showing its age," and "but still has some fight in it",
                    20, 100)

class Consumable:
    def __init__(self,name, healing_value, value):
        self.name = name
        self.healing_value = healing_value
        self.value = value

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing_value)

CrustyBread = Consumable("CrustyBread",10, 12)

Apple = Consumable("Apple",5,6)

HealingPotion = Consumable("Healing Potion", 50, 100)

class Sellable:
    def __init__(self, name, value):
        self.name = name 
        self.value = value 
    
    def __str__(self):
        return self.name

GoldRing = Sellable("Gold ring", 150)

Web = Sellable("Web",5)

BearFur = Sellable ("Bear Fur", 15)
