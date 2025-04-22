# 📊 Painel de Dados Financeiros

Este projeto é uma aplicação desenvolvida em Python que coleta, trata e exibe dados financeiros em tempo real utilizando bibliotecas como **Dash**, **MetaTrader 5**, **Selenium** e **Pandas**. Ele oferece uma interface interativa para visualização de:

- Cotações ao vivo
- Gráficos de ativos
- Indicadores macroeconômicos
- Notícias do mercado
- Análise por setores da B3

---

## 📋 Funcionalidades

### ✅ Painel de Mercado ao Vivo
- Exibição de cotações em tempo real (via MetaTrader 5)
- Gráficos de candlestick para ações selecionadas
- Ranking de maiores altas e baixas do Ibovespa

### 📈 Indicadores Econômicos
- Curva de juros (DI) atual e histórica
- Gráficos de inflação (IPCA, IGP-M)
- Evolução da dívida/PIB e do dólar
- Tabelas-resumo com variação mensal, anual e acumulada

### 🗞️ Notícias Financeiras e Tecnológicas
- Webscraping automatizado de fontes como:
  - G1
  - Valor Econômico
  - Brazil Journal
  - WSJ
  - Fortune
  - Financial Times
- Organização por temas e regiões: Brasil e Mundo

### 🏢 Setores da Bolsa
- Exibição de ações agrupadas por setor
- Tabela de cotações setoriais com destaque para liquidez

---

## 🛠️ Tecnologias Utilizadas

### Frontend
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Plotly](https://plotly.com/)

### Backend
- [MetaTrader 5](https://www.metatrader5.com/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [python-bcb](https://pypi.org/project/python-bcb/)

### Auxiliares
- `datetime`, `pytz`, `zipfile`, `os`, `time`, `csv`, `parquet`, `webdriver-manager`

---

## 📂 Estrutura do Projeto

> Exemplo da estrutura do projeto no VSCode:
> ![estrutura](./2c5859a5-0396-4fe0-8342-1cb1307a15dd.png)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. **Python 3.10+**
2. **Google Chrome** instalado (utilizado pelo Selenium)
3. **MetaTrader 5** instalado e com login ativo (credenciais no `dados_mt5.py`)
4. Instalar as dependências com:
   ```bash
   pip install -r requirements.txt
   ```

---

### Execução

1. **Atualizar os dados** (coleta + processamento):
   ```bash
   python rotinas.py
   ```

2. **Rodar o servidor local (Dashboard):**
   ```bash
   python formato.py
   ```

3. **Acessar no navegador:**
   ```
   http://127.0.0.1:8051
   ```

---

## ⚠️ Observações

- **XPath quebrado:** Se algum scraping falhar, revise o XPath da página no navegador.
- **Arquivos gerados:** CSVs e `.parquet` são salvos automaticamente na raiz do projeto.
- **Dependência de fontes externas:** Sites como B3 e jornais online podem alterar suas estruturas.

---

## 👨‍💻 Autor

Gabriel Lima  
[LinkedIn](#https://www.linkedin.com/in/gabriel-pereira-lima/) | [Instagram](#https://www.instagram.com/cga.gabriellima/)

---

## 📝 Licença

Este projeto é de uso interno e não possui licença pública.
