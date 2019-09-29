class Enemy:
    def __init__ (self):
        raise NotImplementedError ("Do not create raw Enemy objectiv")
 
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2

class Orge(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10
    
class Bear(Enemy):
    def __init__(self):
        self.name = "Bear"
        self.hp = 100
        self.damage = 4

class Wolf(Enemy):
    def __init__(self):
        self.name = "Wolf"
        self.hp = 80
        self.damage = 15