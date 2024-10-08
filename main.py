import streamlit as st
from components import *

st.set_page_config(page_title="Desafio Bázico",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.title("Desafio Analítico e Estratégico ≠")
st.subheader("Desafio de Dados")
st.markdown("> Desenvolvido por: **Túlio Gois**")
st.divider()

st.write("""
E ai, pessoal da Bázico! Tudo tranquilo?

Fiquei muito feliz por ter passado de fase no processo e chegado até o desafio de dados :) 
         
Ao ver que a apresentação era por minha conta, pensei em trazer algo que fosse diferente.
Então aqui eu vos apresento a minha:

### Resposta ao Desafio de Dados ≠
         
#### Introdução
> Esse é um **Data App interativo**, construído usando o Streamlit, uma biblioteca de Python para criação de aplicações web. Nele você pode navegar pelas perguntas e respostas do desafio, além de visualizar todos os códigos e dados que utilizei*.

#### Navegando pelas Perguntas
> Para acessar as perguntas, basta clicar no menu lateral esquerdo (caso não esteja aparecendo, no canto superior esquerdo terá uma setinha, basta clicar). Lá você encontrará as perguntas do desafio e poderá visualizar as respostas que preparei para cada uma delas.  


Qualquer dúvida, estou à disposição para esclarecer. Espero que gostem!

---    

> **O desenvolvimento desse Data App foi registrado no GitHub e todos os códigos estão disponíveis no repositório [desafio-bazico](https://github.com/tuliosg/desafio-bazico)*
         
""")
