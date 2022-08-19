# README

## Objetivos, metodologia e casos de uso

### Metodologia
artigos sobre NLP

### Objetivo e usos
O sistema é desenhado em função de analisar relatórios anuais da industria automotiva. Ele visa permitir não só a extração de dados, mas assessorar pesquisadores da área através de analises textuais automatizadas. Isso se dará em quatro frentes:

* disponibilização dos dados para buscas rápidas
* análises de conteúdo simples/quantitativas
* análises não supervisionadas do conteúdo dos textos
* análises supervisionadas          ''   ''

### Casos de uso

## Desenho do sistema

### fluxo do sistema

### Desenho da base
cada prágrafo é uma entrada única na base
(um documento)

é seguida de :
id
texto (como vou separar títulos? e tabelas?)
documento/relatorio
ano
empresa
página
posição (de 1 a x - ordem que aparece na página)
"parte" da pagina
caracteres
sessao (posterior - semi manual)
tópicos (posterior - )
entidades (posterior - BERT)

### Scripts e funções

O Script programa.py executa as funções principais. Nos scripts auxiliares estão as definições de funções.

Em prepare_csv.py:

create_table()
cria um dataframe vazio com as colunas necessárias.
retorna o dataframe

fill_table(file_path) --> recebe um caminho de arquivo
cria e preenche o dataframe anteriormente a partir do texto contido no arquivo de file_path
retorna o dataframe preenchido

concat_new_df(consolidated_documents_df, new_documents_table) --> recebe a versao mais atual da base e concatena as novas infos
retorna a base atualizada