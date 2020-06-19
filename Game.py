import Pokemon
import Player
import Attack

print("Hello traveler")
question=input("What is your name: ")

player_one=Player.Player()
player_one.name=question

print("Welcome "+ player_one.name)

# Pokemon selection

fire=Attack.Attack()
fire.damage=20
fire.stun=True
fire.name="fire"

lightning=Attack.Attack()
lightning.damage=20
lightning.stun=True
lightning.name="lightning"

water=Attack.Attack()
water.damage=50
water.name="water"


air=Attack.Attack()
air.damage=30
air.name="air"

pikachu=Pokemon.Pokemon()
pikachu.attacks=[lightning,air]

squirttle=Pokemon.Pokemon()
squirttle.attacks=[water,fire]

selection=input("Which pokemon do you select (p or s) ")

while selection != "p" and selection != "s":
    print(selection)
    selection=input("dude (p or s) ") 

player_two=Player.Player()
player_two.name="cpu"

if selection=="p":
    print("You have chosen pikachu")
    player_one.pokemon=pikachu
    player_two.pokemon=squirttle

elif selection=="s":
    print("You have choen squirttle")
    player_one.pokemon=squirttle
    player_two.pokemon=pikachu




# battle

while player_one.pokemon.hp >0 and player_two.pokemon.hp >0:
    move=Pokemon.choose_move(player_one)
    Pokemon.attack_pokemon(move,player_one,player_two)
    move2=Pokemon.choose_move2()
    Pokemon.attack_pokemon(move2,player_two,player_one)
    Pokemon.print_hp(player_one,player_two)
