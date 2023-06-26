import sqlite3
from funções_utilizadas import verifica_loop, mensagem_enfeitada


#lista_de_dados = []
dados = {}
mensagem_enfeitada('Bem-vindo(a) ao sistema de cadastro de citações')

conexao = sqlite3.connect('citações.db')
cursor = conexao.cursor()
# cursor.execute('SELECT * FROM citacoes')
#resultado = cursor.fetchall()
contador = 1
while True:
    cursor.execute('SELECT * FROM citacoes')
    resultado = cursor.fetchall()
    print(resultado)
    if not resultado:
        dados['id_citacao'] = 1
    else:
        dados['id_citacao'] = len(resultado) + 1
    dados['citacao'] = str(input('Digite a citação: ')).strip()
    dados['autor'] = str(input('Nome do autor (caso não tenha, deixe em branco): ')).title().strip()
    if dados['autor'] == '':
        dados['autor'] = 'autor desconhecido'
    print(dados)
    confirmacao = str(input('Confirmar inserção no banco de dados? [s/n]')).lower()
    verifica_loop(confirmacao)
    if confirmacao != 'n':
        cursor.execute('''
            INSERT INTO citacoes(id_citacao, citacao, autor)
            values(:id_citacao, :citacao, :autor)
            ''', dados)
        print('Citação inserida com sucesso!')
    else:
        pass
    #lista_de_dados.append(dados)
    verif = str(input('Quer continuar? [s/n]')).lower()
    verifica_loop(verif)
    if verif == 'n':
        break
    '''
    if verif == 'n':
        break
    elif verif != 's':
        while verif != 's':
            print('Ops, opção incorreta!')
            verif = str(input('Quer continuar? [s/n]')).lower()'''



conexao.commit()
cursor.close()
conexao.close()
