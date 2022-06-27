from cgitb import text
from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry

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
app_nome = Label(frame_cima, text='Formulário de Consulta', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1, relief='flat')
app_nome.place(x=10, y=20)

# Configuração tela preenchimento
# Nome
label_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_nome.place(x=10, y=10)
entry_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_nome.place(x=15, y=40)

# Email
label_email = Label(frame_baixo, text='E-mail', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_email.place(x=10, y=70)
entry_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_email.place(x=15, y=100)

# Telefone
label_telefone = Label(frame_baixo, text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_telefone.place(x=10, y=130)
entry_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_telefone.place(x=15, y=160)

# Data da consulta
label_calendario = Label(frame_baixo, text='Data da Consulta', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_calendario.place(x=10, y=190)
entry_calendario = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_calendario.place(x=15, y=40)

# Prioridade
label_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_nome.place(x=10, y=10)
entry_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_nome.place(x=15, y=40)

# Consulta sobre
label_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_nome.place(x=10, y=10)
entry_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_nome.place(x=15, y=40)

janela.mainloop()
