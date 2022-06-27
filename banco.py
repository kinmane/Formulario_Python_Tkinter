# Importando SQLite
import sqlite3 as lite

# Criando conexão
conexao = lite.connect('dados.db')

# Criando tabelas
with conexao:
    cur = conexao.cursor()
    cur.execute('CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_consulta DATE, prioridade TEXT, assunto TEXT)')
