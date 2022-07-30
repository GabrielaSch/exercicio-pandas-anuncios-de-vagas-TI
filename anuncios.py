import pandas as pd
import matplotlib.pyplot as plt

# 1.0 abrir o arquivo e ler a tabela 
import csv
df = pd.read_csv("anuncios.csv", sep = ',', low_memory=False)
print(novodf.head())

# 1.1 selecionar as colunas de interesse
newcol = ['Empresa', 'Nome da ocupação']
newdata = pd.read_csv("anuncios.csv", sep = ',', low_memory=False, usecols=newcol)

# 1.2 gerar gráfico do número de vagas por empresas 
newdata['Empresa'].value_counts()[:20].plot(kind='barh', alpha=0.6, color=['m','c','r','k','b'], figsize = (12, 8), width = 0.5)
plt.xlabel("Número de vagas")
plt.ylabel("Empresa")
plt.title("Número de ocupações por empresa", fontsize= 14)

# 2.0 definir as palavras vazias
from wordcloud import WordCloud, STOPWORDS
stop_words = STOPWORDS.update(["para", "de", "em", "o", "ou", "que", "da", "e", "na", "das", "os", "ter", "nosso",\
                               "ser", "etc", "ao", "dos", "outras", "nossos", "é", "incluindo", "nas", "também",\
                               "um", "será um", "realizar", "forma", "seu", "aos", "will", "sobre", "sua", "nos",\
                               "se", "outra", "toda", "por", "você", "mais"])

# 2.1 gerar a núvem de palavras 
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(999.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(90.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=open ("anuncios.csv", encoding='utf-8').read()

wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords = stop_words,
                            background_color = 'white',
                            width = 1200,
                            height = 1200,
                            color_func = random_color_func
                            ).generate(file_content)

plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
