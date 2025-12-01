import tkinter as tk
from Classes_Functions import *


# ========= Instanciar Janela =========
root = tk.Tk()
root.geometry('1400x700')
root.title('DashBoard Clima')
root.resizable(False, False)
root.configure(bg='#17517E')



# ===== Entry =====
barradebusca = tk.Entry(root, width=50, bd=0, font=('arial',15))
barradebusca.place(x=120, y=50)


# ===== Botão =====
botaopesquisa = tk.Button(root, text='Buscar',command=lambda: botaopesquisar(root,barradebusca),bd=0)
botaopesquisa.place(x=70, y=50)


# ===== Labels =====
textobarradebuscalabel = tk.Label(root,text='Insira o nome da Cidade que deseja buscar',font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
textobarradebuscalabel.place(x=120, y=25)

Condicaolabel = tk.Label(root,text="Clima Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
Condicaolabel.place(x=120, y=200)

descricaolabel = tk.Label(root,text="Condição Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
descricaolabel.place(x=120, y=230)

temperaturalabel = tk.Label(root,text="Temperatura Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
temperaturalabel.place(x=120, y=260)

umidadelabel = tk.Label(root,text="Umidade Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
umidadelabel.place(x=120, y=290)


root.mainloop()

