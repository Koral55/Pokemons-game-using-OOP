import random
from Names import list_of_enemy_pokemons
from Classes import Pokemon, Enemy
from Functions import list_of_pokemons, list_of_pokemons_names, kills, \
    option_1_func, create_pokemon, \
    option_2_func, \
    option_3_func, which_pokemon, indexing, pokemon_turn, enemy_turn, stats_showing, battle


print("Close the game: 0;  Create pokemon: 1;  Check pokemons stats: 2; Battle: 3;")
while True:
    input_value_menu = int(input(":"))
    if input_value_menu == 0:
        break
    elif input_value_menu == 1:
        option_1_func()
    elif input_value_menu == 2:
        option_2_func()
    elif input_value_menu == 3:
        option_3_func()
        break
