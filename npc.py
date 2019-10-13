import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError ("Do not create raw NPC")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__ (self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                         items.CrustyBread(),
                         items.CrustyBread(),
                         items.Rustysword(),
                         items.HealingPotion()]
                         
class QuestNPC(NonPlayableCharacter):
    def __init__(self):
        self.name = "Emma"
        self.gold = 500
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion]