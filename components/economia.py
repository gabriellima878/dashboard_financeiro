from app import *
from dash import Dash, html, dcc, dash_table, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from funcoes_dd import fazer_grafico_di, fazer_tabela_di, grafico_divida_pib, grafico_dolar, grafico_inflacao, info_divida_pib, info_dolar, info_inflacao

lista_indicadores = ['DI', 'INFLAÇÃO', 'DÓLAR', 'DÍVIDA/PIB']
lista_periodos = ['1 ano', '3 anos', '5 anos', '10 anos']

layout = html.Div([
    
            dbc.Row([

                dbc.Col([

                    dbc.Row([

                        dbc.Col(html.Div(dcc.Dropdown(lista_indicadores, value = 'DI', id = 'indicador-economico-graph', className = 'dcc-padrao',
                                                                style = {"background-color": 'black', 'color': 'white'}))),
                        dbc.Col(dcc.Dropdown(lista_periodos, value = '3 anos', id = 'indicador-economico-periodo', className = 'dcc-padrao',
                                                                style = {"background-color": 'black', 'color': 'white'}))

                    ]),
                    dbc.Row(dcc.Graph(style={"width": "100%", 'height': "302px", 'margin-top': '16px', 'width': '90%', 
                                                             'border-radius':'8px',
                                                             'background-color': '#131516', 'border': "2px solid #212946"}, 
                                                             id ='grafico_economia'), style={'display': 'flex', 'justify-content': 'center'})
                ])
            ]),

            dbc.Row([

                html.H3(children="Estatísticas", className='categorias-dash', style = {'width': '96%'})

            ], style= {'display': 'flex', 'justify-content': 'center'}),

            dbc.Row([

                html.Div(dcc.Dropdown(lista_indicadores, value = 'DI', id = 'indicador-economico-tabela', className = 'dcc-padrao',
                                                                style = {"background-color": 'black', 'color': 'white', 'margin-top': "9px"}),         
                                                                style = {"width": "50%"}),

                html.Div(id = 'estatisticas-economicas', style= {'margin-top': "-10px"})

            ])
                                                       

], style= {'margin-top': '24px'})



@app.callback(Output('grafico_economia', 'figure'),
              [Input('indicador-economico-graph', 'value'),
               Input('indicador-economico-periodo', 'value')]) #cada input representa um argumento da função. Reconhece automatico os inputs. 

def update_metrics(indicador, periodo):

    if indicador == "DI":

        fig = fazer_grafico_di(periodo)

    elif indicador == 'INFLAÇÃO':

        fig = grafico_inflacao(periodo)

    elif indicador == 'DÓLAR':

        fig = grafico_dolar(periodo)

    elif indicador == 'DÍVIDA/PIB':

        fig = grafico_divida_pib(periodo)

    return fig

@app.callback(Output('estatisticas-economicas', 'children'),
              Input('indicador-economico-tabela', 'value'))

def update_metrics(indicador):

    if indicador == "DI":

        tabela = fazer_tabela_di()

    elif indicador == 'INFLAÇÃO':

        tabela = info_inflacao()

    elif indicador == 'DÓLAR':

        tabela = info_dolar()

    elif indicador == 'DÍVIDA/PIB':

        tabela = info_divida_pib()


    return [dash_table.DataTable(columns=[{"name": i, "id": i} for i in tabela.columns],
                                 data = tabela.to_dict('records'),
                                    style_header={'display': 'none'},
                                    style_cell={'textAlign': 'center',
                                                'padding': '12px 8px',
                                                'backgroundColor': '#333E66',
                                                'color': '#D3D6DF'
                                                },

                                    style_data={ 'border': '0px',
                                                'font-size': "12px" },

                                                style_table={
                                                
                                                'borderRadius': '0px',
                                                'overflow': 'hidden'
                                            },
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'column_id': 'ignore_1',
                                            },
                                            'backgroundColor': '#212946',
                                            'fontWeight': 'bold',
                                            'borderRadius': '0px',
                                            'font-size': "12px",
                                            'color': '#D3D6DF'
                                        }]
                                                                                )]



















