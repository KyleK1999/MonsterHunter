import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import (
    get_all_character_names, save_action_round, get_character_stats,
    get_random_monster, get_random_item, add_item_to_inventory,
    get_monster_by_id, execute_action, clear_inventory, reset_all_monsters_health,
    get_monster_by_name,
)

monster_order = ["Undead Skeleton", "Gigantic Troll", "Alduin the Dragon"]
current_monster_id = 0 # This will keep track of the monster we are currently fighting

def get_next_monster_in_sequence():
    if monster_order:
        monster_name = monster_order.pop(0)
        monster = get_monster_by_name(monster_name)
        if monster:
            return monster
    else:
        print("You've defeated all the monsters!")
        print(congratulatory_image)  
        return None
    
startup_image = '''
                                                           .:'                                  `:.                                    
                                                          ::'                                    `::                                   
                                                         :: :.                                  .: ::                                  
                                                          `:. `:.             .             .:'  .:'                                   
                                                           `::. `::           !           ::' .::'                                     
                                                               `::.`::.    .' ! `.    .::'.::'                                         
                                                                 `:.  `::::'':!:``::::'   ::'                                          
                                                                 :'*:::.  .:' ! `:.  .:::*`:                                           
                                                                :: HHH::.   ` ! '   .::HHH ::                                          
                                                               ::: `H TH::.  `!'  .::HT H' :::                                         
                                                               ::..  `THHH:`:   :':HHHT'  ..::                                         
                                                               `::      `T: `. .' :T'      ::'                                         
                                                                 `:. .   :         :   . .:'                                           
                                                                   `::'               `::'                                             
                                                                     :'  .`.  .  .'.  `:                                               
                                                                     :' ::.       .:: `:                                               
                                                                     :' `:::     :::' `:                                               
                                                                      `.  ``     ''  .'                                                
                                                                       :`...........':                                                 
                                                                       ` :`.     .': '                                                 
                                                                        `:  `"""'  :'
                                                                                                                                
                                                                 ╔═╦═╗────╔═╦╗─────╔╗╔╗────╔╗
                                                                 ║║║║╠═╦═╦╣═╣╚╦═╦╦╗║╚╝╠╦╦═╦╣╚╦═╦╦╗
                                                                 ║║║║║╬║║║╠═║╔╣╩╣╔╝║╔╗║║║║║║╔╣╩╣╔╝
                                                                 ╚╩═╩╩═╩╩═╩═╩═╩═╩╝─╚╝╚╩═╩╩═╩═╩═╩╝
'''

congratulatory_image = ''' 
                                                      __      __                         __       __  __           
                                                    /  \    /  |                       /  |  _  /  |/  |          
                                                    $$  \  /$$/______   __    __       $$ | / \ $$ |$$/  _______  
                                                     $$  \/$$//      \ /  |  /  |      $$ |/$  \$$ |/  |/       \ 
                                                      $$  $$//$$$$$$  |$$ |  $$ |      $$ /$$$  $$ |$$ |$$$$$$$  |
                                                       $$$$/ $$ |  $$ |$$ |  $$ |      $$ $$/$$ $$ |$$ |$$ |  $$ |
                                                        $$ | $$ \__$$ |$$ \__$$ |      $$$$/  $$$$ |$$ |$$ |  $$ |
                                                        $$ | $$    $$/ $$    $$/       $$$/    $$$ |$$ |$$ |  $$ |
                                                        $$/   $$$$$$/   $$$$$$/        $$/      $$/ $$/ $$/   $$/ 
'''

