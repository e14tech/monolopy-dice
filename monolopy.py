#!/usr/bin/env python3

from random import randint

player_name = []
print("\n" * 100)
number_of_players = int(input("How many players?\n"))

for i in range(0, number_of_players):
    print("\nName for player", i + 1, "\b:")
    player_name.append(input())

print("\n" * 100)

while True:
    jail_count = 0

    while True:
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)
        print("\n" * 5)

        print("First dice is:", first_dice)
        print("Second dice is:", second_dice)

        if first_dice != second_dice:
            break

        jail_count += 1

        if jail_count == 3:
            print("Go to jail!")
            break

        elif jail_count < 3:
            print("You rolled doubles! Play again!")

            if jail_count == 2:
                print("If you roll doubles again, you'll go to jail!")

        input("Press ENTER or RETURN to continue.")

    print("To play again, just press ENTER or RETURN")
    if input("Press any key before ENTER or RETURN to quit") != "":
        quit()
