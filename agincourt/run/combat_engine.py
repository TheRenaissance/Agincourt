# switch_weap can't change the plyr_wpn, except in that round

from .soldiers.weapons import *
from random import randint

class CombatEngine(object):

    def attack(self, player, opponent, plyr_wpn):
        plyr_dmg = player.attack + plyr_wpn.weap_dmg
        opponent.vitality -= plyr_dmg - opponent.defense
        print(f"You whallop the opponent to {opponent.vitality}")

    def get_attacked(self, player, opponent, opp_wpn):
        opp_dmg = opponent.attack + opp_wpn.weap_dmg
        player.vitality -= opp_dmg - player.defense
        print("The opponent smacks you about!", end=' ')
        print(f"Your vitality is {player.vitality}")

    def switch_weap(self, player, opponent, plyr_wpn):
        print("Do you look at what weapons you have about you?")
        print("\t1. Yes")
        print("\t2. No")

        look_choice = int(input('>>> '))

        if look_choice in (1,2):
            if look_choice == 1:
                print(player.weapons)
                # I want to make a 50% chance that when looking and drawing,
                # the soldier can't also attack, so I'm using a random number
                randnum = randint(1,2)
            else:
                pass

            print("Which weapon do you choose to draw?")

            wpn_choice = input('>>> ')

            # This try/except isn't working - it raises the AttributeError
            try:
                player.current_weapon = wpn_choice
                plyr_wpn = player.active_weapon(player.current_weapon)

            except AttributeError:
                print(f"You fumble, looking for a {wpn_choice}")
                print("where there is none.")

            if look_choice == 2 or (look_choice == 1 and randnum == 1):
                self.attack(player, opponent, plyr_wpn)


    def combat(self, player, opponent):

        plyr_wpn = player.active_weapon(player.current_weapon)

        print(f"Your weapon is a {player.current_weapon}")
        for attr, value in plyr_wpn.__dict__.items():
            print(attr + ': ' + str(value))

        opp_wpn = opponent.active_weapon(opponent.current_weapon)

        print(f"Your foe's weapon is a {opponent.current_weapon}")
        for attr, value in opp_wpn.__dict__.items():
            print(attr + ': ' + str(value))

        while player.vitality > 0 and opponent.vitality > 0:

            print(f"Your weapon is the {plyr_wpn}")
            print("What do you want to do?")
            print("\t1. Strike your foe")
            print("\t2. Switch to another weapon")
            print("\t3. Something else")

            choice = input('>>> ')

            # I think I should be making different functions out of these choices
            # like strike(), switch_weap(), a weapon and damage holder etc
            if choice == '1':
                self.attack(player, opponent, plyr_wpn)

            elif choice == '2':
                self.switch_weap(player, opponent, plyr_wpn)


            elif choice == '7':
                opponent.vitality -= 5000
                print("Giant combusting cows rain down on your foe.")
                print("BOOM BOOM BOOM BOOM BOOM BOOM BOOM")
                print(f"His vitality is now {opponent.vitality}")

            else:
                pass

            # The opponent counterattacks
            if opponent.vitality > 0:
                self.get_attacked(player, opponent, opp_wpn)

        if opponent.vitality <= 0:
            print("The opponent falls in a heap. You win!")
        else:
            print("You fall in a heap. You lose!")
