from dash import html,dcc
# from tabs.eda_tab import eda_tab
# from tabs.about_us_tab import about_us_tab
# from tabs.rebalancing_tab import rebalancing_tab
# from tabs.intro_tab import intro_tab
# from tabs.rebalance_strategy_tab import rebalance_strategy_tab
# from tabs.conclusion_tab import conclusion_tab
# from tabs.cluster_tab import cluster_tab
from PIL import Image

b1 = html.Button('Button1', id = 'play-button')
tabs = dcc.Tabs(id = 'tab_bar',value = 'intro_tab', children = [
                                                                dcc.Tab(label = 'Intro', value = 'intro_tab'),
                                                                dcc.Tab(label = 'EDA', value = 'eda_tab'),
                                                                dcc.Tab(label = 'Clustering', value = 'clustering_tab'),
                                                                dcc.Tab(label = 'Rebalancing', value = 'rebalancing_tab')
    ])

# tabs = dcc.Tabs(id="tabs-example-graph", children=[intro_tab,
                                                    # eda_tab,
                                                    # cluster_tab,
                                                    # rebalancing_tab,
                                                    # rebalance_strategy_tab,
                                                    # conclusion_tab,
                                                    # # about_us_tab
                                                    # ],
                                                    # value='intro')

layout = html.Div([
    html.H1('Citi Bike Capstone Project'),
    tabs,
    html.Div(id='content')

])
