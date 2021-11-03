import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        fighters = [self, opponent]
        winner = random.choice(fighters).name
        print(f'{winner} is the winner')

if __name__ == "__main__ ":
    my_hero = Hero("grace hopper", 200)
    hero2 = Hero("batman", 300)
    my_hero.fight(hero2)
    print(my_hero.name)
    print(my_hero.current_health)
