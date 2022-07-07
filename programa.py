import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('Relatorios_VW/2016.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.getPage(99) 
    
# extracting text from page 
print(pageObj.extractText()) 
    
# closing the pdf file object 
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