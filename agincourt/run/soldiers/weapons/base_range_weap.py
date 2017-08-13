class RangedWeapon(object):
    def __init__(self, att_range, weap_dmg, durability, quiver):
        self.att_range=att_range
        self.weap_dmg=weap_dmg
        self.durability=durability
        self.quiver=quiver

        if quiver <=0:
            # I need a way for the attack to fail, maybe this should be in the
            # combat engine.
            pass
