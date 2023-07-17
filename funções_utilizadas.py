def mensagem_enfeitada(msg, tamanho_da_mensagem=0):
    tamanho_da_mensagem = len(msg) + 2
    print('-' * tamanho_da_mensagem)
    print(' ' + msg)
    print('-' * tamanho_da_mensagem)


def linha(tamanho=30):
    print('-'*tamanho)


def verifica_loop(resposta_do_usuario):
    if resposta_do_usuario != 's' and resposta_do_usuario != 'n':
        while resposta_do_usuario != 's' and resposta_do_usuario != 'n':
            print('Opção incorreta!')
            resposta_do_usuario = str(input('Quer continuar? [s/n]')).lower()


def gerar_citacao():
    import sqlite3
    from random import randint
    with sqlite3.connect('citações.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
        SELECT * FROM citacoes''')
        total_citacoes = len(cursor.fetchall())
        id_aleatorio = randint(1, total_citacoes)
        cursor.execute('''
        SELECT citacao, autor FROM citacoes
        WHERE id_citacao = ?''', (id_aleatorio,))
        return cursor.fetchone()

