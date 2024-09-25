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

### Resposta

Comecei essa estimativa dando uma boa olhada no Instagram de vocês. As informações que mais me chamaram atenção foram as seguintes:
- O time da Bázico chegou em Salvador no dia 03/09 mas só começou as operações no dia 04;
- Pelo instagram, a campanha durou algo entre 20 e 23 dias;
- Nos reels em que apareciam algumas pessoas vestindo as roupas da bázico, cheguei em uma estimativa aproximada de 25 peças por reel;
- Houve também o sorteio de 40 camisas, aumentando o total;
- No dia 23/09 houve um post dizendo que haviam mais de 500 bázicas em Salvador.

Levando em consideração essas informações, fiz algumas contas para chegar em um mínimo e um máximo:
- **Mínimo**: 20 dias de campanha x 25 peças por reel + 40 do sorteio = **540 peças**
- **Máximo**: 23 dias de campanha x 25 peças por reel + 40 do sorteio = **615 peças**
"""
)