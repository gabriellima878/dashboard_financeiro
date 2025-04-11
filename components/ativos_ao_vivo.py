import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback
from dados_mt5 import puxando_cotacoes, maiores_altas, maiores_baixas, gerar_lista_principais
import pandas as pd
from app import *
from dash.dependencies import Input, Output

comp_ibov = pd.read_csv('comp_ibov.csv')
tickers_ibov = comp_ibov['codigos']

colunas_padrao = [{'name': 'Ticker', 'id': 'Ticker'},
                    {'name': 'Preço', 'id': 'Preço', 'type': 'numeric'},
                    {'name': 'Retorno', 'id': 'Retorno', 'type': 'numeric'}]

layout =  dbc.Row([dcc.Interval(
                                                            id='interval-component',
                                                            interval=1*1000, # in milliseconds
                                                            n_intervals=0),            
                        
                    dbc.Col([

                                html.H3(children="Principais ativos", className='categorias-dash'),
                                html.Div([
                                                    dash_table.DataTable(

                                                        colunas_padrao,
                                                        id = 'cotacoes-tempo-real',
                                                        style_header={
                                                                    'backgroundColor': '#333E66',
                                                                    'fontWeight': 'bold',
                                                                    'border': '0px',
                                                                    'font-size': "12px",
                                                                    'color': '#D3D6DF',
                                                                    "borderRadius": "8px"},
                                                                    
                                                        style_cell={'textAlign': 'center',
                                                                    'padding': '12px 8px',
                                                                    'backgroundColor': '#212946',
                                                                    "borderRadius": "8px",
                                                                    'color': '#D3D6DF'
                                                                    
                                                                    },

                                                        style_data={ 'border': '0px',
                                                                    'font-size': "12px",
                                                                        },

                                                        style_table={
                                                                    
                                                                    'borderRadius': '8px',
                                                                    'overflow': 'hidden'
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
                                                                ]),

            
                                                            ], style= {'margin-top': "13px"})
                                

                    ]),
                    dbc.Col([

                        dbc.Row([dcc.Interval(
                                                            id='interval-component-altas',
                                                            interval=1*5000, # in milliseconds
                                                            n_intervals=0), 

                                html.Div(children = [
                                        
                                        html.H2(children="Maiores altas Ibovespa", className='categorias-dash'),
                                        html.Div([
                                                                dash_table.DataTable( 
                                                                    colunas_padrao,
                                                                    id = 'maiores_altas',
                                                                    style_header={
                                                                                'backgroundColor': '#333E66',
                                                                                'fontWeight': 'bold',
                                                                                'border': '0px',
                                                                                'font-size': "12px",
                                                                                'color': '#D3D6DF'},
                                                                                
                                                                    style_cell={'textAlign': 'center',
                                                                                'padding': '12px 8px',
                                                                                'backgroundColor': '#212946',
                                                                                'color': '#D3D6DF'
                                                                                },

                                                                    style_data={ 'border': '0px',
                                                                                'font-size': "12px" },

                                                                                style_table={
                                                                                
                                                                                'borderRadius': '8px',
                                                                                'overflow': 'hidden'
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
                                                                    ]
                                                                  

                                                                                )
                                                ], style= {'margin-top': "13px"})

                        ])]),
                        dbc.Row([dcc.Interval(
                                                            id='interval-component-baixas',
                                                            interval=1*5000, # in milliseconds
                                                            n_intervals=0), 

                                html.Div(children = [
                                        
                                        html.H2(children="Maiores baixas Ibovespa", className='categorias-dash'),
                                        html.Div([
                                                    dash_table.DataTable(
                                                        colunas_padrao,
                                                        id = 'maiores_baixas',
                                                        style_header={
                                                                    'backgroundColor': '#333E66',
                                                                    'fontWeight': 'bold',
                                                                    'border': '0px',
                                                                    'font-size': "12px",
                                                                    'color': '#D3D6DF'},
                                                                    
                                                        style_cell={'textAlign': 'center',
                                                                    'padding': '12px 8px',
                                                                    'backgroundColor': '#212946',
                                                                    'color': '#D3D6DF'
                                                                    },

                                                        style_data={ 'border': '0px',
                                                                    'font-size': "12px" },

                                                                    style_table={
                                                                    
                                                                    'borderRadius': '8px',
                                                                    'overflow': 'hidden'
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
                                                        ]
                                                        

                                                                    )
                                                ], style= {'margin-top': "13px"})

                        ])])

                    ])])




@app.callback(Output('cotacoes-tempo-real', 'data'),
              Input('interval-component', 'n_intervals'))

def update_metrics(n):

    tickers_escolhidos = gerar_lista_principais()

    df_ao_vivo = puxando_cotacoes(tickers_escolhidos, principal = True)

    df_ao_vivo['Retorno'] = df_ao_vivo['Retorno'].apply(lambda x: round(x , 2))
    df_ao_vivo.iloc[1, 1] = df_ao_vivo.iloc[1, 1]/1000
    df_ao_vivo.iloc[0, 0] = "IBOV"
    df_ao_vivo.iloc[1, 0] = "DÓLAR"
   
    return df_ao_vivo.to_dict("records")


@app.callback(Output('maiores_baixas', 'data'),
              Input('interval-component-baixas', 'n_intervals'))

def update_metrics(n):

    baixas = maiores_baixas(tickers_ibov)
    baixas['Retorno'] = baixas['Retorno'].apply(lambda x: round(x , 2))
    baixas['Preço'] = baixas['Preço'].apply(lambda x: round(x , 2))
    
    return baixas.to_dict("records")

@app.callback(Output('maiores_altas', 'data'),
              Input('interval-component-altas', 'n_intervals'))

def update_metrics(n):

    altas = maiores_altas(tickers_ibov)
    altas['Retorno'] = altas['Retorno'].apply(lambda x: round(x , 2))
    altas['Preço'] = altas['Preço'].apply(lambda x: round(x , 2))

    return altas.to_dict("records")

