defeat_image = '''
                                                                                                                       dddddddd
YYYYYYY       YYYYYYY                                     DDDDDDDDDDDDD          iiii                                  d::::::d
Y:::::Y       Y:::::Y                                     D::::::::::::DDD      i::::i                                 d::::::d
Y:::::Y       Y:::::Y                                     D:::::::::::::::DD     iiii                                  d::::::d
Y::::::Y     Y::::::Y                                     DDD:::::DDDDD:::::D                                          d:::::d 
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu         D:::::D    D:::::D iiiiiii     eeeeeeeeeeee        ddddddddd:::::d 
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         D:::::D     D:::::Di:::::i   ee::::::::::::ee    dd::::::::::::::d 
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u         D:::::D     D:::::D i::::i  e::::::eeeee:::::ee d::::::::::::::::d 
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u         D:::::D     D:::::D i::::i e::::::e     e:::::ed:::::::ddddd:::::d 
      Y:::::::Y   o::::o     o::::ou::::u    u::::u         D:::::D     D:::::D i::::i e:::::::eeeee::::::ed::::::d    d:::::d 
       Y:::::Y    o::::o     o::::ou::::u    u::::u         D:::::D     D:::::D i::::i e:::::::::::::::::e d:::::d     d:::::d 
       Y:::::Y    o::::o     o::::ou::::u    u::::u         D:::::D     D:::::D i::::i e::::::eeeeeeeeeee  d:::::d     d:::::d 
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u         D:::::D    D:::::D  i::::i e:::::::e           d:::::d     d:::::d 
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu     DDD:::::DDDDD:::::D  i::::::ie::::::::e          d::::::ddddd::::::dd
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u     D:::::::::::::::DD   i::::::i e::::::::eeeeeeee   d:::::::::::::::::d
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u     D::::::::::::DDD     i::::::i  ee:::::::::::::e    d:::::::::ddd::::d
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu     DDDDDDDDDDDDD        iiiiiiii    eeeeeeeeeeeeee     ddddddddd   ddddd
'''

engine = create_engine("sqlite:///monsterhunterdb.db")
Session = sessionmaker(bind=engine)
session = Session()


def action_round(character_name):
    character = get_character_stats(character_name)
    actions = ["Attack", "Defend", "Heal"]

    monster = get_next_monster_in_sequence()
    if monster:
        monster.health = monster.monster_default_health
    else:
        print("\nCongratulations! You've defeated all the monsters!")
        return

    while character.health > 0 and monster.health > 0:
            print(f"\n{character.name}'s Health: {character.health}")
            print(f"{monster.name}'s Health: {monster.health}")

            player_action = input(f"What will {character.name} do against {monster.name}? ({'/'.join(actions)}): ")  
            player_result = execute_action(character, player_action)
            monster_action = random.choice(actions)
            monster_result = execute_action(monster, monster_action)

            if player_action == "Attack":
                monster.health -= player_result
            elif player_action == "Heal":
                character.health += player_result
                character.health = min(character.health, character.default_health)

            if monster_action == "Attack":
                character.health -= monster_result
            elif monster_action == "Heal":
                monster.health += monster_result

            save_action_round(character.name, player_action, player_result)

            if monster.health <= 0:
                print(f"\nCongratulations! You defeated {monster.name}!")
                item_dropped = get_random_item()
                print(f"\n{monster.name} dropped an item: {item_dropped.name}!")
                add_item_to_inventory(character_name, item_dropped.id)
                print(f"{item_dropped.name} has been added to {character.name}'s inventory!")


            elif character.health <= 0:
                print(defeat_image)  # Print the ASCII art for defeat
                print(f"\nOh no! {monster.name} defeated you!")
                break

def display_character_stats(character_name):
    character = get_character_stats(character_name)
    character.health = character.default_health  # Reset the character's health to default
    print(f"\nStats for {character.name}:")
    print(f"Health: {character.health}")
    print(f"Attack: {character.attack}")
    print(f"Defense: {character.defense}")

def main():
    clear_inventory()
    print(startup_image)
    print("Welcome to Monster Hunter CLI!")

    characters = get_all_character_names()
    for index, character in enumerate(characters, 1):
        print(f"{index}. {character[0]} - {character[1]}")

    choice = int(input("Choose your character: "))
    chosen_character_name = characters[choice - 1][0]

    display_character_stats(chosen_character_name)
    input("\nPress Enter to continue...")

    character = get_character_stats(chosen_character_name)

    print(f"\nYou've chosen {character.name}!")

    # Reset both monster and character health
    reset_all_monsters_health()  

    # Reinitialize monster_order every time the game is played
    global monster_order
    monster_order = ["Undead Skeleton", "Gigantic Troll", "Alduin the Dragon"]

    while True:
        action_round(chosen_character_name)  # Start the action round
        print(f"\nPress Enter to continue...")
        input()  # Wait for the user to press Enter

    input("\nPress Enter to exit the game.")

if __name__ == '__main__':
    main()
            

