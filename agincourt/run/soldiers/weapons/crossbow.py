from .base_weap import Weapon

class Crossbow(Weapon):
    def __init__(self):
        self.att_range=100
        self.weap_dmg=20
        self.durability=2

# Some notes to self - maybe sep base class for long-range?
# durability should work dif, because weap not hitting foe
# need to implement system for firing, being empty, reloading
