import sqlite3 as lite



# Criando a conexão
conexao = lite.connect('dados.db')

lista = ['Fulano', 'fulano@gmail.com', 123456789, '27/06/2022', 'Normal', 'Clínico Geral']

# Inserir
with conexao:
    cursor = conexao.cursor()
    query = 'INSERT INTO formulario (nome, email, telefone, dia_consulta, prioridade, assunto) VALUES(?, ?, ?, ?, ?, ?)'
    cursor.execute(query, lista)

# Acessar Informações
with conexao:
    cursor = conexao.cursor()
    query = 'SELECT * FROM formulario'
    cursor.execute(query)
    info = cursor.fetchall()
    print(info)

# Atualizar
with conexao:
    cursor = conexao.cursor()
    query = 'UPDATE formulario SET nome=? WHERE id=?'
    cursor.execute(query, lista)

# Deletar
with conexao:
    cursor = conexao.cursor()
    query = 'DELETE FROM formulario WHERE id=?'
    cursor.execute(query, lista)

