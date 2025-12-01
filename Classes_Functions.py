import requests
import customtkinter as ctk
from PIL import Image

Debug = False

#==== Imgs ====
frioimage = ctk.CTkImage(Image.open("imgs/cold.png"),size=(16,16))
sunimage = ctk.CTkImage(Image.open("imgs/sun.png"),size=(16,16))

class Dados:
    def __init__(self, dados_json):
        # Clima
        self.condicao = dados_json["weather"][0]["main"]
        self.descricao = dados_json["weather"][0]["description"]

        # Coordenadas
        self.latitude = dados_json["coord"]["lat"]
        self.longitude = dados_json["coord"]["lon"]

        # Temperatura
        temperaturajs = dados_json["main"]["temp"]
        self.temperatura = round(temperaturajs - 273.15)

        temperaturaminjs = dados_json["main"]["temp_min"]
        self.temperaturamin = round(temperaturaminjs - 273.15)

        temperaturamaxjs = dados_json["main"]["temp_max"]
        self.temperaturamax = round(temperaturamaxjs - 273.15)

        temperatursensjs = dados_json["main"]["feels_like"]
        self.temperatursens = round(temperatursensjs - 273.15)

        # Outros
        self.umidade = dados_json["main"]["humidity"]
        self.vento = dados_json["wind"]["speed"]


def funcaopesquisar(root,barradebusca):

    try:

        # ==== buscar cordenadas ====

        cidadenome= barradebusca.get()

        urlgeo = (
            f"https://api.openweathermap.org/geo/1.0/direct?"
            f"q={cidadenome}&limit=1&appid=" #sua chave aqui
        )


        respostageo = requests.get(urlgeo)
        cidade = respostageo.json()

        if Debug:
            print(cidade)

        if len(cidade) == 0:
            respostaresquestlabel = ctk.CTkLabel(root,text="Cidade não encontrada!",font=('arial',15),text_color='#FF5555')
            respostaresquestlabel.place(x=120, y=80)
            return

        lat = cidade[0]["lat"]
        lon = cidade[0]["lon"]

        # ==== buscar clima ====

        url_clima = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid=" #sua chave aqui
        )

        resposta = requests.get(url_clima)
        dados = Dados(resposta.json())

        if Debug:
            print(resposta.json())

        # ==== Exibir Valores Labels====

        respostaresquestlabel = ctk.CTkLabel(root,text="Dados Encontrados!                     ",font=('arial',15),text_color='#55FF55')
        respostaresquestlabel.place(x=120, y=80)

        condicaoresquestlabel = ctk.CTkLabel(root, text=f"{dados.condicao}                     ", font=("Arial", 20), text_color='#FFFFFF')
        condicaoresquestlabel.place(x=320, y=170)

        descricaoresquestlabel = ctk.CTkLabel(root, text=f"{dados.descricao}                   ", font=("Arial", 20), text_color='#FFFFFF')
        descricaoresquestlabel.place(x=320, y=210)

        # Temperaturas

        temperaturarequestlabel = ctk.CTkLabel(root, text=f"{dados.temperatura}°C              ", font=("Arial", 20), text_color='#FFFFFF')
        temperaturarequestlabel.place(x=320, y=250)

        temperaturaminrequestlabel = ctk.CTkLabel(root, text=f"Temp.Min.{dados.temperaturamin} °C - ", font=("Arial", 20), text_color='#FFFFFF')
        temperaturaminrequestlabel.place(x=380, y=250)

        temperaturamaxrequestlabel = ctk.CTkLabel(root, text=f"Temp.Max.{dados.temperaturamax} °C   ", font=("Arial", 20),text_color='#FFFFFF')
        temperaturamaxrequestlabel.place(x=540, y=250)

        temperaturasensrequestlabel = ctk.CTkLabel(root, text=f"Sensação Termica {dados.temperatursens} °C     ", font=("Arial", 20), text_color='#FFFFFF')
        temperaturasensrequestlabel.place(x=320, y=290)

        umidaderequestlabel = ctk.CTkLabel(root, text=f"{dados.umidade}%            ", font=("Arial", 20), text_color='#FFFFFF')
        umidaderequestlabel.place(x=320, y=330)

        ventorequestlabel = ctk.CTkLabel(root, text=f"{dados.vento}m/s             ", font=("Arial", 20), text_color='#FFFFFF')
        ventorequestlabel.place(x=320, y=370)

        if dados.temperatura > 25:
            imgquente = ctk.CTkImage(Image.open("imgs/sun.png"),size=(150,150),)
            imbquentelabel = ctk.CTkLabel(root, text='',image=imgquente,width=150,height=150)
            imbquentelabel.place(x=900, y=120)
            root.configure(fg_color="dark red")
        else:
            imgfrio = ctk.CTkImage(Image.open("imgs/cold.png"),size=(150,150))
            imgfrolabel = ctk.CTkLabel(root, text='',image=imgfrio,width=150,height=150)
            imgfrolabel.place(x=900, y=120)
            root.configure(fg_color="dark blue")





    except Exception as e:
        print(e)
        exceptrequestlabel = ctk.CTkLabel(root,text="Ocorreu um erro!",font=("Arial", 15), text_color='#FF5555')
        exceptrequestlabel.place(x=120, y=80)





