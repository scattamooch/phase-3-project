from models import session, Race, Character, CharClass

#Call 'python table_setter.py' to reset the tables to their default settings
#(5 starting characters and no user created Races or Classes)

#Deletes Past Session Races/Classes
session.query( Race ).delete()
session.query( CharClass ).delete()

#All Starting Races
dragonborn = Race(name = "Dragonborn", age = 80, size = "Medium", language = "Common, Draconic", skill = 's200001')
human = Race(name = "Human", age = 100, size = "Medium", language = "Common", skill = 's111111')
dwarf = Race(name = "Dwarf", age = 350, size = "Medium", language = "Common, Dwarvish", skill = 's002000')
elf = Race(name = "Elf", age = 750, size = "Medium", language = "Common, Elvish", skill = 's020000')
gnome = Race(name = "Gnome", age = 500, size = "Small", language = "Common, Gnomish", skill = 's000020')
half_elf = Race(name = "Half-Elf", age = 180, size = "Medium", language = "Common, Elvish", skill = 's000002')
halfling = Race(name = "Halfling", age = 250, size = "Small", language = "Common, Halfling", skill = 's020000')
half_orc = Race(name = "Half-Orc", age = 75, size = "Medium", language = "Common, Orc", skill = 's201000')
tiefling = Race(name = "Tiefling", age = 100, size = "Medium", language = "Common, Infernal", skill = 's000012')

#All Starting Classes
barbarian = CharClass(name = "Barbarian", armor = "light armor, shields", weapons = "simple weapons, martial weapons", starting_gear = "greataxe")
bard = CharClass(name = "Bard", armor = "light armor", weapons = "simple weapons", starting_gear = "dagger")
cleric = CharClass(name = "Cleric", armor = "light armor, shields", weapons = "simple weapons", starting_gear = "mace")
druid = CharClass(name = "Druid", armor = "light armor, shields", weapons = "clubs, daggers, spears", starting_gear = "simple weapon, shield")
fighter = CharClass(name = "Fighter", armor = "all armor, shields", weapons = "simple weapons, martial weapons", starting_gear = "martial weapon, shield")
monk = CharClass(name = "Monk", armor = "none", weapons = "simple weapons", starting_gear = "short sword, 10 darts")
paladin = CharClass(name = "Paladin", armor= "all armor, shields", weapons = "simple weapons, martial weapons", starting_gear = "martial weapon, shield")
ranger = CharClass(name = "Ranger", armor = "light armor, shields", weapons = "simple weapons, martial weapons", starting_gear = "armor, two melee weapons")
rogue = CharClass(name = "Rogue", armor = "light armor", weapons = "simple weapons", starting_gear = "shortsword, thieves' tools")
sorcerer = CharClass(name = "Sorcerer", armor = "none", weapons = "daggers, light crossbows", starting_gear = "light crossbow, arcane focus")
warlock = CharClass(name = "Warlock", armor = "light armor", weapons = "simple weapons", starting_gear = "light crossbow, arcane focus")
wizard = CharClass(name = "Wizard", armor = "none", weapons = "daggers, light crossbows", starting_gear = "dagger, arcane focus")

#Render Starting Tables
session.bulk_save_objects([dragonborn, human, dwarf, elf, gnome, half_elf, halfling, half_orc, tiefling])
session.bulk_save_objects([barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard])

#Delete Past Session Characters
session.query(Character).filter(Character.id > 5).delete()

session.commit()

#CLI input for new Race
# user_input = 'not x'

# while user_input != 'x':
#     user_input = input( '<3 ' )
#     if user_input == 'r':

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


#CLI input for new Class
# user_input = 'not x'

# while user_input != 'x':
#     user_input = input( '<3 ' )
#     if user_input == 'c':

#         for charclass in session.query( CharClass ).all():
#             print( f'    {charclass.name}' )

#     elif user_input == "add class":
#         charclass_name = input("Enter the name of a race you'd like to add: ")
#         new_class = CharClass(name = charclass_name)
#         session.add(new_class)
#         session.commit()
#         print( f"{new_class.name} has been added.")
    
#     elif user_input != 'x':
#         print( f'{user_input} is not a valid option' )

# print( 'byebye!')