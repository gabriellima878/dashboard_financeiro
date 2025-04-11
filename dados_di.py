import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time 
import datetime
import plotly.graph_objects as go
from selenium.common.exceptions import NoSuchElementException


def webscraping_di():

    hoje = datetime.datetime.now()
    um_ano_atras = hoje - datetime.timedelta(days = 365)
    tres_anos_atras = hoje - datetime.timedelta(days = 365 * 3)
    cinco_anos_atras = hoje - datetime.timedelta(days = 365 * 5)
    dez_anos_atras = hoje - datetime.timedelta(days = 365 * 10)

    lista_datas = [hoje, um_ano_atras, tres_anos_atras, cinco_anos_atras, dez_anos_atras]
    lista_nomes = ['hoje', 'um_ano_atras', 'tres_anos_atras', 'cinco_anos_atras', 'dez_anos_atras']

    legenda = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                        index = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'])
    
    lista_dfs = []

    for n, data in enumerate(lista_datas):
         
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        data_pontual = data

        for i in range(0, 5):
             
            data_teste = data_pontual.strftime("%d/%m/%Y")

            url = f'''https://www2.bmf.com.br/pages/portal/bmfbovespa/boletim1/SistemaPregao1.asp?
            pagetype=pop&caminho=Resumo%20Estat%EDstico%20-%20Sistema%20Preg%E3o&Data={data_teste}
            &Mercadoria=DI1'''

            try:

                tabela, indice = pegando_dados_di(url, driver)

                break

            except NoSuchElementException:
                 
                data_pontual = data_pontual - datetime.timedelta(days = 1)

        driver.quit()    

        dados_di = tratando_dados_di(tabela, indice, legenda)

        dados_di = dados_di.reset_index()
        dados_di.columns = ['data_vencimento', 'preço']
        dados_di['data_preco'] = lista_nomes[n]

        lista_dfs.append(dados_di)

    dados_di = pd.concat(lista_dfs, ignore_index=True)
    dados_di.to_csv("dados_di.csv", index = False)

    return dados_di

def pegando_dados_di(url, driver):
        
        sem_conexao = True
        
        while sem_conexao:
            try:
                driver.get(url)
                sem_conexao = False
            except:
                pass
                
        time.sleep(3)

        local_tabela = '''

        /html/body/form[1]/table[3]/tbody/tr[3]/td[3]/table
        '''

        local_indice = '''
        /html/body/form[1]/table[3]/tbody/tr[3]/td[1]
        '''

        elemento = driver.find_element("xpath", local_tabela)

        elemento_indice = driver.find_element("xpath", local_indice)

        html_tabela = elemento.get_attribute('outerHTML')
        html_indice = elemento_indice.get_attribute('outerHTML')

        

        tabela = pd.read_html(html_tabela)[0]
        indice = pd.read_html(html_indice)[0]

        return tabela, indice

    
def tratando_dados_di(df_dados, indice, legenda):
        
    df_dados.columns = df_dados.loc[0]

    df_dados = df_dados['ÚLT. PREÇO']

    df_dados = df_dados.drop(0, axis = 0)

    indice.columns = indice.loc[0]

    indice = indice.drop(0, axis = 0)
    
    df_dados.index = indice['VENCTO']
    
    df_dados = df_dados.astype(int)

    df_dados = df_dados[df_dados != 0]

    df = df_dados/1000

    lista_datas = []

    for indice in df.index:

        letra = indice[0]
        ano = indice[1:3]

        mes = legenda[letra]

        data = f"{mes}-{ano}"

        data = datetime.datetime.strptime(data, "%b-%y")

        lista_datas.append(data)
        
    df.index = lista_datas  

    df = df/100
        
    return df 

    

if __name__ == "__main__":

    dados_di = webscraping_di()
    print(dados_di)
















