from Classes_Functions import *


# ==== Configurar Tema ====
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# ========= Instanciar Janela =========
root = ctk.CTk()
root.geometry('1200x600')
root.title('Dashboard Clima')
#root.configure(fg_color="dark blue")
root.resizable(False, False)

# ==== Imagens ====
botaoimage = ctk.CTkImage(Image.open("imgs/botaoimg.png"),size=(16,16))


# ===== Entrys =====
barradebusca = ctk.CTkEntry(master=root,placeholder_text="Insira a Cidade que Deseja Buscar", width=550, border_width=1, font=('arial',20),text_color='#FFFFFF')
barradebusca.focus_set()
barradebusca.bind("<Return>",lambda event: funcaopesquisar(root,barradebusca))
barradebusca.place(x=120, y=50)


# ===== Botões =====
botaopesquisa = ctk.CTkButton(root, text='Buscar', command=lambda: funcaopesquisar(root, barradebusca), border_width=0,image=botaoimage,width=100)
botaopesquisa.place(x=680, y=50)


# ===== Labels Estáticas =====
textobarradebuscalabel = ctk.CTkLabel(root,text='Insira o Nome da Cidade (Ex.:Paris,Île-de-France,França)', font=('arial',20),text_color='#FFFFFF',)
textobarradebuscalabel.place(x=120, y=20)


Condicaolabel = ctk.CTkLabel(root,text="Clima Atual: ",font=('arial',20),text_color='#FFFFFF')
Condicaolabel.place(x=120, y=170)

descricaolabel = ctk.CTkLabel(root,text="Descrição do Clima: ",font=('arial',20),text_color='#FFFFFF')
descricaolabel.place(x=120, y=210)

temperaturalabel = ctk.CTkLabel(root,text="Temperatura Atual: ",font=('arial',20),text_color='#FFFFFF')
temperaturalabel.place(x=120, y=250)

temperaturasenslabel = ctk.CTkLabel(root,text="Temperatura Termica: ",font=('arial',20),text_color='#FFFFFF')
temperaturasenslabel.place(x=120, y=290)

umidadelabel = ctk.CTkLabel(root,text="Umidade Atual: ",font=('arial',20),text_color='#FFFFFF')
umidadelabel.place(x=120, y=330)

ventolabel = ctk.CTkLabel(root,text="Vel. Vento Atual: ",font=('arial',20),text_color='#FFFFFF')
ventolabel.place(x=120, y=370)




root.mainloop()



