import pandas as pd

from clean_text import extract_page_text, parse_page_text

def create_table():
    columns = ["id","text","document","year","company","page",
    "pg_order","length","segment","topic","entities","sentiment"]
    documents_table = pd.DataFrame(columns = columns)

    return documents_table

def fill_table(documents_table,file_path):
    texts_list = []
    new_texts = []
    page = 0
    while True:
        try:
            page_text = extract_page_text(file_path,page)
            new_texts = parse_page_text(page_text)
            texts_list.append(new_texts)

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
    return documents_table

def concat_new_df(consolidated_documents_df, documents_df):
    consolidated_documents_df = consolidated_documents_df.concat(documents_df)
    return consolidated_documents_df
