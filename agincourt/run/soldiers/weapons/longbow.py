from .base_range_weap import RangedWeapon

class Longbow(RangedWeapon):
    def __init__(self):
        self.att_range=250
        self.weap_dmg=15
        self.durability=5
        self.quiver=50
