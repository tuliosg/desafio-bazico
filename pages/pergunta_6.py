import streamlit as st
from components import *

st.set_page_config(page_title="Campanha em Salvador",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.markdown(
"""
## 6. Campanha em Salvador
> Quantas bázicas existem em Salvador? Me mostre seu raciocínio para estimar
quantas bázicas existem na cidade que estamos fazendo campanha. Quais
números você utilizou para estimar isso? Não existe certo ou errado, o que
importa é como você faria essa estimativa.

---
"""
)