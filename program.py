import pandas as pd
import os

from prepare_csv import concat_new_df, create_table, fill_table
from NLTK_preprocessing import nltk_cleaning


#prepara um CSV base caso não haja algum
try:
    documents_df = pd.read_csv("base.csv") #le o documento consolidado
except:
    documents_df = create_table() #caso nao exista, cria esse doc
    documents_df.to_csv("base.csv", index=False)


# identifica o diretorio e lista os documentos a serem lidos
dir_path = r'./Relatorios_Volkswagen'
documents_list = [] #pegar lista de documentos

for path in os.listdir(dir_path):
    # garante que é um arquivo
    if os.path.isfile(os.path.join(dir_path, path)):
        documents_list.append(path)
print("Documentos processados: " + 
    str(documents_list))


#concatena DF com textos
for document in documents_list:
    new_documents_table = fill_table("./Relatorios_Volkswagen/" + document)
    documents_df = concat_new_df(documents_df, new_documents_table)


#salva base processada num CSV
documents_df.to_csv('base.csv', escapechar="|", index=False)

#recarrega a base completa e aplica pre processamento
df = pd.read_csv('base.csv')
new_df = nltk_cleaning(df)
new_df.to_csv('base.csv')