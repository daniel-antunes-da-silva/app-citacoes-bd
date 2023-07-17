# Gera uma citação aleatória através das citações cadastradas no banco de dados.(randint de acordo com o id)
# e exibe em uma tela do tkinter.
# Quando o botão "Nova citação" é pressionado, é gerado uma nova citação e exibida na tela através da config (Label).

from tkinter import *
from funções_utilizadas import gerar_citacao


def gerar_nova_citacao():
    nova_citacao = gerar_citacao()
    lbl_citacao.config(text=f'"{nova_citacao[0]}"')
    lbl_autor.config(text=f'- {nova_citacao[1]}')


janela = Tk()
janela.title('App citação')
janela.geometry('800x250+300+280')
citacao_e_autor = gerar_citacao()
# print(citacao_e_autor[0] + ' -> ' + citacao_e_autor[1])
lbl_citacao = Label(janela, text=f'"{citacao_e_autor[0]}"', font=('Arial', 11))
lbl_citacao.pack(padx=20, pady=30)
lbl_autor = Label(janela, text=f'- {citacao_e_autor[1]}', font=('Arial', 10))
lbl_autor.pack(padx=10, pady=10)
btn_nova_citacao = Button(janela, text='Nova citação', command=gerar_nova_citacao)
btn_nova_citacao.pack()
janela.mainloop()
