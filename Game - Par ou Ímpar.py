from random import randint
from time import sleep


cont_vitoria = 0
while True:
    print("=-=" * 20)
    print("Jogo de par ou impar...")
    par_ou_impar = str(input("Você escolhe Par ou Impar? ")).strip().upper()[0]
    while par_ou_impar not in "PpIi":
        print("Digitou uma opção inválida, tente de novo...")
        par_ou_impar = str(input("Você escolhe Par ou Impar? ")).strip().upper()[0]
        if par_ou_impar in "PpIi":
            break
    num = int(input("Qual número você escolhe? de 0 a 9: "))
    print("=-=" * 20)
    if par_ou_impar in "Pp":
        pc = "I"
    else:
        pc = "P"
    num_pc = randint(0, 9)
    print("PROCESSANDO...")
    sleep(1)
    if (num + num_pc) % 2 == 0:
        vencedor = "Par"
    else:
        vencedor = "Impar"
    print(f"Você jogou {num} e o PC jogou {num_pc}, total de {num + num_pc}. Deu {vencedor}!")
    if par_ou_impar == vencedor[0]:
        cont_vitoria += 1
        print(f"Parabéns, você venceu o PC pela {cont_vitoria}ª vez!")
    else:
        print(f"Que pena, você perdeu para o PC... Mas conquistou {cont_vitoria} vitória(s)!")
        break
