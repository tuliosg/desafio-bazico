import streamlit as st
from components import *

st.set_page_config(page_title="Problema de Negócio com Dados",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.markdown(
"""
## 4. Problema de Negócio com Dados
> Imagine que você tem um conjunto de dados de vendas de um e-commerce com
colunas de 'data da venda', 'valor da venda', e 'produto vendido'. Como você usaria
esses dados para prever a receita dos próximos 3 meses? Que abordagens ou
modelos de previsão você consideraria?

---

### Resposta
Diante de uma situação como essa, meu primeiro instinto é pesquisar sobre modelos relacionados, testes e afins para tomar uma melhor decisão. Com base nisso, cheguei em duas estratégias que podem ser úteis:

#### Média Móvel Simples (MMS)
A Média Móvel Simples consiste em calcular a média de um conjunto de dados em um determinado período de tempo. No caso de vendas, é possível usar a MMS para prever a receita dos próximos 3 meses com base na média das últimas vendas. 

- Primeiro, é necessário definir um período de tempo e somar as vendas diárias. Vou usar como exemplo os últimos 30 dias de vendas;
- Depois de somar os valores das vendas diárias, tira a média;
- Essa média é usada como previsão para o dia seguinte;
- Por fim, é repetir o processo, "deslizando" esse período de 30 dias para prever os próximos 3 meses.

A vantagem dessa abordagem é a simplicidade de implementação e a sua robustez quando se trata de dados estáveis. No entanto, ela não é capaz de capturar tendências de longo prazo ou sazonalidade.

A implementação dessa estratégia é relativamente simples e, em Python, pode ser feita usando `pandas` e `numpy`.

#### Modelo SARIMA (Seasonal AutoRegressive Integrated Moving Average)
O SARIMA é um modelo de auto-regressão que leva em consideração a sazonalidade dos dados. Ele é uma extensão do modelo ARIMA, que é um dos modelos mais populares para previsão de séries temporais.

O modelo analisa as vendas passadas procurando por três tipos de padrões:

- Tendência: A direção geral das vendas (se estão subindo, descendo ou estáveis);
- Sazonalidade: Padrões que se repetem em intervalos fixos (como aumento de vendas nos finais de semana);
- Ruído: Flutuações aleatórias que não seguem um padrão.

Ele usa essas informações para fazer uma previsão mais sofisticada para o futuro.

As vantages dessa abordagem são a capacidade de capturar tendências de longo prazo e sazonalidade, além de ser um modelo mais robusto. No entanto, ele é mais complexo de implementar, além de requerer mais dados históricos para funcionar melhor.

A implementação do modelo SARIMA pode ser feita em Python usando a biblioteca `statsmodels`, mas requer maiores conhecimentos técnicos para ajustar os parâmetros.
"""
)