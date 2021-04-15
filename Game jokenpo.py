from random import randint
from time import sleep

player_move = int(input('''let's play jokenpo!
     0- Rock;
     1- Paper;
     2- Scissors.
     Whats your move? '''))
while player_move > 2 or player_move < 0:
    player_move = int(input("Invalid Input! Try again... Whats your move? "))
    if 0 <= player_move <= 2:
        break

AI_move = randint(0, 2)
clash = str(player_move) + str(AI_move)
dic_moves = {
    "02": 'Congratulations, you won!',
    "10": 'Congratulations, you won!',
    "21": 'Congratulations, you won!',
    "20": 'Too bad, AI beat you!',
    "01": 'Too bad, AI beat you!',
    "12": 'Too bad, AI beat you!',
    "00": 'It was a draw!',
    "11": 'It was a draw!',
    "22": 'It was a draw!'
}
itens = ("Rock", "Paper", "Scissors")
print("=-" * 20)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("=-" * 20)
print(f"You chose {itens[player_move]} and AI chose {itens[AI_move]}...")
print(dic_moves[clash])
print("=-" * 20)
