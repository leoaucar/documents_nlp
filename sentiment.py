from matplotlib.pyplot import ylim
import pandas as pd
from textblob import TextBlob

df = pd.read_csv('base.csv')

sentiments = []
for i in df['lems']:
    sentence = TextBlob(str(i))
    sentiments.append(sentence.sentiment)

df_sentiments = pd.DataFrame(data = sentiments)
sentiments_df = pd.concat([df,df_sentiments], axis=1)
sentiments_df.to_csv("sentiment.csv")