#import shit
from models import *
from sqlalchemy.orm import joinedload

#define shit
def print_ascii_welcome():
    welcome_logo = """
                              __        __   _                            
                              \ \      / /__| | ___ ___  _ __ ___   ___  
                               \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ <::::::::::::::::::::}]xxxx()0
 o()xxxx[{::::::::::::::::::::> \ V  V /  __/ | (_| (_) | | | | | |  __/ 
                                 \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 
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
        print(" ")
        character_name = input("Enter the name of your new adventurer: ")

        # Race selection
        print(" ")
        print("Available races:")
        for race in session.query(Race).all():
            print(f"ID: {race.id}, Name: {race.name}")
        print(" ")
        race_id = int(input("Enter the ID of your desired race: "))
        selected_race = session.query(Race).filter_by(id=race_id).first()

        # Class selection
        print(" ")
        print("Available classes:")
        for char_class in session.query(CharClass).all():
            print(f"ID: {char_class.id}, Name: {char_class.name}")
        print(" ")
        class_id = int(input("Enter the ID of your desired class: "))
        selected_class = session.query(CharClass).filter_by(id=class_id).first()

        # Character creation
        new_character = Character(name=character_name, level=1, race_id=selected_race.id, char_class_id=selected_class.id)
        session.add(new_character)
        session.commit()
        print(" ")
        print(f"New character: {character_name}, the {selected_race.name} {selected_class.name}, created successfully!")

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