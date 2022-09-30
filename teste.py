import pandas as pd



#identifica colunas com problemas e dropa elas
df = pd.read_csv('base.csv')

def nltk_cleaning(document_df):
    report_sentences = document_df['text']
    print(report_sentences.head())
    return document_df

nltk_cleaning(df)