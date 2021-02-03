Arquivo = input(print("Insira uma lista em formato .txt:"))
Lista = []
#Exemplo: C:\\Users\\Suu\\Documents\\Lista de frutas.txt
#C:\\Users\\Suu\\Documents\\Lista de games.txt

with open(Arquivo, 'r', encoding='UTF-8') as f:
    Dados = f.readlines()
    for linha in Dados:
        for i in linha.split(','):
            Lista.append(i)
            print(Lista)
            
Keyword = input(print("Dê uma palavra-chave: "))

for item in Lista:
    print(item, Lista.index(item))
    if item != Keyword:
        print('A palavra-chave não está na lista')
    else:
        print("Foi encontrada a palavra-chave na lista, na posição: ", Lista.index(Keyword))



