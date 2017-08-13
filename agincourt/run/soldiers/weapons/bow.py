from .base_range_weap import RangedWeapon

class Bow(Weapon):
    def __init__(self):
        self.att_range=100
        self.weap_dmg=4
        self.durability=2
        self.quiver=50
