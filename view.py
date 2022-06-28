import sqlite3 as lite



# Criando a conexão
conexao = lite.connect('dados.db')

# Inserir
def inserir_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO formulario (nome, email, telefone, dia_consulta, prioridade, assunto) VALUES(?, ?, ?, ?, ?, ?)'
        cursor.execute(query, i)

# Acessar Informações
def mostrar_info():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        query = 'SELECT * FROM formulario'
        cursor.execute(query)
        informacao = cursor.fetchall()

        for infos in informacao:
            lista.append(infos)
    return lista

# Atualizar
def atualizar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'UPDATE formulario SET nome=?, email=?, telefone=?, dia_consulta=?, prioridade=?, assunto=?  WHERE id=?'
        cursor.execute(query, i)

# Deletar
def deletar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'DELETE FROM formulario WHERE id=?'
        cursor.execute(query, i)

