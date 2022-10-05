<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Raspagem de relatórios da indústria automotiva para projeto de NLP

#### Aluno: [Nome Sobrenome](https://github.com/link_do_github)
#### Orientadora: [Nome Sobrenome](https://github.com/link_do_github)

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

<!-- para os links a seguir, caso os arquivos estejam no mesmo repositório que este README, não há necessidade de incluir o link completo: basta incluir o nome do arquivo, com extensão, que o GitHub completa o link corretamente -->
- [Link para o código](https://github.com/link_do_repositorio). <!-- caso não aplicável, remover esta linha -->

---

### Resumo

O sistema é desenhado em função de analisar relatórios anuais da industria automotiva. Ele visa permitir não só a extração de dados, mas assessorar pesquisadores da área através de analises textuais automatizadas. Para isso ele realiza a raspagem de todo o texto dos relatórios e separa em sentenças. Posteriormente é feita a limpeza dessas sentenças com metadados apropriados. Após isso, é feito seu pré-processamento, resultando em duas versões das sentenças: lemmetizadas e não lemmetizadas com pos-tag. Foi então, a título de prova de conceito, realizada a análise de sentimentos dessas sentenças com base na biblioteca TextBlob. Pode-se resumir os objetivos do projeto:

* Produção de um banco de dados a partir dos conteúdos textuais de relatórios da indústria automotiva
* Fornecer insumos para análises de conteúdo simples/quantitativas
* Fornecer insumos para análises supervisionadas e não supervisionadas via processamento de linguagem natural

### Abstract

The system was designed with the purpose of analysing annual reports from the automotive industry. It aims to not only extract the textual data from the reports, but to make it available to other reasearchers and simplify the process of text analysis. With this in mind, it scraps all the text from annual reports and segment them as sentences with apropriate metadata. After, this sentences go through a cleaning processes and are pre-processed, resulting in two versios of the raw data: a lemmetized version and a non-lemmetized but pos-tagged version. As a proof of concept we ran a sentiment analysis of the sentences through the library textBlob. We can summarize the objectives of the project as the following:

* Creation of a automotive industry annual reports text database
* to supply data for content analysis
* to supply data for supervises and non-supervised natural language processing analysis


### 1. Introdução

#### 1.1 Metodologia

O trabalho se insere simultaneamente no campo da sociologia econômica e das ciências da computação. Dessa maneira, propõe utilização de metodologias de localização e obtenção de dados (fonte) e também de processamento de linguagem natural comuns a ciência da computação (livro NLP) para produção de análises sociológicas. Se alinha portanto a uma perspectiva estrutural e de rede, que vê documentos corporativos enquanto artefatos que podem ser mobilizados como proxy do comportamento organizacional e portanto, que podem ser analisados enquanto proxy para compreensão do vocabulário de motivos (fonte Mills) e quadro moral (fonte) da ação organizacional. A ênfase em documentos enquanto artefatos, para além sua consideração enquanto artefatos etnográficos, que se incluem na tradição da antropologia dos documentos e burocracia (fonte lowkron, fonte hull), também dialoga com a compreensão das organizações econômicas enquanto redes sociomateriais (fonte latour), onde os documentos fazem extamente o papel de agregação de associações capazes de colocar a organização em movimento.

Metodologicamente o trabalho se ampara no uso de técnicas de processamento de linguagem natural pela sociologia como exemplificado em FONTE(ano). Em particular, FONTE(ano) já demonstram como é possível utilizar grandes volumes de texto para analisar as mudanças de sentimento e relação entre termos e categorias sociológicas, como gênero, classe e raça. Já FONTE(ano) demonstram a utilização de técnicas de modelagem de tópico no campo da análise cultural. A proposta aqui é produzir um insumo - a base de dados - a ser futuramente utilizadas em estudos aprofundados sobre a temática das estratégias corporativas na indústria automotiva. Fundamentalmente o trabalho propiciará análises de caráter comparativo institucional e histórico (fonte), na medida que se observará como determinadas categorias evoluem e se transformam no tempo em instituições - no caso empresas ou setores de empresas - distintas.

#### 1.2 Casos de uso
Para elaboração, foram considerados alguns casos de uso e usuários típicos.
1) o próprio autor do trabalho - a base de dados produzida será utilizada como parte da tese de doutorado do autor deste trabalho. Dessa maneira, espera-se que ela agilize processos de analise futuros e também permita gradativametne a inclusão de mais relatórios como fonte de dados.
2) colegas de grupo de pesquisa - a base será disponibilizada para colegas de pesquisa juntamente com os scripts python. Espera-se com isso que esses colegas, assumindo certa familiaridade com a linguagem, sejam capazes de reproduzir o sistema para relatórios de empresas de outros ramos, melhorar os tratamentos de texto e acrescentar novas formas de análise desse conteúdo. A disponibilização dos textos brutos com adequada identificação de página e relatório também se propõe a facilitar análises de pesquisadores que busquem ter abordagens qualitativas ou de análise de conteúdo tradicional.
3) demais colegas da comunidade científica - por fim, a disponibilização da base de dados em si propõe-se a facilitar a investigação de quaisquer outros pesquisadores sobre a indústria automotiva. Para além dos dados disponibilizados nessa versão, espera-se com auxílio de colegas produzir um grande banco de dados referente a indústria automotiva que sirva de pontapé inicial para mais pesquisas sobre o setor, especialmente no campo da sociologia econômica.


