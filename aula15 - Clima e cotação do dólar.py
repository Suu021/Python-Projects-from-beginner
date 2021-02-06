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
    print('Clima:')
    print('Cidade: ', clima["city"])
    print('Temperatura: ', str(clima['temp']) + '°C')
    print('O dia está: ', clima['description'])
    print('Umidade relativa: ', str(clima['humidity']) + '%')
    print('Velocidade do vento: ', clima['wind_speedy'])
    print('')
    print('Cotacão:')
    print('Dólar: ', '\nCompra: ', cotacao['USD']['buy'], '\nVenda: ', cotacao['USD']['sell'], '\nVariação: ', cotacao['USD']['variation'])
    print('')
    print('Euro: ', '\nCompra: ', cotacao['EUR']['buy'], '\nVenda: ', cotacao['EUR']['sell'], '\nVariação: ', cotacao['EUR']['variation'])
    print('')
    print('Peso Argentino: ', '\nCompra: ', cotacao['ARS']['buy'], '\nVenda: ', cotacao['ARS']['sell'], '\nVariação: ', cotacao['ARS']['variation'])
    print('')
    print('Bitcoin: ', '\nCompra: ', cotacao['BTC']['buy'], '\nVenda: ', cotacao['BTC']['sell'], '\nVariação: ', cotacao['BTC']['variation'])
    print('')


sair = False
while not sair:
    opcao = input("Informe a sua cidade ou digite SAIR para fechar: ")
    if opcao == "sair":
        sair = True
        print("Saindo...")
    else:
        key = '23c8f6c7'
        clima = info_Clima(opcao, key)
        cotacao = info_Cotacao(key)
        detalhes_Clima_e_Cotacao(clima, cotacao)
