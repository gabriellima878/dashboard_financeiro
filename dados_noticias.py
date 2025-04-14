from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def g1_tech():
     
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    url = 'https://g1.globo.com/tecnologia/'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    caixas_restantes = soup.find_all("div", class_ = 'feed-post bstn-item-shape type-materia') 

    df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

    for i, noticia in enumerate(caixas_restantes):

        manchete = noticia.find("p", elementtiming = 'text-csr').text
        link =  noticia.find("h2").a['href']

        df_noticias.loc[i, 'subtopico'] = "Economia"
        df_noticias.loc[i, 'manchete'] = manchete
        df_noticias.loc[i, 'link'] = link
        df_noticias.loc[i, 'topico'] = 'tech'
        df_noticias.loc[i, 'jornal'] = 'g1'

        if i == 5:
             
             break
    
    return df_noticias




def g1_economia():
     
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    url = 'https://g1.globo.com/economia/'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    caixas_destaque = soup.find_all("div", class_ = 'bstn-hl-wrapper') 

    df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

    for i, noticia in enumerate(caixas_destaque):

        subtopico = noticia.find("li", class_ = 'bstn-hl-itemlist bstn-hl-chapeuitem').span.text
        manchete = noticia.find("div", class_ = '_evt').span.text
        link = noticia.a['href']

        df_noticias.loc[i, 'subtopico'] = subtopico
        df_noticias.loc[i, 'manchete'] = manchete
        df_noticias.loc[i, 'link'] = link
        df_noticias.loc[i, 'topico'] = 'economia'
        df_noticias.loc[i, 'jornal'] = 'g1'

        if i == (len(caixas_destaque) - 1):

            i = i + 1

    caixas_restantes = soup.find_all("div", class_ = 'feed-post bstn-item-shape type-materia') 

    for noticia in caixas_restantes:

        manchete = noticia.find("p", elementtiming = 'text-csr').text
        link =  noticia.find("h2").a['href']

        df_noticias.loc[i, 'subtopico'] = "Economia"
        df_noticias.loc[i, 'manchete'] = manchete
        df_noticias.loc[i, 'link'] = link
        df_noticias.loc[i, 'topico'] = 'economia'
        df_noticias.loc[i, 'jornal'] = 'g1'

        if i == 5:
             
             break
        
        i = i + 1

    return df_noticias


def brazil_journal(tema):

        options = Options()
        options.headless = False

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

        if tema == 'economia':

            url = 'https://braziljournal.com/categoria/economia/'

        elif tema == 'tech':
             
            url = 'https://braziljournal.com/categoria/tecnologia/'

        driver.get(url)

        todas_noticias = driver.find_element("xpath", '/html') 

        html_not = todas_noticias.get_attribute('outerHTML')

        driver.quit()

        soup = BeautifulSoup(html_not, 'html.parser')

        caixas_noticias = soup.find_all("figcaption", class_ = 'boxarticle-infos') 

        df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

        for i, noticia in enumerate(caixas_noticias):

            subtopico = noticia.find("p", class_ = 'boxarticle-infos-tag').text
            manchete = noticia.find("h2", class_ = 'boxarticle-infos-title').text
            link = noticia.find("h2", class_ = 'boxarticle-infos-title').a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'brazil_journal'

            if i == 5:

                break

        return df_noticias


def valor_economico(tema):

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if tema == "economia":

        url = 'https://valor.globo.com/financas/'

    elif tema == 'tech':

        url = 'https://valor.globo.com/empresas/'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    caixas_destaque = soup.find_all("div", class_ = 'highlight') 

    df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

    for i, noticia in enumerate(caixas_destaque):

        subtopico = noticia.find("h3").a.text
        manchete = noticia.find('h2').a['title']
        link = noticia.find("h2").a['href']

        df_noticias.loc[i, 'subtopico'] = subtopico
        df_noticias.loc[i, 'manchete'] = manchete
        df_noticias.loc[i, 'link'] = link
        df_noticias.loc[i, 'topico'] = tema
        df_noticias.loc[i, 'jornal'] = 'valor_economico'

        if i == 5:

            break

    return df_noticias


