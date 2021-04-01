from colorama import Fore


print("=-" * 20)
print(f"{'Busca de palavra-chave':^20}")
print("=-" * 20)

Arquivo = input('Insira uma lista em formato "*.txt": ')
cont = 0
lista = []
#Exemplo: C:\\Users\\Suu\\Documents\\Lista de frutas.txt
#C:\\Users\\Suu\\Documents\\Lista de games.txt

with open(Arquivo, 'r', encoding='UTF-8') as f:
    dados = f.readlines()
    for linha in dados:
        for i in linha.split(', '):
            lista.append(i)

Keyword = input("Dê uma palavra-chave: ").strip().capitalize()

for item in lista:
    if item.lower() == Keyword.lower():
        print(Fore.BLUE + f'"{Keyword}" está na {lista.index(Keyword)}ª posição da lista!' + Fore.RESET)
        cont += 1
        break
if cont == 0:
    print(Fore.RED + f'Infelizmente "{Keyword}" não está na lista...' + Fore.RESET)