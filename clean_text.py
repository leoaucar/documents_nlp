import PyPDF2
import pandas as pd

def extract_page_text(file_path, page):
    caminho = file_path
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    page_text = pageObj.extractText()
    pdfFileObj.close()
    return page_text

def export_page_txt(file_name, page_text):
    file1=open(str(file_name) + ".txt","w")
    file1.writelines(page_text)
    file1.close()

def parse_page_text(page_text):
    parsed_text_list = []
    #quebrar em frases
    #ajustar em lista
    
    return parsed_text_list