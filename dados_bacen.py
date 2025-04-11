from bcb import sgs
from datetime import timedelta
from datetime import datetime
import pandas as pd

def att_inflacao():

    hoje = datetime.now()
    inicio = hoje - timedelta(days = 4000)

    inflacao = None

    while isinstance(inflacao, pd.DataFrame) == False:

        inflacao = sgs.get({'ipca': 433,
                    'igp-m': 189}, start = inicio)
    
    inflacao = inflacao/100
    inflacao.to_csv('inflacao.csv')

def att_divida_pib():

    hoje = datetime.now()
    um_ano_atras = hoje - timedelta(days = 4000)
    dados = None

    while isinstance(dados, pd.DataFrame) == False:

        dados = sgs.get({'DIVIDA_PIB':13762}, start = um_ano_atras)

    dados = dados/100

    dados.to_csv('divida_pib.csv')

def att_dolar():

    hoje = datetime.now()
    inicio = hoje - timedelta(days = 365 * 10)  # Tenta com 10 anos
    
    max_tentativas = 5
    tentativas = 0
    dados = None

    while not isinstance(dados, (pd.DataFrame, pd.Series)) and tentativas < max_tentativas:

        try:

            dados = sgs.get({'DOLAR': 1}, start=inicio)

        except Exception as e:

            print(f"Tentativa {tentativas+1}: Erro - {e}")

        tentativas += 1

    if not isinstance(dados, (pd.DataFrame, pd.Series)):

        raise Exception("Não foi possível obter os dados do Dólar após várias tentativas.")

    # Converte para DataFrame se retornar uma Series

    if isinstance(dados, pd.Series):

        dados = dados.to_frame()
    
    dados.to_csv("dolar.csv")



if __name__ == "__main__":

    # att_divida_pib()
    # att_inflacao()
    att_dolar()



















