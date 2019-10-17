import items

class Enemy:
    def __init__ (self, name, hp,damage,gold,inventory):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold
        self.inventory = inventory
 
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0

GiantSpider = Enemy("Giant Spider", 10, 2, 5, [items. Web])

Ogre = Enemy("Ogre", 30, 10, 10, [items.Rock])

Bear = Enemy("Bear", 100, 4, 20, [items.BearFur])

Wolf = Enemy("Wolf", 80, 15, 50,[])

class BossEnemy:
    def __init__(self,name, hp, damage, gold, inventory):
        self.name = name 
        self.hp = hp
        self.damage = damage
        self.gold = gold
        self.inventory = inventory
    
    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0
        
RedSpider = BossEnemy("Red Spider", 100, 15, 100,[items.GoldRing])
