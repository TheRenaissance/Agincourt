from .base_weap import Weapon

class Lance(Weapon):
    hit_lines: []

    def __init__(self):
        self.att_range=2
        self.weap_dmg=7
        self.durability=3

    def charge(self):
        # Perhaps there should be a way of ensuring the player
        # is mounted
        if player.current_move > 2:
            return player.attack + 12
