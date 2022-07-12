import PyPDF2
import pandas as pd

from prepare_csv import concat_new_df, create_table, fill_table

try:
    documents_df = pd.read_csv("base.csv")
except:
    documents_df = create_table()
    documents_df.to_csv("base.csv")

documents_list = []
for document in documents_list:
    new_documents_table = create_table()
    new_table = fill_table(new_documents_table, document)
    documents_df = concat_new_df(documents_df, new_table)
documents_df.to_csv('base.csv')

#loop for vai passar relatório por relatório
#em cada relatório vai tentar extrair todas as páginas
#vai adicionar linhas num grande DF (abaixo colunas)
#ao fim exportaremos o CSV

#id
#texto (como vou separar títulos? e tabelas?)
#documento/relatorio
#ano
#empresa
#página
#posição (de 1 a x - ordem que aparece na página)
#"parte" da pagina
#caracteres
#sessao (posterior - semi manual)
#tópicos (posterior - )
#entidades (posterior - BERT)
#sentimento (manual?)
#departamento ? (manual) --> análise qualitativa

#vou precisar dps:
#um randomizador de parágrafos que me permita tagear as coisas
#posibilitando dps uma classificação
#talvez exportar para o qual coder para buscar categorias?

#como vou controlar quais termos foram extraidos?
#" " " " foram anotados?
#como inserir colunas a partir das anotações do qualcoder?
#provavelmente SQLITE