from monster import Monster
from player import Player
import dice

def generate_map():
    pass

def generate_characters():
    bunyip = Monster("Bunyip", 100, 100, 100, "claws","a fuzzy wild bunyip")
    return bunyip

print("Welcome to the game!")
player_name = input("Please enter your name: ")
print(f"Hello {player_name}, welcome to the game. The first thing we will do is create a character")
character_name = input("Please enter character name: ")
character_class = input("Please enter charcter class: ")
character = Player(character_name,  character_class)

generate_map()
monster_1 = generate_characters()

print(f"Welcome {character.name} to the world of the Country Womens Association.")
print(f"You are walking through the bushland and come across {monster_1.monster_class}")
print("What are you going to do? Fight or Run away?")
player_choice = input("> ")
if player_choice == "Fight":
    roll = dice.roll_d20()
    character.attack(roll,monster_1)    


