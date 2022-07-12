import PyPDF2
import pandas as pd


reports_text = pd.DataFrame()
documents_list = []

columns = ["id","text","document","year","company","page",
"pg_order","length","segment","topic","entities","sentiment"]
documents_df = pd.DataFrame(columns = columns)

#ler os para pegar diretorio

documents_list = ["a"]
for document in documents_list:
    caminho = 'Relatorios_VW/2016.pdf'
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    page = 49
    while page < 50:
        try:
            df_temp = pd.DataFrame(columns = columns)

            pageObj = pdfReader.getPage(page)
            page_text = pageObj.extractText()
            print(page_text)
            #quebrar texto em paragrafos e dps...
            df_temp.loc[0,['text']] = str(page_text)
            #passar documento (VW2016, ST2005 etc...)
            #passar ano
            #empresa
            #pagina
            #ordem
            #comprimento
            #documents_df.concat(df_temp)
            page = page + 1

        except:
            break
    pdfFileObj.close()
    df_temp.to_csv('TESTE.csv')

    #documents_df.to_csv('teste.csv')

#loop for vai passar relatório por relatório
#em cada relatório vai tentar extrair todas as páginas
#vai adicionar linhas num grande DF (abaixo colunas)
#ao fim exportaremos o CSV

#id
#texto (como vou separar títulos? e tabelas?)
#documento/relatorio
#ano
#empresa
#página
#posição (de 1 a x - ordem que aparece na página)
#"parte" da pagina
#caracteres
#sessao (posterior - semi manual)
#tópicos (posterior - )
#entidades (posterior - BERT)
#sentimento (manual?)
#departamento ? (manual) --> análise qualitativa

#vou precisar dps:
#um randomizador de parágrafos que me permita tagear as coisas
#posibilitando dps uma classificação
#talvez exportar para o qual coder para buscar categorias?

#como vou controlar quais termos foram extraidos?
#" " " " foram anotados?
#como inserir colunas a partir das anotações do qualcoder?
#provavelmente SQLITE