import pandas as pd

#ler base
#basear na coluna página

#formatar uma lista de topicos para cada relatório e aplicar retroativamente
report_1 = {'topic 1':(40,50),
            'topic 2': (51,60)}
report_list = [report_1]

#for i in report_list:
#    #print(i.keys)
#    for key, value in i.items():
#        print(key, value[0], value[1])

df_base = pd.read_csv('./baseTeste.csv')
row = 0

#loop pela coluna páginas
#checar se valor esta no dicionário
#substituir por chave