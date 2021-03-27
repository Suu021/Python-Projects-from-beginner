import requests
import json

def Requisicao(titulo, key):
    try:
        req = requests.get(f"http://www.omdbapi.com/?apikey={key}&t={titulo}")
        dic = json.loads(req.text)
        return dic
    except:
        print("Algo deu errado!")
        return None

def Detalhes_do_filme(filme):
    print(f'~~'*20)
    print(f'Título: {filme["Title"]}')
    print(f'Ano: {filme["Year"]}')
    print(f'Gênero: {filme["Genre"]}')
    print(f'Diretor: {filme["Director"]}')
    print(f'Atores: {filme["Actors"]}')
    print(f'Nota: {filme["imdbRating"]}')
    print(f'Sinopse: {filme["Plot"]}')
    print(f'~~'*20)

print("=-"*20)
print(f"{'Consulte informações de filmes':^40}")
print("=-"*20)

while True:
    opcao = input("Digite o título do filme ou digite SAIR para fechar: ").strip()
    if opcao.upper() == "SAIR":
        print("Saindo...")
        break
    else:
        APIkey = '3b2bd4af'
        filme = Requisicao(opcao, APIkey)
        if filme["Response"] == 'False':
            print("Filme não encontrado!")
        else:
            Detalhes_do_filme(filme)
