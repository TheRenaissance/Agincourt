from .weapons import *

class Soldier(object):
    weap_dict: {'lance': Lance(),
                'greatsword': Greatsword(),
                'sword': Sword(),
                'axe': Axe(),
                'morningstar': Morningstar(),
                'crossbow': Crossbow(),
                'dagger': Dagger()}

    def __init__(self, attack,
                       speed,
                       weapons,
                       defense,
                       vitality):

        self.attack=attack
        self.speed=speed
        self.weapons=weapons
        self.defense=defense
        self.vitality=vitality
        self.current_weapon=current_weapon

    def active_weapon(self):
        weap = Soldier.weap_dict.get(self.current_weapon)
        return weap