### 2. Modelagem

#### Desenho do sistema
<p>O principal elemento do sistema será a base de dados. Assim, todo o primeiro conjunto de scripts diz respeito a produção dessa base. A partir dessa base serão utilizados scripts adicionais para análise desses dados. assim, o fluxo pode ser descrito como:</p>

* Preparação de data frame via pandas que servirá de base
* Extração do texto bruto dos relatórios via pyPDF2
* limpeza básica das sentenças uma a uma
* Inserção das sentenças como linhas do dataframe com ids únicos
* Inserção de metadados referentes a cada sentença: documento de origem, empresa, ano
* Realiza primeiro salvamento da base em csv
* pré-processamento dos textos
* análise de sentimento das sentenças como prova de conceito

A seguir, serão descritas brevemente essas etapas a partir da descrição dos scripts utilizados.

#### Scripts e funções
<p>as funções para realização das operações estão divididas em scripts principais divididos em 2 grupos: preparação da base de dados e análise dos dados coletados</p>

##### program.py - Execução do programa
O script principal, acessa os demais scripts para execução. Inicialmente faz uma leitura do diretório buscando identificar a existência da base, caso não cria uma. Em seguida faz a listagem de todos os relatórios dentro da pasta para serem processados.

''' python
for i in list:
    print(i)
'''

Em seguida passa esses relatórios um a um via par ao script prepare_csv.py que realizará a preparação de cada relatório.

''' python
for i in list:
    print(i)
'''

Após esses relatórios prontos, chama os scripts para pré-processamento do texto inclusos em NLTK_preprocessing.py e salva uma vez mais a base.

''' python
for i in list:
    print(i)
'''

##### prepare_csv.py - Preparação das tabelas
Recebe os relatórios um a um e executa a preparação das tabelas com alocação de metadados baseados nos documentos. Primeira parte é a preparação de um data frame para o relatório a ser processado e identificação dos metadados.

'''
for i in list:
    print(i)
'''

Para processamento do texto em si, são utilizadas duas funções do script clean_text.py e também é identificada a página da qual cada texto é retirado.
''' python
for i in list:
    print(i)
'''

Por fim, a gravação dos metadados no dataframe é feita com o seguinte trecho
''' python
for i in list:
    print(i)
'''

##### clean_text.py - limpeza inicial do texto e segmentação em sentenças
especificamente trata os textos extraídos, separando em sentenças. É importante notar que, na extração de texto bruto, as sentenças frequentemente eram separadas por quebras de linha ('/n'). Em função disso, optou-se pela separação do texto em sentenças e não parágrafos. A seguinte função realiza a extração bruta do texto

'''
def extract_page_text(file_path, page):
    caminho = file_path
    pdfFileObj = open(caminho, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    page_text = pageObj.extractText()
    pdfFileObj.close()
    return page_text
'''

