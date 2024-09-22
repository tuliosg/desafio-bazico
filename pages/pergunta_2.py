import streamlit as st
from components import *
import pandas as pd

st.set_page_config(page_title="Python",
                   layout="wide",
                   page_icon="imgs/bazico.png")

menu_navegacao()

st.markdown(
"""
## 2. Python
> Você tem um arquivo CSV grande com dados de vendas que precisa ser
processado e analisado. Descreva como você usaria Python e bibliotecas como
Pandas para realizar a limpeza dos dados, tratamento de valores ausentes e
análise básica. Forneça exemplos de código.

---
"""
)

st.markdown(
"""
### Solução
Para demonstrar melhor a solução para a pergunta, gerei um arquivo CSV chamado `vendas_roupas_ficticias.csv` que possui pouco mais de 500 linhas e as seguintes colunas:
- `data da venda`
- `valor da venda`
- `produto vendido`
- `quantidade vendida`
"""
)

with st.expander("**Clique aqui para ver o dataset original**", icon="🎲"):
    df = pd.read_csv("data/raw/vendas_roupas_ficticias.csv")
    st.dataframe(df)

with st.container(border=True):
    st.markdown(
    """
    ### Analisando o dataset `vendas_roupas_ficticias.csv`
    """
    )

    st.code("""
    import pandas as pd
    df_vendas = pd.read_csv("vendas_roupas_ficticias.csv")
    df_vendas.info()
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            RangeIndex: 525 entries, 0 to 524
            Data columns (total 4 columns):
            #   Column              Non-Null Count  Dtype
            ---  ------              --------------  -----
            0   data da venda       525 non-null    object
            1   valor da venda      491 non-null    float64
            2   produto vendido     525 non-null    object
            3   quantidade vendida  525 non-null    int64
            dtypes: float64(1), int64(1), object(2)
            """
        )
    
    st.markdown(
    """
    #### Organização e Limpeza
    ##### Renomeando colunas
    Uma boa prática de programação é evitar acentos e espaços em branco no nomes das colunas, então resolvi aterá-los.
    """
    )

    st.code(
    """
    df_vendas.rename(columns={
    'data da venda': 'data_venda',
    'valor da venda': 'valor_venda',
    'produto vendido': 'produto_vendido',
    'quantidade vendida': 'quantidade_vendida'
    }, inplace=True)
    df_vendas.columns
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            Index(['data_venda', 'valor_venda', 'produto_vendido', 'quantidade_vendida'], dtype='object')
            """
        )

    st.markdown(
    """
    ##### Valores ausentes
    A tabela tem valores ausentes na coluna `valor da venda`. Por representar apenas 6\% do total de registros (isso sem considerar se há duplicatas), optei por zerar esses valores. Mas existem outras estratégias, como utilizar a média ou verificar os valores das peças vendidas para preencher.
    """
    )

    st.code(
    """
    df_vendas['valor_venda'].fillna(0, inplace=True)
    df_vendas['valor_venda'].isnull().sum()
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            0
            """
        )

    st.markdown(
    """
    ##### Valores duplicados
    Seguindo a limpeza dos dados, realizei a análise dos valores duplicados e os removi, deixando apenas o último registro. A lógica aqui foi a inserção de uma venda incompleta que posteriormente foi inserida corretamente.
    """
    )

    st.code(
    """
    df_vendas.drop_duplicates(inplace=True, keep='last')
    df_vendas.info()
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            Int64Index: 500 entries, 0 to 524
            Data columns (total 4 columns):
            #   Column              Non-Null Count  Dtype  
            ---  ------              --------------  -----  
            0   data_venda          500 non-null    object 
            1   valor_venda         500 non-null    float64
            2   produto_vendido     500 non-null    object 
            3   quantidade_vendida  500 non-null    int64  
            dtypes: float64(1), int64(1), object(2)
            """
        )

    st.markdown(
    """
    #### Análise básica
    ##### Estatísticas dos valores de venda
    Finalizadas as etapas de limpeza, iniciei a análise pela coluna `valor_venda`, que possui valores monetários. Como zerei os valores ausentes na tabela, resolvi criar uma cópia do DataFrame para não perder os dados originais e realizar a análise com um DF sem vendas fiadas.
    """
    )

    st.code(
    """
    df_vendas_processed = df_vendas[df_vendas['valor_venda'] > 0]
    print(f"
    Análise básica das vendas (com relação aos valores):
    - Média: R$ {df_vendas_processed['valor_venda'].mean():.2f}
    - Mediana: R$ {df_vendas_processed['valor_venda'].median():.2f}
    - Mínimo: R$ {df_vendas_processed['valor_venda'].min():.2f}
    - Máximo: R$ {df_vendas_processed['valor_venda'].max():.2f}
    ")
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            Análise básica das vendas (com relação aos valores):
            - Média: R$ 262.01
            - Mediana: R$ 273.06
            - Mínimo: R$ 20.37
            - Máximo: R$ 498.74
            """
        )

    st.markdown(
    """
    ##### Produtos mais vendidos
    """)
    st.code(
    """
    print(f"
    Os produtos mais vendidos foram:
    {df_vendas_processed['produto_vendido'].value_counts()}
    ")
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            Os produtos mais vendidos foram:
            Jaqueta     66
            Calça       61
            Moletom     56
            Saia        50
            Short       50
            Camiseta    49
            Tênis       47
            Vestido     45
            Blusa       43
            Name: produto_vendido, dtype: int64
            """
        )

    st.markdown(
    """
    ##### Quantidade de vendas por mês
    """
    )

    st.code(
    """
    df_vendas_processed['data_venda'] = pd.to_datetime(df_vendas_processed['data_venda'])

    print(f"
    Os meses com mais vendas são:
    {df_vendas_processed['data_venda'].dt.month_name(locale='pt_BR').value_counts().head(3)}
    
    Já os meses com menos vendas são:
    {df_vendas_processed['data_venda'].dt.month_name(locale='pt_BR').value_counts().tail(3)}
    ")
    """, language='python')

    with st.expander("**Saída**", icon="💻"):
        st.code(
            """
            Os meses com mais vendas são:
            Março       43
            Dezembro    43
            Agosto      43
            Name: data_venda, dtype: int64

            Já os meses com menos vendas são:
            Janeiro      37
            Fevereiro    32
            Setembro     29
            Name: data_venda, dtype: int64
            """
        )
    