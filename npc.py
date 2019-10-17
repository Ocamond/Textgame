import items

class NonPlayableCharacter():
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold

    def __str__(self):
        return self.name

Trader = NonPlayableCharacter("Trader", 100)
Trader.inventory = [items.CrustyBread,
                    items.CrustyBread,
                    items.CrustyBread,
                    items.Rustysword,
                    items.HealingPotion]

QuestNPC = NonPlayableCharacter("Emma", 500)
QuestNPC.inventory = [items.CrustyBread,
                      items.CrustyBread,
                      items.HealingPotion]

RewardNPC = NonPlayableCharacter("Sophia", 0)
RewardNPC.inventory = [items.GoldRing]
