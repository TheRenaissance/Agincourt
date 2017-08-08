from .base_weap import Weapon

class Longbow(Weapon):
    def __init__(self):
        self.att_range=250
        self.weap_dmg=15
        self.durability=5
