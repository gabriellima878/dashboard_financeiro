from dados_b3 import composicao_ibov, setores_bolsa
from dados_di import webscraping_di
from dados_mt5 import construcao_historica_cotacoes, selecionando_tickers
from dados_bacen import att_inflacao, att_divida_pib, att_dolar
from dados_noticias import scraping_noticias
import time

while True:

    def atualizar_rotinas():

        caminho_downloads = r'C:\Users\Gabriel Lima\Downloads'

        selecionando_tickers()
        construcao_historica_cotacoes()
        composicao_ibov(caminho_downloads)
        setores_bolsa(caminho_downloads)
        att_inflacao()
        att_divida_pib()
        att_dolar()
        webscraping_di()
        scraping_noticias()

    atualizar_rotinas()

    time.sleep(86400)