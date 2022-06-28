from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from view import *

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
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_direita = Frame(janela, width=588, height=403, bg=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Tela cima
app_nome = Label(frame_cima, text='Formulário de Consulta', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1, relief='flat')
app_nome.place(x=10, y=20)

global tree


def inserir():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    calendario = entry_calendario.get()
    prioridade = entry_prioridade.get()
    especialista = entry_especialista.get()

    lista = [nome, email, telefone, calendario, prioridade, especialista]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        entry_prioridade.delete(0, 'end')
        entry_especialista.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()


def atualizar():
    try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        tree_lista = treeview_dicionario['values']

        valor_id = tree_lista[0]

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        entry_prioridade.delete(0, 'end')
        entry_especialista.delete(0, 'end')

        entry_nome.insert(0, tree_lista[1])
        entry_email.insert(0, tree_lista[2])
        entry_telefone.insert(0, tree_lista[3])
        entry_calendario.insert(0, tree_lista[4])
        entry_prioridade.insert(0, tree_lista[5])
        entry_especialista.insert(0, tree_lista[6])

        def update():
            nome = entry_nome.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            dia_consulta = entry_calendario.get()
            prioridade = entry_prioridade.get()
            assunto = entry_especialista.get()

            lista = [nome, email, telefone, dia_consulta, prioridade, assunto, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')
                entry_calendario.delete(0, 'end')
                entry_prioridade.delete(0, 'end')
                entry_especialista.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        botao_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 8 bold'), bg=cor2, fg=cor1, relief='raised', overrelief='ridge')
        botao_confirmar.place(x=112, y=368)


    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def deletar():
    try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        tree_lista = treeview_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'O dado foi deletado com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


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
label_calendario.place(x=15, y=190)
entry_calendario = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, locale='pt_BR')
entry_calendario.place(x=15, y=220)

# Prioridade
label_prioridade = Label(frame_baixo, text='Prioridade', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_prioridade.place(x=160, y=190)
entry_prioridade = Entry(frame_baixo, width=21, justify='left', relief='solid')
entry_prioridade.place(x=160, y=220)

# Especialista
label_especialista = Label(frame_baixo, text='Especialista', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_especialista.place(x=15, y=260)
entry_especialista = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_especialista.place(x=15, y=290)

# Botões
botao_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 8 bold'), bg=cor6, fg=cor1, relief='raised', overrelief='ridge')
botao_inserir.place(x=15, y=340)
botao_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 8 bold'), bg=cor2, fg=cor1, relief='raised', overrelief='ridge')
botao_atualizar.place(x=112, y=340)
botao_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 8 bold'), bg=cor7, fg=cor1, relief='raised', overrelief='ridge')
botao_deletar.place(x=210, y=340)


def mostrar():
    global tree
    # Tabelas
    lista = mostrar_info()

    nomes_listas = ['ID', 'Nome', 'E-mail', 'Telefone', 'Data', 'Prioridade', 'Especialista']

    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=nomes_listas, show='headings')

    vertical_scrollbar = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.xview)

    horizontal_scrollbar = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    tree.grid(column=0, row=0, sticky='NSEW')
    vertical_scrollbar.grid(column=1, row=0, sticky='NS')
    horizontal_scrollbar.grid(column=0, row=1, sticky='EW')

    frame_direita.grid_rowconfigure(0, weight=12)

    identacao_lista = ['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
    tamanho_tabela = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for coluna in nomes_listas:
        tree.heading(coluna, text=coluna.title(), anchor=CENTER)
        tree.column(coluna, width=tamanho_tabela[n], anchor=identacao_lista[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()
