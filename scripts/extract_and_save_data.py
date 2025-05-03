"""
Até o momento temos desenvolvido nosso pipeline em um notebook Jupyter, que oferece um ambiente interativo e prático para o aprendizado e experimentação de novos conceitos e métodos. Agora, temos um novo desafio!

Nosso objetivo é ter um pipeline de dados eficiente e automatizado. Portanto, para nos aproximarmos ainda mais dessa realidade, nosso próximo desafio é transformar o código que desenvolvemos até agora no nosso notebook em um script Python estruturado em funções.

Essa abordagem traz vantagens como: facilidade de teste, reutilização de código, manutenção mais simples e automação do pipeline. Sem contar que, em um ambiente de produção, geralmente são utilizados scripts ao invés de notebooks. Então, bora desenvolver e praticar essa habilidade?

Orientações para o desafio
Preparando o ambiente:
crie uma subpasta chamada scripts na sua pasta de trabalho;
na pasta scripts crie um arquivo chamado "extract_and_save_data.py".
Desenvolvendo o código:
Para desenvolver as funções a seguir, você pode utilizar os códigos já feitos no notebook, adaptando-os para que se tornem funções, sendo elas:

1 - connect_mongo(uri): estabelece a conexão com a instância do MongoDB usando a URI fornecida. Ela retorna o cliente do MongoDB que permite interagir com o banco de dados.

2 - create_connect_db(client, db_name): utiliza o(a) cliente do MongoDB para criar (se não existir) e conectar-se ao banco de dados especificado pelo parâmetro db_name. Ela retorna o objeto de banco de dados que pode ser usado para interagir com as coleções dentro dele.

3 - create_connect_collection(db, col_name): cria (se não existir) e conecta-se à coleção especificada pelo parâmetro col_name dentro do banco de dados fornecido. Ela retorna o objeto de coleção que pode ser usado para interagir com os documentos dentro dela.

4 - extract_api_data(url): extrai dados de uma API na URL fornecida e retorna os dados extraídos no formato JSON.

5 - insert_data(col, data): recebe uma coleção e os dados que serão inseridos nela. Ela deve adicionar todos os documentos à coleção e retornar a quantidade de documentos inseridos.

Com as funções prontas, o próximo desafio é executá-las, realizando os seguintes passos:

criar um novo banco de dados;
criar uma coleção;
extrair os dados da API: https://labdados.com/produtos;
inserir os dados da API na coleção criada.
"""