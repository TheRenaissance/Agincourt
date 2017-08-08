class Weapon(object):
    hit_lines = []
    def __init__(self, att_range,
                       weap_dmg,
                       durability):

        self.att_range=att_range
        self.weap_dmg=weap_dmg
        self.durability=durability
