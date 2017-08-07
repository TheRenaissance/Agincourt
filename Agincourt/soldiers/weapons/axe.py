from .base_weap import Weapon

class Axe(Weapon):
    hit_lines = []

    def __init__(self):
        self.att_range=1
        self.weap_dmg=5
        self.durability=4
