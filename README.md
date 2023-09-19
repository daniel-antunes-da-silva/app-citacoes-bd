-- Atualização do código 17/07/2023 -- 

Esse é um projeto de um app que guarda citações, autor e id da citação em um banco de dados sqlite3, onde é possível 
adicionar nova citação, remover citação existente, alterar uma citação ou autor, ou exibir todas as citações. 

Nessa versão, o sistema foi renomeado para "gerenciando_citacoes", e foi arrumado o erro em que o id da citação não era
atualizado de acordo com a remoção ou adição de novas citações. 

Nessa versão, foi adicionada um novo arquivo "app_citacoes.py", onde é gerada uma tela e exibida uma citação aleatória,
de acordo com o id (aleatorizada com randint da biblioteca random). O usuário pode optar por gerar uma nova citação,
e a configuração das labels são alteradas para exibir a nova citação.

# Exibição de tela simples com citação randomizada:

![Tela citacao](https://github.com/daniel-antunes-da-silva/app-citacoes-bd/assets/132831685/2c1051a6-4d3f-4fa7-a8f3-5a2ca4d7ab92)


# Sistema de gerenciamento de citações | Menu de opções:


![Menu de opcoes](https://github.com/daniel-antunes-da-silva/app-citacoes-bd/assets/132831685/ecdcfaba-57ca-45f0-87d9-bf34cfd677c5)

Exibindo citações (com autores) já cadastradas:

![Exibindo citacoes cadastradas no bd](https://github.com/daniel-antunes-da-silva/app-citacoes-bd/assets/132831685/7ef7f6c9-052f-4c5b-b601-cb00cb60245b)

Para novas citações adicionadas, o ID é incrementado automaticamente.
