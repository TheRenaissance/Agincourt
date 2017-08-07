from .base_sol import Soldier
from random import randint, sample

class MAA(Soldier):
    weap_dict: {'greatsword': Greatsword(),
                'sword': Sword(),
                'axe': Axe(),
                'morningstar': Morningstar(),
                'crossbow': Crossbow(),
                'dagger': Dagger()}

    def __init__(self):
        # A list of weapons to generate from in the init
        maa_weapons = ['greatsword', 'sword', 'axe', 'morningstar', 'crossbow',
                        'dagger']

        self.attack=randint(3,7)
        self.speed=1
        # The weapons are a bit complicated, because I want variation
        weap_indx = sample(range(0, 5), 3)
        self.weapons=[maa_weapons[weap_indx[0]], maa_weapons[weap_indx[1]],
                      maa_weapons[weap_indx[2]]]
        self.defense=randint(6,9)
        self.vitality=randint(20,25)
        self.current_weapon=[self.weapons[0]]

    def active_weapon(self, current_weapon):
        weap = self.weap_dict.get(current_weapon)
        return weap
