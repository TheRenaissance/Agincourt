from .weapons.lance import Lance

class Soldier(object):
    weap_dict: {'lance': Lance()}

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
