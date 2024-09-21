import streamlit as st

def menu_navegacao():
    st.sidebar.image("imgs/bazico_svg.svg", use_column_width="auto")
    st.sidebar.divider()
    st.sidebar.markdown("### Página inicial")
    st.sidebar.page_link(page='main.py', label='Desafio Bázico **≠**')
    st.sidebar.markdown("### Perguntas")
    st.sidebar.page_link(page="pages/pergunta_1.py", label="1. SQL")
    st.sidebar.page_link(page="pages/pergunta_2.py", label="2. Python")
    st.sidebar.page_link(page="pages/pergunta_3.py", label="3. Ferramentas de Análise")
    st.sidebar.page_link(page="pages/pergunta_4.py", label="4. Problema de Negócio")
    st.sidebar.page_link(page="pages/pergunta_5.py", label="5. Transformação de Dados")
    st.sidebar.page_link(page="pages/pergunta_6.py", label="6. Campanha em Salvador")

    st.sidebar.divider()
    st.sidebar.markdown("<small>Desenvolvido por: [Túlio Gois](https://www.linkedin.com/in/tuliosg/) </small>", unsafe_allow_html=True)