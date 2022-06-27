from tkinter import *

# Cores
cor0 = "#f0f3f5"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#4fa882"  # Verde
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"  # Letra
cor5 = "#e06636"  # - profit
cor6 = "#038cfc"  # Azul
cor7 = "#ef5350"  # Vermelho
cor8 = "#263238"  # + verde
cor9 = "#e9edf5"  # Sky blue

# Configuração inicial da tela
janela = Tk()
janela.title('Consultas')
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

# Divisão das Janelas
frame_cima = Frame(janela, width=310, height=50, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1,sticky=NSEW)

frame_direita = Frame(janela, width=588, height=403, bg=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

# Tela cima
app_nome = Frame(frame_cima, text='Formulário de Consulta', anchor=NW)
app_nome.grid(row=0, column=0)

janela.mainloop()
