import PyPDF2

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
    #quebrar em frases
    #ajustar em lista
    parsed_text_list = page_text #temporario para testar criador de tabela

    return parsed_text_list