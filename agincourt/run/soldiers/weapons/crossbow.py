from .base__range_weap import RangedWeapon

class Crossbow(Weapon):
    def __init__(self):
        self.att_range=100
        self.weap_dmg=20
        self.durability=2
        self.quiver=2

# durability should work dif, because weap not hitting foe
# need to implement system for firing, being empty, reloading
