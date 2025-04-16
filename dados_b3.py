import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import zipfile
import os


def setores_bolsa(caminho_downloads):

    print("\nColetando Setores da Bolsa...")

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm'

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "bvmf_iframe")))


    botao_expandir = driver.find_element('xpath', '//*[@id="accordionClassification"]/div/app-companies-home-filter-classification/form/div[2]/div[3]/div[2]/p/a')

    driver.execute_script("arguments[0].click();", botao_expandir)

    planilha = driver.find_element('xpath', '/html/body/app-root/app-companies-home/div/div/div/div/div[2]/div[2]/div/app-companies-home-filter-classification/form/div[2]/div[3]/div[2]/p/a')

    driver.execute_script("arguments[0].click();", planilha) 

    time.sleep(5)

    driver.quit()

    with zipfile.ZipFile(caminho_downloads + r"\ClassifSetorial.zip") as arquivo_zip:
        for nome_planilha in arquivo_zip.namelist():
            with arquivo_zip.open(nome_planilha) as plan:
                setores = pd.read_excel(plan, skiprows=6)

    setores['SUBSETOR'] = setores['SUBSETOR'].ffill()

    setores = setores.dropna(subset = ['SEGMENTO'])

    setores = setores[['SUBSETOR', 'SEGMENTO', 'LISTAGEM']]

    setores = setores.dropna()

    setores.columns = ['SETOR', 'NOME', 'TICKER']

    os.remove(caminho_downloads + r"\ClassifSetorial.zip")

    setores.to_csv("setores.csv", index = False) 


def composicao_ibov(caminho_downloads):

    print("\nColetando composição do Ibovespa...")

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm'

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "bvmf_iframe")))
    
    time.sleep(3)

    planilha = driver.find_element("xpath", '//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/p/a')

    driver.execute_script("arguments[0].click();", planilha)

    time.sleep(5)

    driver.quit()

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    if dia < 10:
        
        dia = "0" + str(dia)

    if mes < 10:
        
        mes = "0" + str(mes)
        
    ano = str(ano)[2:]

    ibovespa_comp = pd.read_csv(caminho_downloads + fr"\IBOVDia_{dia}-{mes}-{ano}.csv", sep = ";", 
                            skipfooter = 2, encoding = 'ISO-8859-1', engine = 'python', decimal = ',',
                           thousands = ".", header = 1, index_col = False)
    
    
    os.remove(caminho_downloads + fr"\IBOVDia_{dia}-{mes}-{ano}.csv")

    ibovespa_comp.columns = ['codigos', 'nome', 'classe', 'qtd', 'part']
    
    ibovespa_comp.to_csv("comp_ibov.csv", index = False)


if __name__ == "__main__":

    caminho_downloads = r'C:\Users\Gabriel Lima\Downloads'

    # composicao_ibov(caminho_downloads)

    # setores_bolsa(caminho_downloads)