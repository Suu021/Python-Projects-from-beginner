import requests
import json

def info_Clima(cidade, key):
    try:
        reqClima = requests.get('https://api.hgbrasil.com/weather/?format=json&city_name=' + cidade + '&key=' + key)
        resultado = json.loads(reqClima.text)
        return resultado['results']

    except Exception as erro:
        print('Algo deu errado: ', erro)
        return None

def info_Cotacao(key):

    try:
        reqCotacao = requests.get('https://api.hgbrasil.com/finance/quotations?format=json&key=' + key)
        resultado = json.loads(reqCotacao.text)
        return resultado['results']['currencies']

    except Exception as erro:
        print('Algo deu errado: ', erro)
        return None

def detalhes_Clima_e_Cotacao(clima, cotacao):
    print("=-="*20)
    print('Clima:')
    print(f'Cidade: {clima["city"]}')
    print(f'Temperatura: {str(clima["temp"])} °C')
    print(f'O dia está {clima["description"]}')
    print(f'Umidade relativa: {str(clima["humidity"])}%')
    print(f'Velocidade do vento: {clima["wind_speedy"]}')
    print("=-="*20)
    print('Cotacão:')
    print(f'Dólar: '
          f'\nCompra: {cotacao["USD"]["buy"]}; '
          f'\nVenda: {cotacao["USD"]["sell"]}; '
          f'\nVariação: {cotacao["USD"]["variation"]}')
    print('---'*20)
    print(f'Euro: '
          f'\nCompra: {cotacao["EUR"]["buy"]}; '
          f'\nVenda: {cotacao["EUR"]["sell"]}; '
          f'\nVariação: {cotacao["EUR"]["variation"]}')
    print('---'*20)
    print(f'Peso Argentino: '
          f'\nCompra: {cotacao["ARS"]["buy"]}; '
          f'\nVenda: {cotacao["ARS"]["sell"]};'
          f'\nVariação: {cotacao["ARS"]["variation"]}')
    print('---'*20)
    print(f'Bitcoin: '
          f'\nCompra: {cotacao["BTC"]["buy"]}; '
          f'\nVenda: {cotacao["BTC"]["sell"]}; '
          f'\nVariação: {cotacao["BTC"]["variation"]}')
    print('---'*20)


while True:
    opcao = input('Informe a sua cidade ou digite "sair" para fechar: ').strip().lower()
    if opcao == "sair":
        print("Saindo... Volte sempre!")
        break
    else:
        key = '23c8f6c7'
        clima = info_Clima(opcao, key)
        cotacao = info_Cotacao(key)
        detalhes_Clima_e_Cotacao(clima, cotacao)
