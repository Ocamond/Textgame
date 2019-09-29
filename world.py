import random
import enemies
import npc

class MapTile:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def modify_player(self, player):
        pass
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return """You find yourself in a dark forrest with a flickering torch on the ground.
        You can make out four paths, each equally as dark and foreboding."""

class BoringTile(MapTile):
    def intro_text(self):
        return """ There is nothing relevant in this area. You can rest and plan your next moves."""

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True
    def intro_text(self):
        return """ You see a bright light in the distance...
        it grows as you get closer! It's sunlight

        Vicotry is yours! for now....
        """

class EnemyTile(MapTile):
    def __init__ (self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text ="A gaint spider jumps down from its web in front of you!"
            self.dead_text = "The corpse of a dead spider rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Orge()
            self.alive_text = "An Ogre is blocking your path"
            self.dead_text = "A dead Ogre reminds you of your triumph"
        elif r < 0.95:
            self.enemy = enemies.Bear()
            self.alive_text = "You see a Bear he looks very strong and dangerouse"
            self.dead_text = "The bear is dead hope there is not another one lurking around"
        else:
            self.enemy = enemies.Wolf()
            self.alive_text = "You have disturbed a sleeping wolf he is very angry"
            self.dead_text = "He is finally dead a though fight it was...."
        
        super().__init__(x,y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

class TraderTile(MapTile):
    def __init__ (self,x,y):
        self.trader = npc.Trader
        super().__init__(x,y)
    
    def intro_text(self):
        return """
        A frail not-quite-home, not-quite-creature squats at a tree
        clinking his gold coins together. He looks willing to trade.
        """
    
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}.{} - {} Gold".format(i, item.name, item.value))
        
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["Q", "Q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)

                except ValueError:
                    input("Invalid choice!")
    
    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.invenotry.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print ("Trade complete")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell or (Q)uit")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("Here is what is available to buy: ")
                self.trade(player, self.trader)
            elif user_input in ["S", "s"]:
                print("Here is what is available to sell: ")
                self.trade(self.trader, player)
            else:
                print("invalid choice!")

class FindGoldTile(MapTile):
    def __init__ (self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print ("+{} gold added.".format(self.gold))
    
    def intro_text(self):
        if self.gold_claimed:
            return """ Another unremarkable part of the forest. You must forge onwards. 
            """
        else:
            return "Soneone dropped some gold. You pick it up."

world_dsl = """
|FG|EN|EN|TT|EN|VT|
|EN|  |  |EN|FG|  |
|EN|  |  |EN|  |EN|
|EN|  |FG|EN|EN|FG|
|TT|EN|FG|EN|FG|EN|
|EN|  |  |EN|  |TT|
|ST|EN|FG|EN|EN|EN|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
        
    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}
world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
 
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
 
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None