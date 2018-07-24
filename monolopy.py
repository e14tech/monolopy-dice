#!/usr/bin/env python3

from random import randint

player_name = []
print("\n" * 100)
number_of_players = int(input("How many players?\n"))

for i in range(0, number_of_players):
    print("\nName for player", i + 1, "\b:")
    player_name.append(input())

print("\n" * 100)

turn = 0

while True:
    jail_count = 0

    while True:
        if turn >= number_of_players:
            turn = 0

        first_dice = randint(1, 6)
        second_dice = randint(1, 6)

        print("\n" * 100)

        print("It's", player_name[turn], "\b's turn.")

        print("First dice is:", first_dice)
        print("Second dice is:", second_dice)

        if first_dice != second_dice:
            turn += 1
            break

        jail_count += 1

        if jail_count < 3:
            print("You rolled doubles! Play again!")

        if jail_count == 3:
            print("Go to jail!")
            break

            if jail_count == 2:
                print("If you roll doubles again, you'll go to jail!")

        input("Press ENTER or RETURN to continue.\n")

    print("To play again, just press ENTER or RETURN")
    if input("Press any key before ENTER or RETURN to quit\n") != "":
        quit()
