import streamlit as st
from components import *

st.set_page_config(page_title="Transformação de Dados",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.markdown(
"""
## 5. Transformação de Dados
> Descreva um processo ETL (Extract, Transform, Load) que você já realizou ou
como você faria para integrar dados de diferentes fontes em um data warehouse.
Que ferramentas ou linguagens você utilizaria para garantir a consistência e
integridade dos dados?

---

### Resposta
No meu primeiro ano de Iniciação Tecnológica, realizei um processo de ETL com dados do Twitter. O objetivo foi coletar tweets para avaliar a inserção uma palavra e suas variações no léxico brasileiro. O processo partiu da API do Twitter na sua versão gratuita e o uso da biblioteca `Tweepy`. As etapas foram:
- Coletar os dados partindo de palavras-chave: no trabalho em questão, a palavra era "fanfic" e outros conjuntos de palavras que serviam para identificar o contexto de uso da palavra;
- Limpar e organizar os dados: a busca usando a API do Twitter já permitia a coleta de maneira muito organizada, removendo retweets e afins, porém, por ser um trabalho baseado em Processamento de Linguagem Natural, eu fiz um pré-processamento que consistiu na remoção de palavras irrelavantes, emojis, links entre outros elementos que não seriam úteis para a análise;
- Carregar os dados em formato de tabela: os dados foram salvos em um arquivo CSV para facilitar a análise posterior;
- Análise dos dados: com os dados limpos e organizados, fiz uma análise de bigramas e frequências das palavras, procurando pelas associações mais frequentes.

Além da biblioteca para a conexão da API, utilizei também `pandas` na manipulação dos dados e `NLTK` nas análises de texto.

Sei que outras formas de realizar um processo ETL podem envolver o uso de ferramentas como o Airflow, que permite a criação de pipelines de dados de forma mais automatizada, bibliotecas que tenha capacidade para processar grandes volumes de dados, como PySpark e Great Expectations, nas etapas de validação dos dados. Dessas soluções, tive breves contatos tanto com o Airflow quanto com o PySpark.
"""
)