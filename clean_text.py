from distutils.command.clean import clean
import PyPDF2
import re

#extrai dados do documento
def doc_length(file_path):
    caminho = file_path
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    doc_len = len(pdfReader.pages)
    pdfFileObj.close()
    return doc_len#,doc_name, doc_year, doc_company
    #mudar a funcao para extrair dados do documento

#extrai o texto bruto da página
def extract_page_text(file_path, page):
    caminho = file_path
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    page_text = pageObj.extractText()
    pdfFileObj.close()
    return page_text

#caso queiramos exportar o texto da pagina num txt separado
def export_page_txt(file_name, page_text):
    file1=open(str(file_name) + ".txt","w")
    file1.writelines(page_text)
    file1.close()

#trata o texto da página para ser uma lista de sentenças
def parse_page_text(page_text):
    parsed_text_list = []
    #quebra em frases
    pattern_split = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    splitted_sentences = re.split(pattern_split, page_text)
    for i in splitted_sentences:
        #trata cada sentença separadamente
        clean_sentence = i.replace("\n", " ")
        clean_sentence = re.sub(r'\s{2,}', " ", clean_sentence)
        clean_sentence = clean_sentence.strip()
        if clean_sentence != "":
            print(clean_sentence)
            parsed_text_list.append(clean_sentence) #temporario para testar criador de tabela

    return parsed_text_list

