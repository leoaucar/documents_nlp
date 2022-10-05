# carrega bibliotecas necessárias
import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk import stem
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')
from nltk.corpus import stopwords

from collections import Counter

stopwords = stopwords.words('english')


def nltk_cleaning(document_df):


    report_sentences = document_df['text'].copy()

    df_lems= pd.DataFrame()
    df_tags = pd.DataFrame()

    lems_list = []
    tags_list = []

    for sent in report_sentences:
        #tokenização e deixar em minúsculas
        lower_words = [word.lower() for word in word_tokenize(sent)]
        
        #tratamentos de texto
        clean_words = (re.sub("[^A-Za-z']+", ' ', str(word)).lower() for word in lower_words)
        clean_words = (word for word in clean_words if len(word) > 1)


        #remover stopwords
        clean_words = [word for word in clean_words if word not in stopwords]
        
        #Stemming
        stemmer = stem.PorterStemmer()
        stem_words = [stemmer.stem(word) for word in clean_words]
        
        #lemmatização
        lemmetizer = WordNetLemmatizer()
        palavras_lem = [lemmetizer.lemmatize(word) for word in stem_words]
        lems_list.append(palavras_lem)
        
        #taggind das palavras
        tags = [nltk.pos_tag([word]) for word in clean_words]
        tags_list.append(tags)
        

    print(lems_list)
    print(tags_list)
    df_lems = pd.concat([df_lems,pd.Series(lems_list)])
    df_tags = pd.concat([df_tags,pd.Series(tags_list)])
    document_df = pd.concat([document_df,df_lems,df_tags], axis=1)

    #print(palavras_lem)
    print(df_lems.shape)
    print(df_tags.shape)
    print(document_df.shape)
    document_df = document_df.rename(columns={document_df.columns[-2]:'lems'})
    document_df = document_df.rename(columns={document_df.columns[-1]:'tags'})
    return document_df
