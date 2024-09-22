import streamlit as st
from components import *

st.set_page_config(page_title="SQL",
                   layout="wide",
                   page_icon="imgs/bazico.png")
                   
menu_navegacao()

st.markdown(
"""
## 1. SQL
> Explique como você faria para identificar registros duplicados em uma tabela SQL
e, em seguida, como você os removeria. Dê um exemplo prático usando SQL.

---
"""
)

st.markdown(
"""
### Solução
Para essa pergunta, considerei uma tabela chamada `vendas_roupas_ficticias` com as seguintes colunas:
- `id_venda`
- `data_venda` 
- `valor_venda` 
- `produto_vendido` 
- `quantidade_vendida` 

Primeiramente, é identifiquei os registros de vendas duplicados. Nesse caso, um registro duplicado seria aquele que possui os mesmos valores em todas as colunas. Para esse passo, a query foi:

```sql
SELECT 
    data_venda, 
    valor_venda, 
    produto_vendido, 
    quantidade_vendida, 
    COUNT(*) as contagem
FROM 
    vendas_roupas_ficticias
GROUP BY 
    data_venda, valor_venda, produto_vendido, quantidade_vendida
HAVING 
    COUNT(*) > 1
ORDER BY 
    contagem DESC;
```

No fim desse passo, consegui identificar as linhas que ocorrem mais de uma vez na tabela. Para remover esses registros duplicados, usei a estratégia de criar uma tabela temporária com os registros únicos, mantendo aqueles com o menor `id_venda` e apagando os registros que não estão na tabela temporária. A query para esse passo foi:

```sql
CREATE TEMPORARY TABLE ids_unicos AS
SELECT MIN(id_venda) as id_venda
FROM vendas_roupas_ficticias
GROUP BY data_venda, valor_venda, produto_vendido, quantidade_vendida;

DELETE FROM vendas_roupas_ficticias
WHERE id_venda NOT IN (SELECT id_venda FROM ids_unicos);

DROP TEMPORARY TABLE ids_unicos;
```

Outra abordagem válida seria criar uma nova tabela que não tivesse essas duplicatas e, no final, substituir a tabela original.
"""
)