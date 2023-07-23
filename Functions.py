import random
from Names import list_of_enemy_pokemons
from Classes import Pokemon, Enemy


list_of_pokemons = []
list_of_pokemons_names = []
kills = 0

""" OPTION 1"""
def create_pokemon(name, attack, health):        #this function creates pokemon object ads it to list of pokemons
    name = Pokemon(name, attack, health)
    if bool(list_of_pokemons):
        for x in list_of_pokemons:
            if x.name == name.name:
                print("That pokemon has already been created")
            else:
                list_of_pokemons.append(name)
                print("Pokemon has been created")
    else:
        list_of_pokemons.append(name)
        print("Pokemon has been created")

def option_1_func():        #this function acquires name, attack and health value for pokemon object and creates it
    if len(list_of_pokemons) == 2:
        print("You can't create more than 2 pokemons")
    else:
        name_input = input("What will be pokemon's name? ")
        attack_input = random.randrange(10, 30)
        health_input = random.randrange(1, 100)
        create_pokemon(name_input, attack_input, health_input)



""" OPTION 2"""
def option_2_func():        #this function shows stats of your pokemons
    if len(list_of_pokemons) != 0:
        for x in list_of_pokemons:
            if x.name in list_of_pokemons_names:
                pass
            else:
                list_of_pokemons_names.append(x.name)
        which_pokemon_menu = input(f"Which pokemon's stats do you want to see? Available: {list_of_pokemons_names} ")
        for x in list_of_pokemons:
            if which_pokemon_menu == x.name:
                print(f"{x.name}:  Attack: {x.attack};  Health: {x.health}")
                break
            else:
                if which_pokemon_menu in list_of_pokemons_names:
                    pass
                else:
                    print("Such pokemon has not been created")
                    break
    else:
        print("No pokemons have been created")



""" OPTION 3"""

def which_pokemon():        #this function creates variable "current_pokemon_index" which tells us which pokemon is the player using
    if len(list_of_pokemons) != 0:
        for x in list_of_pokemons:
            if x.name in list_of_pokemons_names:
                pass
            else:
                list_of_pokemons_names.append(x.name)
        which_pokemon_battle_start = input(f"Choose pokemon which you think is stronger! Available: {list_of_pokemons_names}")
        for x in list_of_pokemons:
            if which_pokemon_battle_start == x.name:
                print(f"{which_pokemon_battle_start} has been chosen!")
                global current_pokemon_index
                current_pokemon_index = list_of_pokemons.index(x)
                break
            else:
                if which_pokemon_battle_start in list_of_pokemons_names:
                    pass
                else:
                    print("Such pokemon does not exist")
                    break
    else:
        print("No pokemons have been created")


def indexing():     #this function creates "pokemon" and "enemy" variables and assigns correct objects to them
    global pokemon
    global enemy
    pokemon = list_of_pokemons[current_pokemon_index]
    enemy = Enemy(random.choice(list_of_enemy_pokemons), random.randrange(1, 30), random.randrange(1, 100))

def pokemon_turn():
    print("Your turn!")
    print("Attack: 1; Heal: 2;")
    input_value_battle = int(input(":"))
    if input_value_battle == 1:
        pokemon.attack_func(enemy)
        print(f"{pokemon.name} attacks!")
    elif input_value_battle == 2:
        heal_number = random.randrange(0, 50)
        pokemon.heal_func(heal_number)
        print(f"{pokemon.name} has been healed by {heal_number} points!")

def enemy_turn():
    print("Enemy turn!")
    enemy.attack_func(pokemon)
    print(f"{enemy.name} attacks!")

def stats_showing():
    print(f"Stats: {pokemon.name}: Attack: {pokemon.attack}; Health:{pokemon.health};  {enemy.name}: Attack: {enemy.attack}; Health: {enemy.health}")

def battle():
    global kills
    while True:
        indexing()
        if pokemon.health > 0:
            print(f"A wild {enemy.name} appeared!")
            stats_showing()
            while True:
                pokemon_turn()
                if pokemon.health <= 0 or enemy.health <= 0:
                    if enemy.health <= 0:
                        print(f"{enemy.name} has been defeated!")
                        kills += 1
                        break
                    else:
                        break
                enemy_turn()
                if pokemon.health <= 0 or enemy.health <= 0:
                    if enemy.health <= 0:
                        print(f"{enemy.name} has been defeated!")
                        kills += 1
                        break
                    else:
                        break
                stats_showing()

        else:
            break
def option_3_func():
    which_pokemon()
    battle()
    print(f"You lost! Number of pokemons defeated: {kills}")
