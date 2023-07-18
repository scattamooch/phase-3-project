from models import session, Race, Character, CharClass   


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



user_input = 'not x'

while user_input != 'x':
    user_input = input( '<3 ' )
    if user_input == 'a':

        for charclass in session.query( CharClass ).all():
            print( f'    {charclass.name}' )

    elif user_input == "add class":
        charclass_name = input("Enter the name of a race you'd like to add: ")
        new_class = CharClass(name = charclass_name)
        session.add(new_class)
        session.commit()
        print( f"{new_class.name} has been added.")
    
    elif user_input != 'x':
        print( f'{user_input} is not a valid option' )

print( 'byebye!')