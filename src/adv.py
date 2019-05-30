import time
import random
import os

from room import room
from player import player
from messages import hello, goodbye, where_to_go, offer_items


def walking_function(n):
    for n in range(0, 2):
        print("walking...")
        time.sleep(0.8)
    print("almost there...")
    time.sleep(1)


def drop_item(p):
    print("You are already carrying 3 things. You can't take anything at this moment, but you can drop something")
    dropped_item = input(
        f"Would you like to drop any of these items - {p.items[0].upper()} {p.items[1].upper()} {p.items[2].upper()} - (input no for no): ")

    if(dropped_item.lower() == p.items[0]):
        p.dropItem(p.items[0])
        return
    elif(dropped_item.lower() == p.items[1]):
        p.dropItem(p.items[1])
        return
    elif(dropped_item.lower() == p.items[2]):
        p.dropItem(p.items[2])
        return
    elif(dropped_item.lower() == "no"):
        return
    else:
        print("Not sure what is that")
        drop_item(p)


def take_item(f, s, p):
    if(len(p.items) < 3):
        chosen_item = input(
            "Would you like to take something? What is it going to be: ")
        if(chosen_item.lower() == f):
            p.getItem(f)
        elif(chosen_item.lower() == s):
            p.getItem(s)
        elif(chosen_item.lower() == "no"):
            return
        else:
            print("Not sure what is that, can you add it one more time")
            take_item(f, s, p)
    else:
        drop_item(p)


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
                offer_items(
                    player.current_room.items[0], player.current_room.items[1])
                take_item(
                    player.current_room.items[0], player.current_room.items[1], player)
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
                offer_items(
                    player.current_room.items[0], player.current_room.items[1])
                take_item(
                    player.current_room.items[0], player.current_room.items[1], player)
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
                offer_items(
                    player.current_room.items[0], player.current_room.items[1])
                take_item(
                    player.current_room.items[0], player.current_room.items[1], player)
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
                offer_items(
                    player.current_room.items[0], player.current_room.items[1])
                take_item(
                    player.current_room.items[0], player.current_room.items[1], player)
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
