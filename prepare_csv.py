from hashlib import new
from pydoc import doc
import pandas as pd
import re

from clean_text import extract_page_text, parse_page_text, doc_length


#cria uma tabela com as colunas corretas
def create_table():
    columns = ["id","text","document","year","company","page",
    "pg_order","length","segment","topic","entities","sentiment"]
    documents_table = pd.DataFrame(columns = columns)

    return documents_table

#adicionar os dados extraidos de uma pagina numa tabela
def fill_table(file_path):
    new_documents_table = create_table()
    texts_list = []
    new_texts = []

    #/home/leoaucar/Documents/documents_nlp/Relatorios_VW/2015.pdf
    
    m = re.search('Relatorios_(.*)', str(file_path))
    company_name = m.group(0)[11:-9]
    year = str(file_path[-8:-4])
    document_name = str(company_name) + " Annual report " + str(year)

#loop indo de página em página do relatório
    page = 0
    doc_len = doc_length(file_path)
    print("processando " + str(doc_len) + " páginas")
    while page < (doc_len-1):
        try:
            page_text = extract_page_text(file_path,page)
            new_texts = parse_page_text(page_text)
            for i in new_texts:
                #chamar aqui a correção do texto sobre i
                texts_list.append((i, page))

            #preencher colunas
            page = page + 1
            print('pagina ' + str(page) + " de "
            + str(doc_len) + " processada")
        except:
            print("erro página " + str(page))
            continue

#um loop adicionando linha a linha as colunas corretas
    id=0
    for i in texts_list:
        try:
            d = {'id':[id],'text':[i[0]], 'document':[document_name],
            'year':[year], 'company':[company_name],
            'page':[i[1]]}
            df_i = pd.DataFrame(data=d)
            new_documents_table = pd.concat([new_documents_table,df_i])
            id = id + 1
        except:
            print("erro id " + str(id))
            continue

    return new_documents_table

# concatena essa nova tabela a tabela principal
def concat_new_df(consolidated_documents_df, new_documents_table):
    consolidated_documents_df = pd.concat(
        [consolidated_documents_df,new_documents_table],
        ignore_index=True)
    return consolidated_documents_df

    #recebe comprimento
    #recebe segmento