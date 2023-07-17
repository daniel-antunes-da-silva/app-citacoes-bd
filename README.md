-- Atualização do código 17/07/2023 -- 

Esse é um projeto de um app que guarda citações, autor e id da citação em um banco de dados sqlite3, onde é possível 
adicionar nova citação, remover citação existente, alterar uma citação ou autor, ou exibir todas as citações. 

Nessa versão, o sistema foi renomeado para "gerenciando_citacoes", e foi arrumado o erro em que o id da citação não era
atualizado de acordo com a remoção ou adição de novas citações. 

Nessa versão, foi adicionada um novo arquivo "app_citacoes.py", onde é gerada uma tela e exibida uma citação aleatória,
de acordo com o id (aleatorizada com randint da biblioteca random). O usuário pode optar por gerar uma nova citação,
e a configuração das labels são alteradas para exibir a nova citação.