def fortune(tema):

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if tema == "economia":

        url = 'https://fortune.com/section/finance/'

    elif tema == 'tech':

        url = 'https://fortune.com/section/tech/'

    elif tema == 'ia':

        url = 'https://fortune.com/tag/artificial-intelligence/'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    caixas_destaque = soup.find_all("li", class_ = 'sc-faa25045-0 fBDziX') 

    df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

    for i, noticia in enumerate(caixas_destaque):

        if tema != 'ia':

            subtopico = noticia.find("div", class_ = 'sc-faa25045-2 jikDob').span.text
            manchete = noticia.find("div", class_ = 'sc-faa25045-2 jikDob').a.span.text
            link = noticia.find("div", class_ = 'sc-faa25045-2 jikDob').a['href']

        else:

            subtopico = noticia.find("div", class_ = 'sc-faa25045-2 jikDob').span.text
            manchete = noticia.find("div", class_ = 'sc-faa25045-2 jikDob').find_all('a')

            for m, manch in enumerate(manchete):

                if m == 1:
                    
                    manchete = manch.span.text
                    link = manch['href']


        df_noticias.loc[i, 'subtopico'] = subtopico
        df_noticias.loc[i, 'manchete'] = manchete
        df_noticias.loc[i, 'link'] = link
        df_noticias.loc[i, 'topico'] = tema
        df_noticias.loc[i, 'jornal'] = 'fortune'

        if i == 5:

            break

    return df_noticias


def wsj(tema):

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if tema == "economia":

        url = 'https://www.wsj.com/finance'

    elif tema == 'tech':

        url = 'https://www.wsj.com/tech'

    elif tema == 'ia':

        url = 'https://www.wsj.com/tech/ai'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    if tema == 'tech':

        caixas_destaque = soup.find_all("div", attrs={'data-testid': 'allesseh'}) 

        df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

        for i, noticia in enumerate(caixas_destaque):

            subtopico = '-'
            manchete = noticia.find('h3', class_ = 'css-fsvegl').a.span.p.text
            link = noticia.find('h3', class_ = 'css-fsvegl').a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'wsj'

            if i == 5:

                break

        return df_noticias

    elif tema == 'economia':

        df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

        caixas_destaque = soup.find_all("div", class_ = 'css-1yp7ne6') 

        for i, noticia in enumerate(caixas_destaque):

            subtopico = '-'
            manchete = noticia.find('h3', class_ = 'css-fsvegl').a.span.p.text
            link = noticia.find('h3', class_ = 'css-fsvegl').a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'wsj'

            if i == (len(caixas_destaque) - 1) or i == 5:
                
                i = i + 1
                break

        caixas_destaque = soup.find_all("div", class_ = 'css-18y1fei') 

        for _, noticia in enumerate(caixas_destaque):

            subtopico = '-'
            manchete = noticia.find('h3', class_ = 'css-fsvegl').a.span.p.text
            link = noticia.find('h3', class_ = 'css-fsvegl').a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'wsj'

            i = i + 1

            if i == 6:

                break

        return df_noticias

    elif tema == 'ia':

        caixas_destaque = soup.find_all("div", class_ = 'css-bdm6mo') 

        df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

        for i, noticia in enumerate(caixas_destaque):

            subtopico = '-'
            manchete = noticia.find('h3', class_ = 'css-fsvegl').a.span.p.text
            link = noticia.find('h3', class_ = 'css-fsvegl').a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'wsj'

            if i == 5:

                break

        return df_noticias


