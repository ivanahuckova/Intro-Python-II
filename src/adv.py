import time
import random
import os

from room import room
from player import player
from messages import hello, goodbye, where_to_go


def walking_function(n):

    for n in range(0, n):
        print("walking...")
        time.sleep(0.8)
    print("almost there...")
    time.sleep(1)


# Game logic
directions = ''
os.system('clear')
print(f"{hello}")
print(
    f"{player.name}, you are currently in {player.current_room.name.upper()} {player.current_room.emoji}")

while directions != 'q':
    directions = input(f"{where_to_go}")
    try:
        if directions == "n":
            os.system('clear')
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                walking_function(random.randint(1, 5))

                print(
                    f"\nYou have decided to go north and you arrived to {player.current_room.name.upper()} {player.current_room.emoji}\n")
                print(f"{player.current_room.describtion}")

            else:
                print(
                    f"⬆️  There is nothing north of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "s":
            os.system('clear')
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                walking_function(random.randint(1, 5))
                print(
                    f"\nYou have decided to go south and you arrived to {player.current_room.name.upper()} {player.current_room.emoji}\n")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"⬇️  There is nothing south of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "e":
            os.system('clear')
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                walking_function(random.randint(1, 5))
                print(
                    f"You have decided to go east and you arrived to {player.current_room.name.upper()} {player.current_room.emoji}\n")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"➡️  There is nothing east of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "w":
            os.system('clear')
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                walking_function(random.randint(1, 5))
                print(
                    f"You have decided to go east and you arrived to {player.current_room.name.upper()} {player.current_room.emoji}\n")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"⬅️  There is nothing west of {player.current_room.name.upper()}")
        elif directions == "q":
            goodbye(player.current_room)
            break
        else:
            print("Please select a valid direction")
    except ValueError:
        print("Please enter the valid direction")
