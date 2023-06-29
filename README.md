Esse é um projeto de um app que guarda citações em um banco de dados.
Nessa versão, é possível apenas inserir os dados no bd, onde o id é gerado automaticamente de acordo com o número de citações já existentes.
A citação e o autor são inseridos manualmente, através de inputs.

Nas próximas versões, será possível editar ou excluir dados do bd.

-- Atualização de código 29/06/2023 -- 

Nessa versão, está se tornando um sisteminha mais completo, onde possui menus, e é possível alterar citações ou 
autores, bem como excluir citações inteiras (ou seja, excluir o registro da citação), entre outras funcionalidades 
que foram implementadas, e alguns tratamentos de erro.

No entanto, ainda não foi adicionada uma atualização dos ids automaticamente, quando uma citação é excluida. Ou seja,
os ids ficam em inconformidade com o número de linhas. Isso gerou um bug na funcionalidade de adicionar nova citação,
e será resolvido em um próximo momento.