import pandas as pd
import os

from prepare_csv import concat_new_df, create_table, fill_table


#prepara um CSV base caso não haja algum
try:
    documents_df = pd.read_csv("base.csv") #le o documento consolidado
except:
    documents_df = create_table() #caso nao exista, cria esse doc
    documents_df.to_csv("base.csv", index=False)


# identifica o diretorio e lista os documentos a serem lidos
dir_path = r'./Relatorios_VW'
documents_list = [] #pegar lista de documentos

for path in os.listdir(dir_path):
    # garante que é um arquivo
    if os.path.isfile(os.path.join(dir_path, path)):
        documents_list.append(path)
print(documents_list)

#concatena DF com textos
for document in documents_list:
    new_documents_table = fill_table("./Relatorios_VW/" + document)
    documents_df = concat_new_df(documents_df, new_documents_table)
documents_df.to_csv('base.csv', index=False)





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