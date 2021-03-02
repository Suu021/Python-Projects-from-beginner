from random import randint
from time import sleep

jogada = int(input('''Vamos jogar jokenpo!
0- Pedra;
1- Papel;
2- Tesoura.
Qual a sua jogada? '''))

jogada_IA = randint(0, 3)
embate = str(jogada)+str(jogada_IA)
dic_jogadas = {
     "02": 'Parabéns, você venceu!',
     "10": 'Parabéns, você venceu!',
     "21": 'Parabéns, você venceu!',
     "20": 'Que pena, a IA te venceu!',
     "01": 'Que pena, a IA te venceu!',
     "12": 'Que pena, a IA te venceu!',
     "00": 'Deu empate!',
     "11": 'Deu empate!',
     "22": 'Deu empate!'
}
itens = ["Pedra", "Papel", "Tesoura"]
print("=-"*20)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("=-"*20)
print("Você escolheu {} e a IA escolheu {}...".format(itens[jogada], itens[jogada_IA]))
print(dic_jogadas[embate])
print("=-"*20)