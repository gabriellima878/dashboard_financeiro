import pandas as pd
import MetaTrader5 as mt5
import pandas as pd
import datetime
import pytz


def login_mt5(login, password, server):
    # Verifica se o terminal já está inicializado
    if mt5.terminal_info() is not None:
        print("Já está logado no MetaTrader 5.")
        return True  # Retorna True para indicar que já está logado

    # Caso não esteja logado, tenta inicializar e fazer login
    if not mt5.initialize(login=login, password=password, server=server):
        print("Falha ao inicializar o MetaTrader 5", mt5.last_error())
        mt5.shutdown()
        exit()
    print("Login realizado com sucesso")
    return True


def pegando_todos_os_tickers():

    login_mt5(login = 12345678, password = '123456', server = 'XPMT5-DEMO')

    simbolos = mt5.symbols_get()

    tickers = [simbolo.name for simbolo in simbolos]

    tickers = sorted(tickers, reverse=True)

    acoes = []

    for ticker in tickers:
    
        try:
            int(ticker[3]) #a quarta letra tem que ser uma string, não um número
        except:
            
            final_ticker = ticker[4:]

            if len(final_ticker) == 2:

                if final_ticker == "11":

                    if (ticker[0:4] + "3") in acoes or (ticker[0:4] + "4") in acoes:

                        acoes.append(ticker)

            if len(final_ticker) == 1:  

                if final_ticker == "3" or final_ticker == "4":

                    acoes.append(ticker)

    return acoes    


def gerar_lista_principais():

    '''
    O vencimento do contrato de dólar acontece no primeiro dia útil de todo mês.
    Já o vencimento do contrato de índice acontece a cada dois meses (somente nos meses pares).
    '''
     
    legenda_indice = pd.Series([2, 4, 6, 8, 10, 12],
                        index = ['G', 'J', 'M', 'Q', 'V', 'Z'])
    
    legenda_dolar = pd.Series(list(range(1, 13)),
                        index = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'])
    
    ano = datetime.datetime.now().year
    mes = datetime.datetime.now().month

    if mes == 12:

        letra_indice = 'G'
        letra_dolar = 'F'
        codigo_indice = 'WIN' + letra_indice + str(ano + 1)[2:]
        codigo_dolar = 'WDO' + letra_dolar + str(ano + 1)[2:]
    
    else:
         
        letra_indice = (legenda_indice[legenda_indice > mes]).index[0]
        letra_dolar = (legenda_dolar[legenda_dolar > mes]).index[0]

        codigo_indice = 'WIN' + letra_indice + str(ano)[2:]
        codigo_dolar = 'WDO' + letra_dolar + str(ano)[2:]

    tickers_juros = ['DI1F' + str(ano_escolhido)[2:] for ano_escolhido in range(ano + 1, ano + 6)] 

    tickers_mercado = [codigo_indice, codigo_dolar, 'SMAL11', 'IVVB11'] + tickers_juros

    return tickers_mercado


def selecionando_tickers():

    acoes = pegando_todos_os_tickers()

    tickers_mercado = gerar_lista_principais()
    
    tickers_totais = acoes + tickers_mercado

    for ticker in tickers_totais:

           mt5.symbol_select(ticker)



def puxando_cotacoes(tickers_escolhidos, principal = False):

    login_mt5(login = 12345678, password = '123456', server = 'XPMT5-DEMO')

    df_cotacoes = pd.DataFrame(columns=['Ticker', 'Preço', 'Retorno'], index=list(range(0, len(tickers_escolhidos))))

    for i, ticker in enumerate(tickers_escolhidos):

        if principal == False:

            if mt5.symbol_info(ticker).session_deals > 10:

                retorno = mt5.symbol_info(ticker).price_change
                fechamento = mt5.symbol_info(ticker).last

                df_cotacoes.loc[i, :] = [ticker, fechamento, retorno]

        else:
             
            retorno = mt5.symbol_info(ticker).price_change
            fechamento = mt5.symbol_info(ticker).last

            df_cotacoes.loc[i, :] = [ticker, fechamento, retorno]


    return df_cotacoes


def maiores_altas(tickers_ibov):
        
        acoes = pegando_todos_os_tickers()

        df = puxando_cotacoes(acoes)

        df = df[df['Ticker'].isin(tickers_ibov)]

        df = df.sort_values("Retorno", ascending = False)
        df = df.head(3)
        df = df.reset_index(drop = True)

        return df

def maiores_baixas(tickers_ibov):

        acoes = pegando_todos_os_tickers()

        df = puxando_cotacoes(acoes)
        
        df = df[df['Ticker'].isin(tickers_ibov)]

        df = df.sort_values("Retorno", ascending = True)
        df = df.head(3)
        df = df.reset_index(drop = True)

        return df


def construcao_historica_cotacoes():
    
    acoes = pegando_todos_os_tickers()
    lista_df_cotacoes = []
    timezone = pytz.timezone("Brazil/West")
    data_inicial = (datetime.datetime.now(tz = timezone) - datetime.timedelta(days= 1095))
    data_final = datetime.datetime.now(tz = timezone)

    for acao in acoes:

        try:

            cotacoes = mt5.copy_rates_range(acao, mt5.TIMEFRAME_D1, data_inicial, data_final)

            cotacoes = pd.DataFrame(cotacoes)
            
            cotacoes = cotacoes[['time', 'open', 'high', 'low', 'close']]
            cotacoes['time']=pd.to_datetime(cotacoes['time'], unit='s')
            cotacoes['ticker'] = acao

        except:
             
             print(acao)

        lista_df_cotacoes.append(cotacoes)

    cotacoes_finais = pd.concat(lista_df_cotacoes)

    empresas = cotacoes_finais['ticker'].unique()

    df_empresas = pd.DataFrame({'tickers': empresas})

    df_empresas.to_csv('tickers.csv', index = False)
    cotacoes_finais.to_parquet("cotacoes.parquet", index = False) 



if __name__ == "__main__":


    # todas_as_acoes = pegando_todos_os_tickers()
    # print(todas_as_acoes)

    # tabela = puxando_cotacoes(tickers_escolhidos=['WEGE3', 'PETR4'])
    # print(tabela)

    construcao_historica_cotacoes()

























