#import shit
from models import *
from sqlalchemy.orm import joinedload
import pdb

#define shit
def print_ascii_welcome():
    welcome_logo = """
                              __        __   _                            
                              \ \      / /__| | ___ ___  _ __ ___   ___                       ()
        ()                     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ <::::::::::::::::::::}]xxxx()0
 o()xxxx[{::::::::::::::::::::> \ V  V /  __/ | (_| (_) | | | | | |  __/                      
        ()                       \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 
"""

    print(welcome_logo)

def print_intro():
    intro_message = """
...to the DnD Character Creator!

In this character creator, you'll be able to build your own unique Dungeons & Dragons character. You'll have the opportunity to choose your race, class, abilities, and more. Get ready to embark on an epic adventure!

Let your imagination soar as you bring your character to life and shape their destiny. Are you ready to create a legendary hero or a cunning rogue? The choice is yours!

Get ready to delve into a world of magic, monsters, and thrilling quests. Gather your wits, grab your dice, and let the adventure begin!

"""
    print(intro_message)

#Call shit
print_ascii_welcome()
print_intro()

user_input = input("Enter N to make a new character, S to view saved characters, or X at any time to exit: ")

while user_input.lower() != "x":
    if user_input.lower() == "n":
        # Name
        print("\n Enter the name of your new adventurer: ")
        character_name = input("\n ") 
        while len(character_name) > 15:
            print('\n Error: Name too long!')
            character_name = input("\n Waiting for name: ")
        while len(character_name) < 2:
            print('\n Error: Name too short!')
            character_name = input("\n Waiting for name: ")
        print(f"\n Your character name is: {character_name} \n \n \n")

        # Race selection
        print("\n~Enter the ID of your desired race. For more information add 100 to your desired race.")
        print("~~Available races:")
        for race in session.query(Race).all():
            print(f"ID: {race.id}, Name: {race.name}")
        print(" ")
        race_id = int(input("Waiting on race selection... "))
        while not 1 <= race_id <= 12 and not 100 <= race_id <= 112:
            print("Error: Not a valid selection. Try again!")
            race_id = int(input("Waiting on race selection... "))
        while 100 <= race_id <= 112: 
            info_race = session.query(Race).filter_by(id=race_id - 100).first()
            print(f"\n    Race: {info_race.name} | Age: {info_race.age}, Size: {info_race.size}, Languages: {info_race.language} \n")
            race_id = int(input("Waiting on race selection... "))
        else:
            selected_race = session.query(Race).filter_by(id=race_id).first()
        print(f"\n You have selected {selected_race.name} as your race! \n \n \n")


        # Class selection
        print("\n~Enter the ID of your desired class. For more information add 100 to your desired class.")
        print("~~Available classes:")
        for char_class in session.query(CharClass).all():
            print(f"ID: {char_class.id}, Name: {char_class.name}")
        print(" ")
        char_class_id = int(input("Waiting on class selection... "))
        while not 1 <= int(char_class_id) <= 12 and not 100 <= int(char_class_id) <= 112 and (type(char_class_id) is int):
            print("Error: Not a valid selection. Try again!")
            char_class_id = int(input("Waiting on class selection..."))
        while 100 <= int(char_class_id) <= 112: 
            info_char_class = session.query(CharClass).filter_by(id=char_class_id - 100).first()
            print(f"\n    Class: {info_char_class.name} | Armor: {info_char_class.armor}, Weapons: {info_char_class.weapons}, Starting Gear: {info_char_class.starting_gear} \n")
            char_class_id = int(input("Waiting on class selection..."))
        else:
            selected_char_class = session.query(CharClass).filter_by(id=char_class_id).first()
        print(f"\n You have selected {selected_char_class.name} as your class! \n \n \n")

        # Skill Rolls
        print(" ")
        skill = tuple(selected_race.skill)
        diceroll = [15,14,13,12,10,8]
        print(f"Your Current Skills:\n(S) Strength: {skill[1]}, (D) Dexterity: {skill[2]}, (C) Constitution: {skill[3]}, (W) Wisdom: {skill[4]}, (I) Intelligence: {skill[5]}, (R) Charisma: {skill[6]}")
        print(" ")
        print(f"Your Dice Roll Results:\n1: {diceroll[0]}, 2: {diceroll[1]}, 3: {diceroll[2]}, 4: {diceroll[3]}, 5: {diceroll[4]}, 6: {diceroll[5]}")
        print(" ")
        set_skill = input("(Example: 'S1' to assign 1st Dice Roll value to Strength)\nAssign your dice roll results to your skills: ")
        chosen_skill = [int(skill[1]), int(skill[2]), int(skill[3]), int(skill[4]), int(skill[5]), int(skill[6])]
        skill_cat =['S', 'D', 'C', 'W', 'I', 'R']

        # Set skills
        iteration_count = 0
        while iteration_count < 6:
            if len(set_skill) == 2:
                skill_index = set_skill[0].upper()
                roll_index = int(set_skill[1]) - 1

                if skill_index in skill_cat and 0 <= roll_index < len(chosen_skill):
                    chosen_skill[skill_cat.index(skill_index)] = chosen_skill[skill_cat.index(skill_index)] + (diceroll[roll_index])
                    diceroll.pop(roll_index)
                    print(" ")
                    print(f"Your Current Skills:\n(S) Strength: {chosen_skill[0]}, (D) Dexterity: {chosen_skill[1]}, (C) Constitution: {chosen_skill[2]}, (W) Wisdom: {chosen_skill[3]}, (I) Intelligence: {chosen_skill[4]}, (R) Charisma: {chosen_skill[5]}")
                    print(" ")
                    print(f"Your Dice Roll Results:\n" + ", ".join([f"{i + 1}: {diceroll[i]}" for i in range(len(diceroll))]))
                    print(" ")
                    set_skill = input("Assign your dice roll results to your skills: ")
                    iteration_count += 1
                else:
                    print("Error: Choose only between S,D,C,W,I,R and 1,2,3,4,5,6 for inputs, respectively")
            else:
                print("Error: Please enter a letter for your Skill and a number for the Dice Roll")
        print(f"Your Character's Skills:\nStrength: {chosen_skill[0]}, Dexterity: {chosen_skill[1]}, Constitution: {chosen_skill[2]}, Wisdom: {chosen_skill[3]}, Intelligence: {chosen_skill[4]}, Charisma: {chosen_skill[5]}")

        selected_char_skill = f'sk{str(chosen_skill[0]).zfill(2)}{str(chosen_skill[1]).zfill(2)}{str(chosen_skill[2]).zfill(2)}{str(chosen_skill[3]).zfill(2)}{str(chosen_skill[4]).zfill(2)}{str(chosen_skill[5]).zfill(2)}'

        pdb.set_trace()


        # Character creation
        new_character = Character(name=character_name, level=1, char_skill=selected_char_skill, race_id=selected_race.id, char_class_id=selected_char_class.id)
        session.add(new_character)
        session.commit()
        print(f"\n Your new character: {character_name}, the {selected_race.name} {selected_char_class.name}, has been created successfully!\n")

        #transition into stat rolls?

    elif user_input.lower() == "s":
        #match the characters class/race IDs to their string equivalents
        characters = session.query(Character).options(joinedload(Character.char_class), joinedload(Character.race)).all()

        #view saved characters
        print("ID | Name           | Level | Class          | Race")
        print("-------------------------------------------------------------------")
        for character in characters:
            print(f"{character.id:2} | {character.name:<14} | {character.level:^5} | {character.char_class.name:<14} | {character.race.name}")

        

    else:
        print(f"{user_input} is not a valid entry.")

    user_input = input("Enter N to make a new character, S to view saved characters, or X at any time to exit: ")

print("Happy campaigning!")
























# user_input = 'not x'

# while user_input != 'x':
#     user_input = input( '<3 ' )
#     if user_input == 'a':

#         for race in session.query( Race ).all():
#             print( f'    {race.name}' )

#     elif user_input == "add race":
#         race_name = input("Enter the name of a race you'd like to add: ")
#         new_race = Race(name = race_name)
#         session.add(new_race)
#         session.commit()
#         print( f"{new_race.name} has been added.")
    
#     elif user_input != 'x':
#         print( f'{user_input} is not a valid option' )

# print( 'byebye!')