def ft(tema):

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if tema == "economia":

        url = 'https://www.ft.com/markets'

    elif tema == 'tech':

        url = 'https://www.ft.com/technology'

    elif tema == 'deep_dive':

        url = 'https://www.ft.com/deep-dive'

    driver.get(url)

    todas_noticias = driver.find_element("xpath", '/html') 

    html_not = todas_noticias.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    df_noticias = pd.DataFrame(columns=['manchete', 'subtopico', 'link', 'topico', 'jornal'], index=[0, 1, 2, 3, 4, 5])

    if tema != "deep_dive":

        noticia_principal = soup.find("div", attrs={'class':"o-teaser o-teaser--article o-teaser--top-story o-teaser--landscape o-teaser--has-image js-teaser"}) 

        try:
            
            subtopico = noticia_principal.find("div", attrs={'class':"js-teaser-standfirst-link"}).a.text

        except:

            subtopico = "-"

        manchete = noticia_principal.find("div", attrs={'class':'o-teaser__heading'}).a.text
        link = noticia_principal.find("div", attrs={'class':'o-teaser__heading'}).a['href']
        
        df_noticias.loc[0, 'subtopico'] = subtopico
        df_noticias.loc[0, 'manchete'] = manchete
        df_noticias.loc[0, 'link'] = "https://www.ft.com" + link
        df_noticias.loc[0, 'topico'] = tema
        df_noticias.loc[0, 'jornal'] = 'ft'

        i = 0

        noticia_gerais = (soup.find("div", attrs={'data-trackable':"top-stories-column-one"})).find_all("div", class_ = 'o-teaser__content')

        for _, noticia in enumerate(noticia_gerais):

            i = i + 1

            try:

                subtopico = noticia.find("div", attrs={'class':"o-teaser__meta"}).a.text

            except:

                subtopico = '-'

            manchete = noticia.find("div", attrs={'class':'o-teaser__heading'}).a.text
            link = noticia.find("div", attrs={'class':'o-teaser__heading'}).a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = "https://www.ft.com" + link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'ft'

            if i == 3:

                break

        noticia_opinião = soup.find("div", attrs={'data-trackable':'opinion-and-analysis'}).find_all("div", class_ = 'o-teaser__content')

        for _, noticia in enumerate(noticia_opinião):

            i = i + 1

            try:

                subtopico = noticia.find("div", attrs={'class':"o-teaser__meta"}).a.text

            except:

                subtopico = '-'

            manchete = noticia.find("div", attrs={'class':'o-teaser__heading'}).a.text
            link = noticia.find("div", attrs={'class':'o-teaser__heading'}).a['href']

            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'link'] = "https://www.ft.com" + link
            df_noticias.loc[i, 'topico'] = tema
            df_noticias.loc[i, 'jornal'] = 'ft'

            if i == 5:

                break

        return df_noticias
    
    else:

        editorial = soup.find_all("li", attrs={'class': 'o-teaser-collection__item o-grid-row'}) 

        i = 0

        for _, noticia in enumerate(editorial):

            if noticia.find("div", attrs={'class':"o-ads__outer"}) == None: #pulando linhas de anúncios

                subtopico = noticia.find("div", attrs={'class':"o-teaser__meta"}).a.text
                manchete = noticia.find("div", attrs={'class':'o-teaser__heading'}).a.text
                link = noticia.find("div", attrs={'class':'o-teaser__heading'}).a['href']

                df_noticias.loc[i, 'subtopico'] = subtopico
                df_noticias.loc[i, 'manchete'] = manchete
                df_noticias.loc[i, 'link'] = "https://www.ft.com" + link
                df_noticias.loc[i, 'topico'] = tema
                df_noticias.loc[i, 'jornal'] = 'ft'

                if i == 5:

                    break

                i = i + 1
        
        return df_noticias



def scraping_noticias():

    #br

    bj_e = brazil_journal('economia')
    bj_t = brazil_journal('tech')
    g1_e = g1_economia()
    g1_t = g1_tech()
    valor_e = valor_economico('economia')
    valor_t = valor_economico('tech')

    #gringo

    f_e = fortune('economia')
    f_t = fortune('tech')
    f_ia = fortune('ia')
    wsj_e = wsj('economia')
    wsj_t = wsj('tech')
    wsj_ia = wsj('ia')
    ft_e = ft('economia')
    ft_t = ft('tech')
    ft_dd = ft('deep_dive') 

    noticias = pd.concat([ft_e, ft_t, ft_dd], ignore_index=True)

    print(noticias)

    noticias.to_csv("noticias.csv", index = False)

if __name__ == "__main__":
    
    scraping_noticias()








