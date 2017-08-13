from .weapons import *

class Soldier(object):
    weap_dict = {
                'axe': Axe(),
                'bow': Bow(),
                'crossbow': Crossbow(),
                'dagger': Dagger(),
                'greatsword': Greatsword(),
                'lance': Lance(),
                'longbow': Longbow(),
                'morningstar': Morningstar(),
                'skillet': Skillet(),
                'sword': Sword()
                }

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
        self.current_weapon=weapons[0]

    def active_weapon(self, current_weapon):
        weap = self.weap_dict.get(current_weapon)
        return weap
