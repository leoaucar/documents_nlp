import pandas as pd



#identifica colunas com problemas e dropa elas
df = pd.read_csv('base.csv')

def nltk_cleaning(document_df):
    report_sentences = document_df['text']
    print(report_sentences.head())

    #steeming
    #stopwords
    #lemmetização
    #

    return document_df

new_df = nltk_cleaning(df)
new_df.to_csv('nltk_test')