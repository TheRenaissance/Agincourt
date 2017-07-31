from textwrap import dedent
from combat_engine import CombatEngine

class Setup(object):

    def run(self):
        print(dedent("""
        Choose your soldier:
            1. Cavalryman (Easy)
        """))

        choice = input('>>> ')
        if choice == '1':
            player = Cavalryman()
            print("You have chose the Cavalryman! Good job!")
            for attr, value in player.__dict__.items():
                if isinstance(value, list):
                    print(attr + ':')
                    for n in value:
                        print(f'\t{n}')
                else:
                    print(attr + ': ' + str(value))
            opponent = Cavalryman()
            print("Your opponent is a Cavalryman! Good job!")
            for attr, value in opponent.__dict__.items():
                if isinstance(value.list):
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
