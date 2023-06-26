# Cadastrando citações
import sqlite3

conexao = sqlite3.connect('citações.db')
cursor = conexao.cursor()
cursor.execute('''create table citacoes(
    id_citacao INTEGER PRIMARY KEY AUTOINCREMENT,
    citacao TEXT,
    autor TEXT)''')
