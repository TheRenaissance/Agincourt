from .base_weap import Weapon

class Dagger(Weapon):
    hit_lines = []

    def __init__(self):
        self.att_range=0
        self.weap_dmg=2
        self.durability=4
