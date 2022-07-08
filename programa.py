import PyPDF2
import pandas as pd


reports_text = pd.DataFrame()
documents_list = []

for document in documents_list:
    caminho = 'Relatorios_VW/2016.pdf'
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    while True:
        page = 0
        try:
            pageObj = pdfReader.getPage(page)
            page_text = pageObj.extractText()
        except:
            break
    pdfFileObj.close()


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