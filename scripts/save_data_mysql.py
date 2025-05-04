"""
Desenvolvendo o código:
Para desenvolver as funções a seguir, você pode utilizar os códigos já feitos no notebook, adaptando-os para que se tornem funções, sendo elas:

1 - connect_mysql(host_name, user_name, pw): estabelece a conexão com o servidor MySQL, utilizando os dados do host, usuário e senha. A função deve retornar a conexão estabelecida.

2 - create_cursor(cnx): cria e retorna um cursor, que serve para conseguirmos executar os comandos SQL, utilizando a conexão fornecida como argumento.

3 - create_database(cursor, db_name): cria um banco de dados com o nome fornecido como argumento. Para isso, a função deverá usar o cursor para executar o comando SQL de criação do banco de dados.

4 - show_databases(cursor): exibe todos os bancos de dados existentes. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todos os bancos de dados existentes.

5 - create_product_table(cursor, db_name, tb_name): cria uma tabela com o nome fornecido no banco de dados especificado. A tabela deve ter as colunas que correspondam aos dados que serão inseridos posteriormente.

6 - show_tables(cursor, db_name): lista todas as tabelas existentes no banco de dados especificado. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todas as tabelas no banco de dados.

7 - read_csv(path): lê um arquivo csv do caminho fornecido e retorna um DataFrame do pandas com esses dados.

8 - add_product_data(cnx, cursor, df, db_name, tb_name): insere os dados do DataFrame fornecido à tabela especificada no banco de dados especificado. A função deve usar o cursor para executar o comando SQL de inserção de dados.

Com as funções prontas, o próximo desafio é executá-las, realizando os seguintes passos:

conectar ao servidor MySQL;
criar um cursor;
criar um banco de dados chamado "db_produtos_teste";
exibir todos os bancos de dados existentes;
criar uma tabela chamada "tb_livros" no banco de dados criado;
exibir todas as tabelas no banco de dados criado;
ler os dados do arquivo csv "tb_livros.csv";
adicionar os dados lidos à tabela criada.
"""