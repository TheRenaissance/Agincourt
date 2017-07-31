class CombatEngine(object):

    def combat(self, player, opponent):
        while player.vitality > 0 and opponent.vitality > 0:
            print("Do you wish to strike your foe?")
            print("\t1. Yes")
            print("\t2. No")

            choice = input('>>> ')

            if choice == '1':
                opponent.vitality -= player.attack - opponent.defense
                print(f"You whallop the opponent to {opponent.vitality}")
            elif choice == '7':
                opponent.vitality -= 5000
                print("Giant combusting cows rain down on your foe.")
                print("BOOM BOOM BOOM BOOM BOOM BOOM BOOM")
                print(f"His vitality is now {opponent.vitality}")
            else:
                pass
        if opponent.vitality <= 0:
            print("The opponent falls in a heap. You win!")
        else:
            print("You fall in a heap. You lose!")
