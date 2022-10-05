import pandas as pd

df = pd.read_csv('sentiment.csv')
df = df[['year','polarity']]

groups = df.groupby(by='year').mean()
print(groups.head(9))