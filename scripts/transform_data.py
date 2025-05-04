"""
Desenvolvendo o código:
Para aplicar as transformações, precisamos realizar a conexão com o MongoDB e com a base de dados e coleção específicas. No script extract_and_save_data.py, nós já temos funções que realizam esse processo. Sendo assim, para não termos que criar funções repetidas, podemos importar essas funções nesse novo script:

from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection

Para desenvolver as funções a seguir, você pode utilizar os códigos já feitos no notebook, adaptando-os para que se tornem funções, sendo elas:

1 - visualize_collection(col): imprime todos os documentos existentes na coleção.

2 - rename_column(col, col_name, new_name): renomeia uma coluna existente.

3 - select_category(col, category): seleciona documentos que correspondam a uma categoria específica.

4 - make_regex(col, regex): seleciona documentos que correspondam a uma expressão regular específica.

5 - create_dataframe(lista): cria um dataframe a partir de uma lista de documentos.

6 - format_date(df): formata a coluna de datas do dataframe para o formato "ano-mes-dia".

7 - save_csv(df, path): salva o dataframe como um arquivo CSV no caminho especificado.

Com as funções prontas, o próximo desafio é executá-las, realizando os seguintes passos:

conectar ao MongoDB;
ler os dados da coleção existente no banco de dados "db_produtos_desafio";
renomear as colunas "lat" para "Latitude" e "lon" para "Longitude;
selecionar os dados da categoria livros e salvá-los em csv;
filtrar os produtos vendidos a partir de 2021 e salvá-los em csv.
"""