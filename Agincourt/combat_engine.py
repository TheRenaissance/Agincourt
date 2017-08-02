from soldiers.weapons.lance import Lance

class CombatEngine(object):

    def combat(self, player, opponent, plyr_wpn, opp_wpn):
        while player.vitality > 0 and opponent.vitality > 0:
            print("Do you wish to strike your foe?")
            print("\t1. Yes")
            print("\t2. No")

            choice = input('>>> ')

            plyr_dmg = player.attack + plyr_wpn.weap_dmg
            opp_dmg = opponent.attack + opp_wpn.weap_dmg

            if choice == '1':
                opponent.vitality -= plyr_dmg - opponent.defense
                print(f"You whallop the opponent to {opponent.vitality}")
            elif choice == '7':
                opponent.vitality -= 5000
                print("Giant combusting cows rain down on your foe.")
                print("BOOM BOOM BOOM BOOM BOOM BOOM BOOM")
                print(f"His vitality is now {opponent.vitality}")
            else:
                pass

            # The opponent counterattacks
            if opponent.vitality > 0:
                print("The opponent attacks!")
                player.vitality -= opp_dmg - player.defense
                print("The opponent smacks you about!", end=' ')
                print(f"Your vitality is {player.vitality}")
        if opponent.vitality <= 0:
            print("The opponent falls in a heap. You win!")
        else:
            print("You fall in a heap. You lose!")
