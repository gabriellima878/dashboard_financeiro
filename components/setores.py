import pandas as pd
from dash import Dash, html, dcc, dash_table, callback
from dash.dependencies import Input, Output
from app import *
from funcoes_dd import tabela_cotacao_setor_bolsa 

colunas_padrao = [{'name': 'Ticker', 'id': 'Ticker'},
                    {'name': 'Preço', 'id': 'Preço', 'type': 'numeric'},
                    {'name': 'Retorno', 'id': 'Retorno', 'type': 'numeric'}]

df_setores = pd.read_csv("setores.csv")
    
lista_setores = df_setores['SETOR'].unique()


layout = dbc.Row([

                dbc.Col([html.Div([dcc.Interval(
                                                            id='interval-component-setor-1',
                                                            interval=1*10000, 
                                                            n_intervals=0),

                    dcc.Dropdown(lista_setores, value = 'Madeira e Papel', id = 'escolher-setor-1', className = 'dcc-padrao',
                                                        style = {"background-color": 'black', 'color': 'white', 'margin-top': '24px',
                                                                 'margin-bottom': "13px"}),
                    dash_table.DataTable(
                                                        colunas_padrao,
                                                        id = 'setor-1',
                                                        style_header={
                                                                    'backgroundColor': '#222729',
                                                                    'fontWeight': 'bold',
                                                                    'border': '0px',
                                                                    'font-size': "12px",
                                                                    'color': '#D3D6DF'},
                                                                    
                                                        style_cell={'textAlign': 'center',
                                                                    'padding': '12px 8px',
                                                                    'backgroundColor': '#131516',
                                                                    'color': '#D3D6DF'
                                                                    },

                                                        style_data={ 'border': '0px',
                                                                    'font-size': "12px" },

                                                                    style_table={
                                                                    
                                                                    'borderRadius': '8px',
                                                                    "overflow": "hidden",
                                                                    'border': '2px solid #222729' 
                                                                },

                                                        style_data_conditional=[
                                                                {
                                                                'if': {
                                                                        'filter_query': '{Retorno} > 0',
                                                                        'column_id': 'Retorno'
                                                                    }, 
                                                                    'color': '#19C819',
                                                                    
                                                                },
                                                                {
                                                                'if': {
                                                                        'filter_query': '{Retorno} < 0',
                                                                        'column_id': 'Retorno'
                                                                    }, 
                                                                    'color': '#E50000'
                                                                }
                                                        ])

                                                ], style= {'margin-top': "13px"})

                ], md = 6),

                dbc.Col([html.Div([
                                        dcc.Interval(
                                                            id='interval-component-setor-2',
                                                            interval=1*10000, 
                                                            n_intervals=0),
                    dcc.Dropdown(lista_setores, value = 'Transporte', id = 'escolher-setor-2', className = 'dcc-padrao',
                                                        style = {"background-color": 'black', 'color': 'white', 'margin-top': '24px',
                                                                 'margin-bottom': "13px"}),
                    dash_table.DataTable(
                                                        colunas_padrao,
                                                        id = 'setor-2',
                                                        style_header={
                                                                    'backgroundColor': '#222729',
                                                                    'fontWeight': 'bold',
                                                                    'border': '0px',
                                                                    'font-size': "12px",
                                                                    'color': '#D3D6DF'},
                                                                    
                                                        style_cell={'textAlign': 'center',
                                                                    'padding': '12px 8px',
                                                                    'backgroundColor': '#131516',
                                                                    'color': '#D3D6DF'
                                                                    },

                                                        style_data={ 'border': '0px',
                                                                    'font-size': "12px" },

                                                                    style_table={
                                                                    
                                                                    'borderRadius': '8px',
                                                                    "overflow": "hidden",
                                                                    'border': '2px solid #222729' 
                                                                },

                                                        style_data_conditional=[
                                                                {
                                                                'if': {
                                                                        'filter_query': '{Retorno} > 0',
                                                                        'column_id': 'Retorno'
                                                                    }, 
                                                                    'color': '#19C819',
                                                                    
                                                                },
                                                                {
                                                                'if': {
                                                                        'filter_query': '{Retorno} < 0',
                                                                        'column_id': 'Retorno'
                                                                    }, 
                                                                    'color': '#E50000'
                                                                }
                                                        ])
                                                ], style= {'margin-top': "13px"})

                ], md = 6)
])


@app.callback(Output('setor-1', 'data'),
              [Input('interval-component-setor-1', 'n_intervals'),
               Input('escolher-setor-1', 'value')])

def update_metrics(n, setor):

    df_setor = tabela_cotacao_setor_bolsa(setor)
    df_setor['Retorno'] = df_setor['Retorno'].apply(lambda x: round(x , 2))
    df_setor['Preço'] = df_setor['Preço'].apply(lambda x: round(x , 2))
   
    return df_setor.to_dict("records")


@app.callback(Output('setor-2', 'data'),
              [Input('interval-component-setor-2', 'n_intervals'),
               Input('escolher-setor-2', 'value')])

def update_metrics(n, setor):

    df_setor = tabela_cotacao_setor_bolsa(setor)
    df_setor['Retorno'] = df_setor['Retorno'].apply(lambda x: round(x , 2))
    df_setor['Preço'] = df_setor['Preço'].apply(lambda x: round(x , 2))
   
    return df_setor.to_dict("records")










