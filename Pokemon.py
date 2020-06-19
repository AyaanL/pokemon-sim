import random
import Attack





class Pokemon:
    hp=100
    attacks=[Attack]

  
        


def choose_move(player_one):
    print("choose from these moves: ")
    for a in player_one.pokemon.attacks:
        print(a.name)
    move=input("which move would you like to select (1 or 2)")
    return move 
        
def attack_pokemon(move,player_attacking,player_defending):
    if move=="1":
        player_defending.pokemon.hp -= player_attacking.pokemon.attacks[0].damage
    elif move=="2":
        player_defending.pokemon.hp -= player_attacking.pokemon.attacks[1].damage

def choose_move2():
    numbers=["1","2"]
    move=random.choice(numbers)
    print("player_two is attacking with ",move)
    return move


def print_hp(player_one,player_two):
    print("player one your hp is")
    print(player_one.pokemon.hp)
    print("player two your hp is")
    print(player_two.pokemon.hp)




# Greeting











        