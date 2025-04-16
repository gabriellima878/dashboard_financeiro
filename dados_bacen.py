from bcb import sgs
from datetime import timedelta
from datetime import datetime
import pandas as pd
import time

def att_inflacao():

    print("\nColetando dados de inflação...")

    hoje = datetime.now()
    inicio = hoje - timedelta(days=4000)
    max_tentativas = 5
    tentativas = 0
    inflacao = None

    while tentativas < max_tentativas:
        try:
            inflacao = sgs.get({'ipca': 433, 'igp-m': 189}, start=inicio)
            break  # Sai do loop se a solicitação for bem-sucedida
        except Exception as e:
            tentativas += 1
            print(f"Tentativa {tentativas}: Erro - {e}")
            time.sleep(5)  # Aguarda 5 segundos antes de tentar novamente

    if inflacao is None:
        raise Exception("Não foi possível obter os dados de inflação após várias tentativas.")

    inflacao = inflacao / 100
    inflacao.to_csv('inflacao.csv')

def att_divida_pib():

    print("\nColetando dados do PIB...")

    hoje = datetime.now()
    um_ano_atras = hoje - timedelta(days = 4000)
    dados = None

    while isinstance(dados, pd.DataFrame) == False:

        dados = sgs.get({'DIVIDA_PIB':13762}, start = um_ano_atras)

    dados = dados/100

    dados.to_csv('divida_pib.csv')

def att_dolar():

    print("\nColetando dados do Dólar...")

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
    att_inflacao()
    # att_dolar()



















