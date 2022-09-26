import pandas as pd
import re
import spacy
from time import time
from collections import defaultdict 

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

df_base = pd.read_csv('./base.csv') #pode ser necesario eliminar linha 26024
df_textos = df_base.loc[:,"text"]

#print(df_textos.head(10))
#print(df_textos.tail(10))


#pré processamento com Spacy
nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser']) # disabling Named Entity Recognition for speed

def cleaning(doc):  
    # Lemmatizes and removes stopwords
    # doc needs to be a spacy Doc object
    txt = [token.lemma_ for token in doc if not token.is_stop]
    if len(txt) > 2:
        return ' '.join(txt)

#realiza a limpeza (préprocessamento) e tokeniza
brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in df_base['text'])

t = time()
txt = [cleaning(doc) for doc in nlp.pipe(brief_cleaning, batch_size=5000, n_process=-1)]
print('Time to clean up everything: {} mins'.format(round((time() - t) / 60, 2)))

df_clean = pd.DataFrame({'clean': txt})
df_clean = df_clean.dropna().drop_duplicates()
print(df_clean.shape)
print(df_clean.head(50))


#vamos juntar o novo DF limpo com o DF base para manter as outras coluans
df_final = pd.merge(df_clean, df_base, left_index=True, right_index=True)
print(df_final.shape)
print(df_final.tail())


#pegar etapas de NLP
 #pegar bigramas
 #implementar modelo word2vec

#nuvem de palavras
#analise de conteudo
#identificação de entidades
#analise de sentimentos