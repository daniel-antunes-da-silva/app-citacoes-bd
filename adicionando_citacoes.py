import sqlite3
from funções_utilizadas import verifica_loop, mensagem_enfeitada, linha

dados = {}
mensagem_enfeitada('Bem-vindo(a) ao sistema de gerenciamento de citações')
conexao = sqlite3.connect('citações.db')
cursor = conexao.cursor()
while True:
    linha()
    print('O que você deseja fazer?\n'
          '[1] - adicionar nova citação\n'
          '[2] - remover citação existente\n'
          '[3] - alterar citação existente\n'
          '[4] - ver todas as citações\n'
          '[5] - sair do sistema\n')
    escolha_do_usuario = str(input('Sua escolha: '))
    if escolha_do_usuario == '1':
        contador = 1
        while True:
            cursor.execute('SELECT * FROM citacoes')
            resultado = cursor.fetchall()
            if not resultado:
                dados['id_citacao'] = 1
            else:
                dados['id_citacao'] = len(resultado) + 1
            dados['citacao'] = str(input('Digite a citação: ')).strip()
            dados['autor'] = str(input('Nome do autor (caso não tenha, deixe em branco): ')).title().strip()
            if dados['autor'] == '':
                dados['autor'] = 'autor desconhecido'
            print(dados)
            confirm = str(input('Confirmar inserção no banco de dados? [s/n]')).lower()
            verifica_loop(confirm)
            if confirm != 'n':
                cursor.execute('''
                    INSERT INTO citacoes(id_citacao, citacao, autor)
                    values(:id_citacao, :citacao, :autor)
                    ''', dados)
                print('Citação inserida com sucesso!')
            else:
                conexao.commit()
            verif = str(input('Quer continuar? [s/n]')).lower()
            verifica_loop(verif)
            if verif == 'n':
                break
    elif escolha_do_usuario == '2':
        identifica_citacao = str(input('Digite o id da citação para excluí-la: '))
        cursor.execute('''
        SELECT * FROM citacoes
        WHERE id_citacao = ?
        ''', (identifica_citacao,))
        resultado = cursor.fetchone()
        if resultado is not None:
            try:
                cursor.execute('''
                DELETE FROM citacoes
                WHERE id_citacao = ?''', (identifica_citacao,))
                conexao.commit()
            except sqlite3.Error as causa:
                print(f'Não foi possível deletar: {causa}')
            else:
                print('Apagado com sucesso!')
        else:
            print('O ID não existe.')
    elif escolha_do_usuario == '3':
        identifica_citacao = str(input('Digite o id da citação para alterá-la: '))
        while True:
            cursor.execute('''SELECT * FROM citacoes
                           WHERE id_citacao = ?''', (identifica_citacao,))
            print('O que você quer alterar?\n'
                  '[1] - citação\n'
                  '[2] - autor')
            escolha_alteracao = str(input('Sua escolha: '))
            try:
                if escolha_alteracao == '1':
                    dados['citacao'] = str(input('Digite a nova citação: ')).strip()
                    cursor.execute('''
                           UPDATE citacoes
                           set citacao = ?
                           WHERE id_citacao = ?''', (dados['citacao'], identifica_citacao))
                elif escolha_alteracao == '2':
                    dados['autor'] = str(input('Digite o novo autor: '))
                    cursor.execute('''
                    UPDATE citacoes
                    SET autor = ?
                    WHERE id_citacao = ?''', (dados['autor'], identifica_citacao))
                else:
                    print('Opção inválida.')
                conexao.commit()
                print('Alteração efetuada com sucesso.')
            except:
                print('Não foi possível alterar')
            verif = str(input('Deseja fazer mais alguma alteração? [s/n]: ')).lower()
            verifica_loop(verif)
            if verif == 'n':
                break
    elif escolha_do_usuario == '4':
        cursor.execute('SELECT * FROM citacoes')
        resultado = cursor.fetchall()
        print('id da citação | citação | autor')
        simbolos = ['|', '|', '']
        for result in resultado:
            for r in range(0, 3):
                print(f'{result[r]}  ', end=f'{simbolos[r]}  ')
            print()
    elif escolha_do_usuario == '5':
        break
    else:
        print('Opção incorreta')

conexao.commit()
cursor.close()
conexao.close()
