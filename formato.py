import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback
from components import ativos_ao_vivo, grafico_ativos, setores, economia, noticias
from app import *

tab_painel = html.Div([

    dbc.Row(

        [dbc.Col(html.H2(children = "Mercado ao vivo", className='subtitulos-dash'), md = 8),
        dbc.Col(html.H2(children = "Economia", className='subtitulos-dash'), md = 4)]
    ),
    dbc.Row(

        [dbc.Col(
            [
                dbc.Row(ativos_ao_vivo.layout),
                dbc.Row(grafico_ativos.layout),
            ]

        ),
         dbc.Col(setores.layout),
         dbc.Col(economia.layout),]


    ),

])


tab_noticias =  dbc.Row(

    [
        dbc.Col(noticias.layout_brasil, style= {'margin': '24px 0px 0px 150px'}),
        dbc.Col(noticias.layout_mundo, style= {'margin': '24px 0px 0px 0px'})
    ]
)



app.layout = dbc.Container(

    dbc.Row(
        dbc.Col(
            dbc.Tabs([

                dbc.Tab(tab_painel, label = 'Painel'),
                dbc.Tab(tab_noticias, label = 'Notícias')

                      ]), style = {'margin': '8px'}
        )
    ), fluid = True, style = {'height': '100vh', 'width': '100%', 'padding': "25px 25px 0px 25px", 'background-color': '#131516'}
)





if __name__ == "__main__":
    app.run(debug = False, port = 8051)

