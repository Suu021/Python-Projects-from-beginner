import requests
import json

def Requisicao(titulo, key):
    try:
        req = requests.get("http://www.omdbapi.com/?apikey=" + key + "&t=" + titulo)
        dic = json.loads(req.text)
        return dic
    except:
        print("Algo deu errado")
        return None

def Detalhes_do_filme(filme):
    print('Título: ', filme["Title"])
    print('Ano: ', filme["Year"])
    print('Gênero: ', filme["Genre"])
    print('Diretor: ', filme["Director"])
    print('Atores: ', filme["Actors"])
    print('Nota: ', filme["imdbRating"])
    print('Sinopse: ', filme["Plot"])
    print('')

sair = False
while not sair:
    opcao = input("Digite o título do filme ou digite SAIR para fechar: ")
    if opcao == "sair":
        sair = True
        print("Saindo...")
    else:
        APIkey = '3b2bd4af'
        filme = Requisicao(opcao, APIkey)
        Detalhes_do_filme(filme)
        if filme["Response"] == 'False':
            print("Filme não encontrado!")
        else:
            Detalhes_do_filme(filme)