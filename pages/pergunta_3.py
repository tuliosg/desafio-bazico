import streamlit as st
from components import *

st.set_page_config(page_title="Ferramentas de Análise",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.markdown(
"""
## 3. Ferramentas de Análise
> Quais ferramentas de visualização de dados você já usou (como Power BI,
Tableau, Matplotlib, etc.) e como você as utilizaria para gerar insights a partir de
um conjunto de dados? Dê um exemplo de um painel ou gráfico que você já
criou.

---
"""
)

st.markdown(
"""
### Resposta
A maioria das ferramentas de visualização de dados que utilizei foram bibliotecas Python, sendo elas  matplotlib, seaborn e plotly. Além dessas, já tive contato com a ggplot do R e, mais recentemente, com o Orange DataMining, uma ferramenta construída em Python para trabalhar com dados.

Em etapas de análise, uso as visualizações para entender melhor algumas variáveis, suas relações e comportamentos. Alguns exemplos são correlação entre variáveis, distribuição de valores, comparação entre grupos e variação ao longo do tempo.

Dentre os exemplos de visualizações que já construí, destaco alguns gráficos presentes em noteboks do meu portfólio no kaggle:

#### Gráfico de Barras
Na análise que realizei sobre o café Arábica, utilizei um gráfico de barras para mostrar a quantidade de amostras de café por país. O gráfico foi construído com a biblioteca seaborn:
"""
)

st.image("https://github.com/tuliosg/desafio-bazico/blob/main/imgs/cafes_pais.png?raw=true", width=650)

st.markdown(
"""
> Gráfico presente no notebook [Uma análise Robusta do café Arábica](https://www.kaggle.com/code/tuliosg/uma-an-lise-robusta-do-caf-ar-bica) | [@tuliosg](https://www.kaggle.com/tuliosg)

#### Mapa Coroplético
Outro exemplo interessante foi o mapa coroplético que construí, também sobre o café Arábica. Nele eu exibi as pontuações médias dos cafés por país. O gráfico foi construído com a biblioteca plotly:
""")

st.image("https://github.com/tuliosg/desafio-bazico/blob/main/imgs/plot_cafes_pais.png?raw=true", width=600)

st.markdown(
"""
> Gráfico presente no notebook [Uma análise Robusta do café Arábica](https://www.kaggle.com/code/tuliosg/uma-an-lise-robusta-do-caf-ar-bica) | [@tuliosg](https://www.kaggle.com/tuliosg)

#### Scatterplot
Em uma análise de dados do Spotify, que envolviam as músicas mais ouvidas de 2023, construí um scatterplot para mostrar a relação entre o número de streams e as batidas por minuto (BPM) das músicas. O gráfico foi construído com a biblioteca matplotlib:
"""
)

st.image("https://github.com/tuliosg/desafio-bazico/blob/main/imgs/scatter_spotify.png?raw=true", width=500)

st.markdown(
"""
> Gráfico presente no notebook [Dados, onde vivem? Explorando os dados do Spotify](https://www.kaggle.com/code/tuliosg/dados-onde-vivem-explorando-os-dados-do-spotify) | [@tuliosg](https://www.kaggle.com/tuliosg)

"""
)