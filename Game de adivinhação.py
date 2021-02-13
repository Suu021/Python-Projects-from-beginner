from random import randint
from time import sleep

num_sorteado = randint(0, 9)
print("-=-" * 20)
print("Vou pensar em um número de 0 a 9. Tente adivinhar...")
print("-=-" * 20)
sleep(1)
num = int(input("E então, qual o número que eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if num == num_sorteado:
    print("Parabéns, você acertou!")
else:
    print("Você errou, o número era: ", num_sorteado)