from base_sol import Soldier
from random import randint

class Cavalryman(Soldier):
    def __init__(self):

        self.attack=randint(5, 10)
        self.speed=5
        self.weapons=['lance', 'sword', 'crossbow']
        self.defense=randint(1, 3)
        self.vitality=randint(25, 30)
        self.current_weapon=None

    
