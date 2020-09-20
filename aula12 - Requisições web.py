import requests

'''Antes de importar o "requests" é preciso instalar o pip3 através do terminal com o comando "pip3 install requests".

É interessante usar o "try" e "except" em requisições web'''

texto = None
try:
    requisição = requests.get('https://g1.com.br')
    print(requisição.text)

except Exception as erro:
    print("A requisição deu erro: ", erro)

print(texto)

#Existe outra biblioteca chamada Beautiful Soup 4, pode ser intalada através do comando "pip install bd4".
