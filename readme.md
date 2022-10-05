<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Raspagem de relatórios da indústria automotiva para projeto de NLP

#### Aluno: [Nome Sobrenome](https://github.com/link_do_github)
#### Orientadora: [Nome Sobrenome](https://github.com/link_do_github) e [Nome Sobrenome](https://github.com/link_do_github).
#### Co-orientador(/a/es/as): [Nome Sobrenome](https://github.com/link_do_github) e [Nome Sobrenome](https://github.com/link_do_github). <!-- caso não aplicável, remover esta linha -->

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

<!-- para os links a seguir, caso os arquivos estejam no mesmo repositório que este README, não há necessidade de incluir o link completo: basta incluir o nome do arquivo, com extensão, que o GitHub completa o link corretamente -->
- [Link para o código](https://github.com/link_do_repositorio). <!-- caso não aplicável, remover esta linha -->

- [Link para a monografia](https://link_da_monografia.com). <!-- caso não aplicável, remover esta linha -->

- Trabalhos relacionados: <!-- caso não aplicável, remover estas linhas -->
    - [Nome do Trabalho 1](https://link_do_trabalho.com).
    - [Nome do Trabalho 2](https://link_do_trabalho.com).

---

### Resumo

<!-- trocar o texto abaixo pelo resumo do trabalho, em português -->

O sistema é desenhado em função de analisar relatórios anuais da industria automotiva. Ele visa permitir não só a extração de dados, mas assessorar pesquisadores da área através de analises textuais automatizadas. Isso se dará em quatro frentes:

* Produção de um banco de dados a partir dos conteúdos textuais de relatórios da indústria automotiva
* análises de conteúdo simples/quantitativas
* análises não supervisionadas do conteúdo dos textos
* análises supervisionadas          ''   ''
* disponibilização do banco de dados e análises para outros pesquisadores


### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

<!-- trocar o texto abaixo pelo resumo do trabalho, em inglês -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

Donec molestie, ante quis tempus consequat, mauris ante fringilla elit, euismod hendrerit leo erat et felis. Mauris faucibus odio est, non sagittis urna maximus ut. Suspendisse blandit ligula pellentesque tincidunt malesuada. Sed at ornare ligula, et aliquam dui. Cras a lectus id turpis accumsan pellentesque ut eget metus. Pellentesque rhoncus pellentesque est et viverra. Pellentesque non risus velit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### 1. Introdução

O trabalho 

#### 1.1 Metodologia
<p>O trabalho se baseaia em três grandes campos de produção de conhecimento nas ciências sociais contemporâneas. O primeiro diz respeito aos impactos da grande disponibilidade de dados na pesquisa sociológica (fonte), particularmente as discussões metodológicas sobre as formas apropriadas de se utilizar esses dados para produção de teoria (fonte).</p>
<p>O segundo diz respeito as discussões sobre uso de documentos como artefatos etnográficos e como componentes de uma perspectiva sociomaterial das organizações... ontologia, smith, etc</p>
<p>Por fim, remete a discussões contemporâneas sobre o uso de novas técnicas de machine learning, particularmente de processamento de linguagem natural (NLP) para produção de teoria sociológica. Nesse campo... falar os dois artigos</p>

#### 1.2 Casos de uso
<p>O usuário (caracterísitcas, pesquisador)...</p>
<p>uso primário: por mim mesmo</p>
<p>uso secundário: o banco de dados</p>


### 2. Modelagem

## Desenho do sistema
<p>O principal elemento do sistema será a base de dados. Assim, todo o primeiro conjunto de scripts diz respeito a produção dessa base. A partir dessa base serão utilizados scripts adicionais para análise desses dados. assim, o fluxo pode ser descrito como: Produção da base --> Análise a partir de hipóteses iniciais --> identificação de novas hipóteses --> (re)análise --> etc</p>

### fluxo do sistema
<p>São distinguíveis algumas etapas básicas no projeto. As primeiras etapas são referentes a constituição do banco de dados. 1 - a coleta de dados brutos, realizada com técnicas de scrapping, considerando tanto o texto como metadados de onde aquele texto se origina; 2 - a limpeza do texto bruto a partir de técnicas de pré processamento de texto; 3 - a identificação posterior de metadados sobre as sentenças com base em sua localização no relatório (feito em separado da raspagem, pois exige uma identificação manual dos trechos de cada relatório referentes a certa temática); 4 - identificação de entidades nas sentenças; 5 - classificação das sentenças por tópicos; 6 - amostragem aleatória de sentenças para classificação manual de sentimento; 7 - classificação das demais sentenças por sentimento </p>

<p>A segunda etapa é a realização de um conjunto de análises a partir do banco de dados. São possíveis tanto análises puramente quantitativas a respeito da frequencia de tópicos, entidades e suas localizações no tempo ou seções temáticas dos relatórios, como também será possível análises mais englobantes. Para isto será proposta a construção de modelos word2vec e sentence2vec que permitam trabalhar os significados semanticos dos termos de forma visual e compará-los no tempo e entre distintas empresas. Perceber assim se "marketing" está semanticamente mais próximo de que termos em cada caso ou como as terminologias ligadas a governança corporativa se movimentaram no "espaço semantico" ao londo do tempo.</p>

### Coleta de dados e Desenho da base
<p>A base é constituída a partir de relatórios anuais com informações de empresas da indústria automotiva. A ênfase é nos <i>conteúdos textuais</i> dos relatórios, deixando-se em segundo plano tabelas e dados financeiros.</p>
<p>Cada relatório é "raspado" com auxílio da biblioteca PyPDF2. O texto é extraído por página e depois separado em sentenças a partir do uso de expressões regulares. Algumas informações referentes a cada sentênça sao armazenadas em colunas adicionais. Essas colunas são: </p>

* id --> identificador único daquela sentença na base
* texto --> texto bruto extraído da sentença
* documento --> documento daonde foi extraída a sentença
* ano --> o ano ao qual se refere o documento
* empresa --> empresa a qual se refere o documento
* page --> a página do relatório onde aquela sentença está localizada
* length --> cumprimento da sentença
* words --> dicionário de contágem de palavras únicas na sentença
* segment --> o trecho/seção do relatório ao qual a sentença pertence
* topic --> classificação daquela sentença em tópico a partir de seu conteúdo
* entities --> dicionário com as entidadaes identificadas na sentença
* sentiment --> identificação se a sentença contem sentimento positivo, neutro ou negativo

<p>A proposição é que a base possa servir para agregações e análises tentao produzidas a partir de classificações não supervisionadas (tópicos, entidades), nativos/humanos (segmentos do relatório) ou classificações supervisionadas (sentimento).</p>

<p> Essa abordagem permitira análises quantitativas e qualitativas do conteúdo dos relatórios, além de uma observação de transformações no tempo dos conteúdos presentes no texto e de sua associação a determinadas classificações nativas das organizações (ex. perceber ao longo do tempo que as sentenças relativas ao marketing se tornam mais frequentes e mais positivas, ao passo que sentenças relativas a recursos humanos passam a ser mais raras).</p>

### Scripts e funções
<p>as funções para realização das operações estão divididas em scripts principais divididos em 2 grupos: preparação da base de dados e análise dos dados coletados</p>

### 3. Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

### 4. Conclusões

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

---

Matrícula: 123.456.789

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
