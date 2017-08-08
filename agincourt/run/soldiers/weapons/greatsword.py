from .base_weap import Weapon

class Greatsword(Weapon):
    hit_lines = []

    # I'm debating putting in something lowering the defense while using
    def __init__(self):
        self.att_range=2
        self.weap_dmg=7
        self.durability=7
