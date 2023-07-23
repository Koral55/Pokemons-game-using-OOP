

class Pokemon:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def heal_func(self, heal_number):
        self.health = self.health + heal_number

    def attack_func(self, enemy):
        enemy.health = enemy.health - self.attack



class Enemy:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def attack_func(self, pokemon):
        pokemon.health = pokemon.health - self.attack
