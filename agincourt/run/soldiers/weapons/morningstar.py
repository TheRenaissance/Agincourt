from .base_weap import Weapon

class Morningstar(Weapon):
    hit_lines = []

    def __init__(self):
        self.att_range=1
        self.weap_dmg=4
        self.durability=5
