#!/usr/bin/env python3

from random import randint

player_name = []

class PlayerName:
    def __init__(self, name, double_count, jail_count, in_jail):
        self.name = name
        self.double_count = double_count
        self.jail_count = jail_count
        self.in_jail = in_jail

def jail_dice_roll(player):
    print(player_name[player].name, "is in jail!")

    if player_name[player].jail_count < 2:
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)

        print("First dice is:  ", first_dice)
        print("Second dice is: ", second_dice)

        if first_dice == second_dice:
            print(player_name[player].name, "got out of jail!")
            return False

        else:
            player_name[player].jail_count += 1
            return True

    else:
        print("You must pay $50 to get out now.")
        return False

print("\n" * 100)
number_of_players = int(input("How many players?\n"))

for i in range(0, number_of_players):
    print("\nName for player", i + 1, "\b:")
    player_name.append(PlayerName(str(input()), 0, 0, False))

print("\n" * 100)

turn = 0

while True:
    while True:
        if turn >= number_of_players:
            turn = 0

        if player_name[turn].in_jail == True:

            print("\n" * 100)

            if jail_dice_roll(turn) == False:
                player_name[turn].in_jail = False

            turn += 1
            break

        first_dice = randint(1, 6)
        second_dice = randint(1, 6)

        print("\n" * 100)

        print("It's", player_name[turn].name, "\b's turn.")

        print("First dice is:", first_dice)
        print("Second dice is:", second_dice)

        if first_dice != second_dice:
            player_name[turn].double_count = 0
            turn += 1
            break

        player_name[turn].double_count += 1

        if player_name[turn].double_count < 3:
            print("You rolled doubles! Play again!")

            if player_name[turn].double_count == 2:
                print("If you roll doubles again, you'll go to jail!")

        if player_name[turn].double_count >= 3:
            player_name[turn].in_jail = True
            player_name[turn].double_count = 0
            print("Go to jail!")
            turn += 1
            break

        input("Press ENTER or RETURN to continue.\n")

    print("To play again, just press ENTER or RETURN")
    if input("Press any key before ENTER or RETURN to quit\n") != "":
        quit()
