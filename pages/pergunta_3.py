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
A maioria das ferramentas de visualização de dados que utilizei foram bibliotecas Python, sendo elas  matplotlib, seaborn e plotly. Além dessas, já tive contatos com a ggplot do R e, mais recentemente, com o Orange DataMining, uma ferramenta construída em Python para trabalhar com dados.

Em etapas de análise, uso as visualizações para entender melhor algumas variáveis, suas relações e comportamentos. Alguns exemplos são correlação entre variáveis, distribuição de valores, comparação entre grupos e variação ao longo do tempo.

Dentre os exemplos de visualizações que já construí, destaco alguns gráficos presentes em noteboks do meu portfólio no kaggle:

#### Gráfico de Barras
Na análise que realizei sobre o café Arábica, utilizei um gráfico de barras para mostrar a quantidade de amostras de café por país. O gráfico foi construído com a biblioteca seaborn:

![Gráfico de Barras](https://www.kaggleusercontent.com/kf/161457506/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..jIY_QaNzrDbF8L_a5v6jOw.Ogtggw0eYzfmxoyNOu3PkoDOVTKMzCr9ztiIxhjjv0duSFkkr7oz-A8ySys3ahnMuMbHJn02o3hVW53Wt2M-op83cbt5eUJEADMvhyWBlbY5va_652J0QZFxoGYHY3_i2gKGWSPmzY3JLWEEYWXf8ADkVTvZ8PGmUialcNp8QwqDjdBVSjA8poAIYw6Fkkd39Rmnv6XmoCoGOTgNI5WWBxuh7NlZl1fLLGtLWNA3G9TCBhlhO_JyIYg61P8cud29CKWIhIhgecMLSExJTuBHVV4RxZxAC0nFcK522MkPGJQpQMvub58gKv55s-Q635yI-ouDOikkHdMMMPoKrHPr_RG7d4TmF25MHoafSsznRKZF292_Srvoh7PQEeGgx-7kN7IdF5k9WZ03SQdwe02J3IOi34ydVYKIZC0z8YPcJ790Y5EaMNW7YGpSgWaWUKAEF1wImwq99rteSOD-hunbybaCkT4NK99skjM5xGOzJdYwbTTYXJgkdZ2GntuluGL5pcurFcY2mb-WMKR7HYc4c5bTfLtG-1OS4SMPOP0IBKN6Z-5oCKdWZCWlTO5xd2oVi6s8mhXTlpLWAbIuYbtH7NBNqC1bLL8AJfBqqjJzZMadUgQ9bKmB-6d4a4x4lLQGkmCbOiwDd8ntVngv4iITsLpmiTciQDMhcoVPklYh94k.4h2OLgqNc7o5yKMaYNDCsg/__results___files/__results___25_0.png)

> Gráfico presente no notebook [Uma análise Robusta do café Arábica](https://www.kaggle.com/code/tuliosg/uma-an-lise-robusta-do-caf-ar-bica) | [@tuliosg](https://www.kaggle.com/tuliosg)

#### Mapa Coroplético
Outro exemplo interessante foi o mapa coroplético que construí, também sobre o café Arábica. Nele eu exibi as pontuações médias dos cafés por país. O gráfico foi construído com a biblioteca plotly:
"""
)

st.image("imgs\plot_cafes_pais.png", width=650)

st.markdown(
"""
> Gráfico presente no notebook [Uma análise Robusta do café Arábica](https://www.kaggle.com/code/tuliosg/uma-an-lise-robusta-do-caf-ar-bica) | [@tuliosg](https://www.kaggle.com/tuliosg)

#### Scatterplot
Em uma análise de dados do Spotify, que envolviam as músicas mais ouvidas de 2023, construí um scatterplot para mostrar a relação entre o número de streams e as batidas por minuto (BPM) das músicas. O gráfico foi construído com a biblioteca matplotlib:

![Scatter spotify](https://www.kaggleusercontent.com/kf/167703343/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..6HNO22iWg7fMYWZ6Dj0rYg.WRKBvuN7gFTmhMyiSO0hviO8i9Sun2C8VI5FDpG6rFfCr_yBJCJ4cyNGCza6zM-LIc5-6yHvLFsijV2G8pis-tRr5GeEIk3pzH2-inJhgqeVdvZLeaI9bcdZjApt1tIF48ixNkAtEiu3RnZUb5xj3Wj1HzwC6FHyxURPQptiRoCHsQSPcU1q3Cd7IhbLyrOzom632uWgWARdyscAjCrEq7HH1VYtNf1ClnTo5Rdpr6pDPJLExyVnUHiFR0MEIkUrZre4jDhvU85Ym8nzgObmpoo6MFiVv2vJqNqFHIjvlgmVFky5o4EnU1zuRF9ftWKrPAchxaG9M-HOjyR07JMoJ_Bw_hLMRNbad3CqdqAPYpnYM1u-D9n0dxTnQVxGwtSLyy-o8ZqI9cgJhAlasWqc_Qe83Rj5ggsDrFGolguTq5wlbPihFDRK0yOLWCXj4HVgGLfv-VSPpZyDqhJsK82TXYFSGmNN9dcYeDt_aogEcz3aD-05gP0e-6LeShy6BJqLvNggFHdDmdpZilKGwT0g_AAyu4qY_d9eWjJICf3VC8H3gghSYgd_DoG2EmGaVs6WRHh9IH8uvQUx0MIUA_I7IArg3f6QO3y_Cv33fBFtPLGHvJgGNP71GUD276dWa1G_e68ntw4mlAlJaA_EXpKNlVFcwHEQpK8yVepMnjbHQhg.JhLubasIkmVo6-RxW0v7ew/__results___files/__results___24_0.png)

> Gráfico presente no notebook [Dados, onde vivem? Explorando os dados do Spotify](https://www.kaggle.com/code/tuliosg/dados-onde-vivem-explorando-os-dados-do-spotify) | [@tuliosg](https://www.kaggle.com/tuliosg)

"""
)