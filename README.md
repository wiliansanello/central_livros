# Sistema de Gestão de Biblioteca

O projeto de gestão de biblioteca permite: 
- Atualizar e gerenciar o acervo de uma biblioteca, cadastrando, alterando ou removendo registro de um livro.
- Atualizar o registro de alunos, cadastrando, alterando ou removendo o registro de um aluno. Também é possível importar um arquivo no formato JSON com os registros dos alunos.
- Registrar entradas e saídas, monitorando atrasos e calculando multas proporcionais ao tempo deles.

## Ferramentas utilizadas
**Flask**: Framework para servidor web leve e aderente a projetos pequenos, mas que permite escalabilidade.
**SQLAlchemy**: ORM usada em Python para a conversão de classes em entidades e realização de transações SQL.
**SQLite**: Banco de dados com integração nativa com o Python, simples e adequado para pequenos projetos.
