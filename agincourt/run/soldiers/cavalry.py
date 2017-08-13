from .base_sol import Soldier
from .weapons.lance import Lance
from .weapons.sword import Sword
from .weapons.crossbow import Crossbow
from random import randint

class Cavalryman(Soldier):
    weap_dict = {'lance': Lance(),
                 'sword': Sword(),
                 'crossbow': Crossbow()}

    def __init__(self):

        self.attack=randint(5, 10)
        self.speed=5
        self.weapons=['lance', 'sword', 'crossbow']
        self.defense=randint(1, 3)
        self.vitality=randint(25, 30)
        self.current_weapon='lance'

    def active_weapon(self, current_weapon):
        weap = self.weap_dict.get(current_weapon)
        return weap
