from textwrap import dedent
from run.combat_engine import CombatEngine
from run.soldiers.cavalry import Cavalryman
from run.soldiers.maa import MAA

class Setup(object):

    def run(self):
        print(dedent("""
        Choose your soldier:
            1. Cavalryman (Easy)
            2. Man-at-Arms (Moderate)
        """))

        choice = int(input('>>> '))
        if choice in range(1, 3):
            if choice == 1:
                player = Cavalryman()
                print("You have chosen the Cavalryman! Good job!")
            elif choice == 2:
                player = MAA()
                print("You have chosen the Man-at-Arms! Good job!")

            for attr, value in player.__dict__.items():
                if isinstance(value, list):
                    print(attr + ':')
                    for n in value:
                        print(f'\t{n}')
                else:
                    print(attr + ': ' + str(value))
            plyr_wpn = player.active_weapon(player.current_weapon)
            print(f"Your active weapon is a {player.current_weapon}")
            for attr, value in plyr_wpn.__dict__.items():
                print(attr + ': ' + str(value))

            opponent = Cavalryman()
            print("Your opponent is a Cavalryman! Good job!")
            for attr, value in opponent.__dict__.items():
                if isinstance(value, list):
                    print(attr + ':')
                    for n in value:
                        print(f'\t{n}')
                else:
                    print(attr + ': ' + str(value))
            opp_wpn = opponent.active_weapon(opponent.current_weapon)
            print(f"Your opponent's weapon is a {opponent.current_weapon}")
            for attr, value in opp_wpn.__dict__.items():
                print(attr + ': ' + str(value))

            combatter = CombatEngine()
            combatter.combat(player, opponent, plyr_wpn, opp_wpn)

        else:
            print("Huh?")
            Setup()

play = Setup()
play.run()
