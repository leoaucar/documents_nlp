import PyPDF2
import pandas as pd

caminho = 'Relatorios_VW/2020.pdf'
pdfFileObj = open(caminho, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(45)
page_text = pageObj.extractText()
pdfFileObj.close()

print(page_text)

file1=open("teste2020.txt","w")
file1.writelines(page_text)