from textwrap import dedent
from run.combat_engine import CombatEngine
from run.soldiers.base_sol import Soldier
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

            opponent = Cavalryman()

            print("Your opponent is a Soldier! Good job!")
            for attr, value in opponent.__dict__.items():
                if isinstance(value, list):
                    print(attr + ':')
                    for n in value:
                        print(f'\t{n}')
                else:
                    print(attr + ': ' + str(value))
            
            combatter = CombatEngine()
            combatter.combat(player, opponent)

        else:
            print("Huh?")
            Setup()

play = Setup()
play.run()
