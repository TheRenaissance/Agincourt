class Soldier(object):
    weaps = {}

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

    def get_current_weapon(self, current_weapon)
        weap = Soldier.weaps.get(current_weapon)
        return weap
