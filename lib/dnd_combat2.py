import random
import time
from sqlalchemy.orm import joinedload
from models import session, Character


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


def get_valid_player_choice(row_count):
    while True:
        try:
            print(" ")
            player_id = int(input("Enter an ID to select your character: "))
            if player_id > row_count:
                print("Error! No character with that ID.")
            else:
                return player_id
        except ValueError:
            print("Error! Entry must be a valid integer.")


def print_character_info(char):
    print(f"{char.id:2} | {char.name:<14} | {char.level:^5} | {char.char_class.name:<14} | {char.race.name}")


def choose_character():
    characters = session.query(Character).options(joinedload(Character.char_class), joinedload(Character.race)).all()
    row_count = session.query(Character).count()

    print("ID | Name           | Level | Class          | Race")
    print("-------------------------------------------------------------------")
    for table_char in characters:
        print_character_info(table_char)

    player_id = get_valid_player_choice(row_count)
    selected_character = next((char for char in characters if char.id == player_id), None)

    if selected_character is not None:
        player_name = selected_character.name
        player_race = selected_character.race.name
        player_class = selected_character.char_class.name
        print(f"You have chosen {player_name}, the {player_race} {player_class}.")
        return selected_character
    else:
        return None


def choose_opponent(characters, player_id):
    while True:
        cpu_id = random.randint(1, len(characters))
        if cpu_id != player_id:
            return next((char for char in characters if char.id == cpu_id), None)


def get_move_input(player_name):
    return input(f"{player_name}, P for a physical attack, C to cast a spell, H to heal: ").lower()


def handle_player_move(player_name, cpu_name, player_hp, cpu_hp):
    phys1 = random.randint(90, 100)  # plus strength
    spell1 = random.randint(0, 16)  # plus intellect
    crit_phys1 = random.randint(11, 25)  # plus str
    crit_spell1 = random.randint(11, 25)  # plus int
    crit1 = random.randint(0, 15)
    p1move = get_move_input(player_name)

    if p1move == "p" and crit1 == 5:
        print(f"{player_name} CRITICALLY hit {cpu_name} for {crit_phys1} physical damage!")
        cpu_hp -= crit_phys1
    elif p1move == "p" and crit1 != 5:
        print(f"{player_name} hit {cpu_name} for {phys1} physical damage.")
        cpu_hp -= phys1
    elif p1move == "c" and crit1 == 5:
        print(f"{player_name} CRITICALLY hit {cpu_name} for {crit_spell1} spell damage!")
        cpu_hp -= crit_spell1
    elif p1move == "c" and crit1 != 5:
        print(f"{player_name} hit {cpu_name} for {spell1} spell damage!")
        cpu_hp -= spell1
    elif p1move == "h" and crit1 == 5:
        print(f"{player_name} CRITICALLY heals for {crit_spell1}.")
        player_hp = min(player_hp + crit_spell1, 100)
    elif p1move == "h" and crit1 != 5:
        print(f"{player_name} heals for {spell1}.")
        player_hp = min(player_hp + spell1, 100)
    else:
        print("Invalid move! You need to be faster, you've lost your turn.")
    return player_hp, cpu_hp


def handle_cpu_move(cpu_name, player_name, cpu_hp, player_hp):
    cpumovegen = random.randint(0, 9)
    cpu_phys = random.randint(3, 17)
    cpu_spell = random.randint(3, 17)
    cpu_phys_crit = random.randint(11, 25)
    cpu_spell_crit = random.randint(11, 25)
    cpu_crit = random.randint(0, 15)

    if cpu_hp >= 60 and cpumovegen >= 1:
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
    elif cpumove == "attack" and cpu_crit != 5:
        print(f"{cpu_name} hit {player_name} for {cpu_phys} damage!")
        player_hp -= cpu_phys
    elif cpumove == "heal" and cpu_crit == 5:
        print(f"{cpu_name} CRITICALLY heals for {cpu_spell_crit}.")
        cpu_hp = min(cpu_hp + cpu_spell_crit, 100)
    elif cpumove == "heal" and cpu_crit != 5:
        print(f"{cpu_name} heals for {cpu_spell}.")
        cpu_hp = min(cpu_hp + cpu_spell, 100)

    return player_hp, cpu_hp


def check_game_status(player_name, cpu_name, player_hp, cpu_hp):
    if cpu_hp <= 0:
        print(" ")
        print("////////////////////////////////////////////////////////////////")
        print(f"{cpu_name} has been defeated! {player_name} is victorious!")
        print("////////////////////////////////////////////////////////////////")
        return False
    elif player_hp <= 0:
        print(" ")
        print("////////////////////////////////////////////////////////////////")
        print(f"{player_name} has been defeated! {cpu_name} is victorious!")
        print("////////////////////////////////////////////////////////////////")
        return False
    return True


def start_battle():
    print_arena_logo()
    combat_intro()

    print(" ")
    user_input = input("Enter S to choose your character and start brawling, or enter X to exit: ")

    while user_input.lower() != "x":
        if user_input.lower() == "s":
            player_character = choose_character()

            if player_character is not None:
                characters = session.query(Character).options(joinedload(Character.char_class), joinedload(Character.race)).all()
                player_name = player_character.name
                player_hp = 100
                player_id = player_character.id

                opponent_character = choose_opponent(characters, player_id)

                if opponent_character is not None:
                    cpu_name = opponent_character.name
                    cpu_hp = 100

                    print(" ")
                    print("Adventurers start with 100 hit points, brace yourself!")

                    while player_hp > 0 and cpu_hp > 0:
                        print("================================================================================")
                        print(f"<<< {player_name}: {player_hp} hit points       {cpu_name}: {cpu_hp} hit points >>>")

                        player_hp, cpu_hp = handle_player_move(player_name, cpu_name, player_hp, cpu_hp)

                        if not check_game_status(player_name, cpu_name, player_hp, cpu_hp):
                            break

                        player_hp, cpu_hp = handle_cpu_move(cpu_name, player_name, cpu_hp, player_hp)

                        if not check_game_status(player_name, cpu_name, player_hp, cpu_hp):
                            break

                    restart_input = input("Enter R to restart or X to exit: ")
                    if restart_input.lower() == "r":
                        continue
                    elif restart_input.lower() == "x":
                        print("Thanks for playing! See you next time.")
                        break
                    else:
                        print("Invalid input. The game will exit.")
                        break

        elif user_input.lower() != "s":
            print("Whoops! That wasn't a valid entry!")
            user_input = input("Enter S to choose your character and start brawling, or enter X to exit: ")

    print("That's okay, the arena's not for everyone...")


if __name__ == "__main__":
    start_battle()
