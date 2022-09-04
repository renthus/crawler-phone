import requests

URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(resposta.text)
        else:
            print("Erro ao fazer a requisição!")

    except Exception as error:
        print("Erro Desconhecido!")
        print(error)

buscar(URL_AUTOMOVEIS)