from random import randint
from sqlalchemy.orm import joinedload
from models import *
import time


def print_arena_logo():
	welcome_logo = """ 
  ______       _              _   _                                          
 |  ____|     | |            | | | |              /\                         
 | |__   _ __ | |_ ___ _ __  | |_| |__   ___     /  \   _ __ ___ _ __   __ _ 
 |  __| | '_ \| __/ _ \ '__| | __| '_ \ / _ \   / /\ \ | '__/ _ \ '_ \ / _` |
 | |____| | | | ||  __/ |    | |_| | | |  __/  / ____ \| | |  __/ | | | (_| |
 |______|_| |_|\__\___|_|     \__|_| |_|\___| /_/    \_\_|  \___|_| |_|\__,_|
                                                                                                                                                         
"""
	print(welcome_logo)

def combat_intro():
	intro = """
Choose your warrior and enter the arena! Your opponent will be chosen at random. 
    
Outmaneuver and outlast your enemies to achieve glory and fame! 
    
Keep in mind that strength will boost physical attacks, while intellect will boost magical spells and healing."""
	
	print(intro)

def start_battle():
    print_arena_logo()
    combat_intro()

    print(" ")
    user_input = input("Enter S to choose your character and start brawling, or enter X to exit: ")

    while user_input.lower() != "x":
        if user_input.lower() == "s":
        #match the characters class/race IDs to their string equivalents
            characters = session.query(Character).options(joinedload(Character.char_class), joinedload(Character.race)).all()
            row_count = session.query(Character).count()

        #view saved characters
            print(" ")
            print("ID | Name           | Level | Class          | Race")
            print("-------------------------------------------------------------------")
            for table_char in characters:
                print(f"{table_char.id:2} | {table_char.name:<14} | {table_char.level:^5} | {table_char.char_class.name:<14} | {table_char.race.name}")
                #print(f"Formatted string with stats")
                
            player_id = int(input("Enter an ID to select your character: "))
            
            while player_id > row_count:
                print("Error! No character with that ID.")
                player_id = int(input("Enter an ID to select your character: "))

        #character actually gets assigned to player
            selected_character = None
            for char in characters:
                    if char.id == player_id:
                        selected_character = char

            if selected_character is not None:
                    player_name = selected_character.name
                    player_race = selected_character.race.name
                    player_class = selected_character.char_class.name
            print(f"You have chosen {player_name}, the {player_race} {player_class}.")

        # CPU gets assigned a character, and character gets checked to make sure it's not the same as the players character
            assign_cpu = None
            while True:
                cpu_id = randint(1, row_count)
                if cpu_id != player_id:
                    for cpu_char in characters:
                        if cpu_char.id == cpu_id:
                                assign_cpu = cpu_char
                                break
                if assign_cpu is not None:
                    break

            if assign_cpu is not None:
                cpu_name = assign_cpu.name
                cpu_race = assign_cpu.race.name
                cpu_class = assign_cpu.char_class.name
            print(" ")
            print(f"Your opponent has been determined: {cpu_name}, the {cpu_race} {cpu_class}. Prepare to fight.")
        #where the combat starts            
            player_hp = 100
            cpu_hp = 100

            print(" ")
            print("Adventurers start with 100 hitpoints, brace yourself!")
            while player_hp > 0 and cpu_hp > 0:
            # Player turn
                print("================================================================================")
                print(f"<<< {player_name}: {player_hp} hitpoints       {cpu_name}: {cpu_hp} hitpoints >>>")
                phys1 = randint(90, 100) #plus strength
                spell1 = randint(0, 16) #plus intellect
                crit_phys1 = randint(11, 25) #plus str
                crit_spell1 = randint(11, 25) #plus int
                crit1 = randint(0, 15)
                p1move = input(f"{player_name}, P for a physical attack, C to cast a spell, H to heal: ")
                if p1move.lower() == "p" and crit1 == 5:
                    print(f"{player_name} CRITICALLY hit {cpu_name} for {crit_phys1} physical damage!")
                    cpu_hp -= crit_phys1
                    if cpu_hp > 0:
                        print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                        print(" ")
                    elif cpu_hp <= 0:
                         print(f"{cpu_name} has 0 hitpoints remaining...")
                elif p1move.lower() == "p" and crit1 != 5:
                    print(f"{player_name} hit {cpu_name} for {phys1} physical damage.")
                    cpu_hp -= phys1
                    if cpu_hp > 0:
                        print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                        print(" ")
                    elif cpu_hp <= 0:
                         print(f"{cpu_name} has 0 hitpoints remaining...")
                elif p1move.lower() == "c" and crit1 == 5:
                    print(f"{player_name} CRITICALLY hit {cpu_name} for {crit_spell1} spell damage!")
                    cpu_hp -= crit_spell1
                    if cpu_hp > 0:
                        print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                        print(" ")
                    elif cpu_hp <= 0:
                         print(f"{cpu_name} has 0 hitpoints remaining...")
                elif p1move.lower() == "c" and crit1 != 5:
                    print(f"{player_name} hit {cpu_name} for {spell1} spell damage!")
                    cpu_hp -= spell1
                    if cpu_hp > 0:
                        print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                        print(" ")
                    elif cpu_hp <= 0:
                         print(f"{cpu_name} has 0 hitpoints remaining...")
                elif p1move.lower() == "h" and crit1 == 5:
                    print(f"{player_name} CRITICALLY heals for {crit_spell1}.")
                    player_hp = min(player_hp + crit_spell1, 100)
                    print(f"{player_name} has {player_hp} hitpoints remaining...")
                    print(" ")
                elif p1move.lower() == "h" and crit1 != 5:
                    print(f"{player_name} heals for {spell1}.")
                    player_hp = min(player_hp + spell1, 100)
                    print(f"{player_name} has {player_hp} hitpoints remaining...")
                    print(" ")
                else:
                    print("Invalid move! You need to be faster, you've lost your turn.")
                    print(" ")

            #check if anyones dead
                if cpu_hp <= 0:
                    print(" ")
                    print("////////////////////////////////////////////////////////////////")
                    print(f"{cpu_name} has been defeated! {player_name} is victorious!")
                    print("////////////////////////////////////////////////////////////////")
                    break
                elif player_hp <= 0:
                    print(" ")
                    print("////////////////////////////////////////////////////////////////")
                    print(f"{player_name} has been defeated! {cpu_name} is victorious!")
                    print("////////////////////////////////////////////////////////////////")
                    break
                    
            # CPU Turn
                cpumovegen = randint(0, 9)
                cpu_phys = randint(3, 17)
                cpu_spell = randint(3, 17)
                cpu_phys_crit = randint(11, 25)
                cpu_spell_crit = randint(11, 25)
                cpu_crit = randint(0, 15)
                if cpu_hp >= 60  and cpumovegen >= 1:
                    cpumove = "attack"
                elif cpu_hp >= 60 and cpumovegen == 0:
                    cpumove = "heal"
                elif cpu_hp <= 59 and cpu_hp >= 30 and cpumovegen >= 5 and cpumovegen <= 9:
                    cpumove = "attack"
                elif cpu_hp <= 59 and cpu_hp >= 30 and cpumovegen < 5:
                    cpumove = "heal"
                elif cpu_hp <= 29 and cpu_hp > 0 and cpumovegen <= 2:
                    cpumove = "attack"
                elif cpu_hp <= 29 and cpu_hp > 0 and cpumovegen > 2: 
                    cpumove = "heal"
                
                time.sleep(1.5)
                print("================================================================================")
                print(f"{cpu_name} chooses to {cpumove}!")

                if cpumove == "attack" and cpu_crit == 5:
                    print(f"{cpu_name} CRITICALLY hit {player_name} for {cpu_phys_crit} damage!")
                    player_hp -= cpu_phys_crit
                    if player_hp > 0:
                        print(f"{player_name} has {player_hp} hitpoints remaining...")
                        print(" ")
                    elif player_hp <= 0:
                         print(f"{player_name} has 0 hitpoints remaining...")
                elif cpumove == "attack" and cpu_crit != 5:
                    print(f"{cpu_name} hit {player_name} for {cpu_phys} damage!")
                    player_hp -= cpu_phys
                    if player_hp > 0:
                        print(f"{player_name} has {player_hp} hitpoints remaining...")
                        print(" ")
                    elif player_hp <= 0:
                         print(f"{player_name} has 0 hitpoints remaining...")
                elif cpumove == "heal" and cpu_crit == 5:
                    print(f"{cpu_name} CRITICALLY heals for {cpu_spell_crit}.")
                    cpu_hp = min(cpu_hp + cpu_spell_crit, 100)
                    print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                    print(" ")
                elif cpumove == "heal" and cpu_crit != 5:
                    print(f"{cpu_name} heals for {cpu_spell}.")
                    cpu_hp = min(cpu_hp + cpu_spell, 100)
                    print(f"{cpu_name} has {cpu_hp} hitpoints remaining...")
                    print(" ")
            #check if anyones dead
                if player_hp <= 0:
                    print(" ")
                    print("////////////////////////////////////////////////////////////////")
                    print(f"{player_name} has been defeated! {cpu_name} is victorious!")
                    print("////////////////////////////////////////////////////////////////")
                    break
                elif cpu_hp <= 0:
                    print(" ")
                    print("////////////////////////////////////////////////////////////////")
                    print(f"{cpu_name} has been defeated! {player_name} is victorious!")
                    print("////////////////////////////////////////////////////////////////")
                    break
    # user can restart or exit
        if player_hp <= 0 or cpu_hp <= 0:
                print("The battle is over!")
                restart_input = input("Enter R to restart or X to exit: ")
                if restart_input.lower() == "r":
                    # Restart the game by going back to the combat intro
                    continue
                elif restart_input.lower() == "x":
                    print("Thanks for playing! See you next time.")
                    break
                else:
                    print("Invalid input. The game will exit.")
                    break
        elif user_input.lower() == "x" or user_input.lower() != "s":
            print("Whoops! That wasn't a valid entry!")
            user_input = input("Enter 1 to choose your character and start brawling, or enter X to exit: ")
            
            
    print("That's okay, the arena's not for everyone...")

start_battle()