import requests
import tkinter as tk

class Dados:
    def __init__(self, dados_json):
        # Clima
        self.condicao = dados_json["weather"][0]["main"]
        self.descricao = dados_json["weather"][0]["description"]

        # Coordenadas
        self.latitude = dados_json["coord"]["lat"]
        self.longitude = dados_json["coord"]["lon"]

        temperatura_kelvin = dados_json["main"]["temp"]
        self.temperatura = round(temperatura_kelvin - 273.15)

        self.umidade = dados_json["main"]["humidity"]


def botaopesquisar(root,barradebusca):

    # ==== buscar cordenadas ====

    cidadenome= barradebusca.get()

    urlgeo = (
        f"https://api.openweathermap.org/geo/1.0/direct?"
        f"q={cidadenome}&limit=1&appid=19e5b3f3a7ba81f1e8734ada48104bcc"
    )

    respostageo = requests.get(urlgeo)
    cidade = respostageo.json()

    if len(cidade) == 0:
        print("Cidade não encontrada")
        return

    lat = cidade[0]["lat"]
    lon = cidade[0]["lon"]

    # ==== buscar clima ====

    url_clima = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid=19e5b3f3a7ba81f1e8734ada48104bcc"
    )

    resposta = requests.get(url_clima)
    dados = Dados(resposta.json())

    # ==== exibir ====

    condicaoresquestlabel = tk.Label(root, text=dados.condicao, font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    condicaoresquestlabel.place(x=200, y=200)

    descricaoresquestlabel = tk.Label(root, text=dados.descricao, font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    descricaoresquestlabel.place(x=225, y=230)

    temperaturarequestlabel = tk.Label(root, text=f"{dados.temperatura}°C", font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    temperaturarequestlabel.place(x=250, y=260)


    umidaderequestlabel = tk.Label(root, text=f"{dados.umidade}%", font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    umidaderequestlabel.place(x=225, y=290)