Ja o trecho a seguir realiza a separação do texto de cada página em sentenças e realiza a limpeza de caractéres básica. Como forma de separação de sentenças usou-se a seguinte expressão regular: r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

'''
#trata o texto da página para ser uma lista de sentenças
def parse_page_text(page_text):
    parsed_text_list = []
    #quebra em frases
    pattern_split = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s" #considerar tamanho máximo de sentenças
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
'''

##### nltk_preprocessing.py - Pré processamento do texto bruto
realiza pré processamento de todo o texto bruto para a NLP e armazena numa coluna que será acessada pelas outras análises de NLP

##### sentiment.py
Como prova de conceito

#### A base de dados
<p>A base é constituída a partir de relatórios anuais com informações de empresas da indústria automotiva. A ênfase é nos <i>conteúdos textuais</i> dos relatórios, deixando-se em segundo plano tabelas e dados financeiros.</p>
<p>Cada relatório é "raspado" com auxílio da biblioteca PyPDF2. O texto é extraído por página e depois separado em sentenças a partir do uso de expressões regulares. Algumas informações referentes a cada sentênça sao armazenadas em colunas adicionais. Essas colunas são: </p>

* id --> identificador único daquela sentença na base
* text --> texto bruto extraído da sentença
* document --> documento daonde foi extraída a sentença
* year --> o ano ao qual se refere o documento
* company --> empresa a qual se refere o documento
* page --> a página do relatório onde aquela sentença está localizada

Em seguida, como descrito a cima foram préprocessados os textos brutos, resultando em duas novas colunas:

* lems --> versão das sentenças já limpeza de stopwords, steeming e lemmetização
* tags --> versão das sentenças com palavras sem steeming ou lemetização e com pos-tag

Todas as colunas acima foram agregadas na base base.csv.

Por fim, a prova de conceito de análise de sentimetno resultou em:
* polarity --> identificação do grau de positividade ou negatividade da sentença
* subjectivity --> identificação do grau em que a sentença é considerada uma opinião subjetiva
Essas colunas foram salvas apenas numa versão da base entitulada "sentiments.csv"

Futuramente propõe-se que serão adicionadas outros metadados sobre as sentenças:
* words --> dicionário de contagem de palavras únicas na sentença
* segment --> o trecho/seção do relatório ao qual a sentença pertence
* topic --> classificação daquela sentença em tópico a partir de seu conteúdo
* entities --> dicionário com as entidadaes identificadas na sentença

<p>A proposição é que a base possa servir para agregações e análises tentao produzidas a partir de classificações não supervisionadas (tópicos, entidades), nativos/humanos (segmentos do relatório) ou classificações supervisionadas (sentimento).Essa abordagem permitira análises quantitativas e qualitativas do conteúdo dos relatórios, além de uma observação de transformações no tempo dos conteúdos presentes no texto e de sua associação a determinadas classificações nativas das organizações (ex. perceber ao longo do tempo que as sentenças relativas ao marketing se tornam mais frequentes e mais positivas, ao passo que sentenças relativas a recursos humanos passam a ser mais raras).</p>


### 3. Resultados

Como resultado inicial da análise de 9 relatórios obteve-se uma base de dados de XX000 mil sentenças. Essas sentenças encontram-se já pré-processadas em versões com lemmetização e pos-tag. Adicionalmente, a fim de prova de conceito, utilizou-se os dados coletados jutnamente com a biblioteca textBlob para realizar uma análise de sentimento. Como prova de conceito do uso dos metadados dos relatórios, apresenta-se abaixo a evolução da polaridade das sentenças por ano.

IMAGEM

Assim, espera-se que, com o crescimetno da base via inserção de relatórios de utros anos e empresas, e complementação dos metadados (seja manualmente, automaticamente via técnicas supervisionadas ou não supervisionadas) seja possível realizar agregações e comparações do conteúdo textual - e seus significados - ao longo do tempo e também entre categorias distintas (por exemplo, observar a mudança do sentimento médio das sentenças em empresas distintas ou em seções distintas dos documentos).

### 4. Conclusões

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

---

Matrícula: 123.456.789

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
