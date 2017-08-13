from random import randinti
from .weapons.longbow import Longbow
from .weapons.dagger import dagger

class Archer(Soldier):
    weap_dict = {'longbow': Longbow(),
                 'dagger': Dagger()}

    def __init__(self):
        self.attack=randint(2,5)
        self.speed=2
        self.weapons=['longbow', 'dagger']
        self.defense=randint(2,5)
        self.vitality=randint(15,20)
        self.current_weapon='longbow'

    def active_weapon(self, current_weapon):
        weap = self.weap_dict.get(current_weapon)
        return weap
