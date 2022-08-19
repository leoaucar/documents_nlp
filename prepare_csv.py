from hashlib import new
import pandas as pd

from clean_text import extract_page_text, parse_page_text

def create_table():
    columns = ["id","text","document","year","company","page",
    "pg_order","length","segment","topic","entities","sentiment"]
    documents_table = pd.DataFrame(columns = columns)

    return documents_table

def fill_table(file_path):
    new_documents_table = create_table()
    texts_list = []
    new_texts = []
    page = 55
    while page < 57:
        try:
            page_text = extract_page_text(file_path,page)
            new_texts = parse_page_text(page_text)
            texts_list.append(new_texts)
            #print(texts_list) #--> texta se esta pegando texto
            #preencher colunas
            page = page + 1

        except:
            break
    #recebe id
    #recebe texto
    #recebe nome do documento
    #recebe ano
    #recebe empresa
    #recebe página
    #recebe lugar
    #recebe comprimento
    #recebe segmento
    id=0
    for i in texts_list:
        d = {'id':[id],'text':[i]}
        df_i = pd.DataFrame(data=d)
        new_documents_table = pd.concat([new_documents_table,df_i])
        print(new_documents_table.iloc[[0]])
        id = id + 1
    
    for i in new_documents_table['text']:
        print(i)
    return new_documents_table

def concat_new_df(consolidated_documents_df, new_documents_table):
    consolidated_documents_df = pd.concat([consolidated_documents_df, new_documents_table], ignore_index=True)
    return consolidated_documents_df
