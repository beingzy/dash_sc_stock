""" dashboard to track daily close stock price of 
    a selection of companies in semiconductor industry

    Author: Yi Zhang <beingzy@gmail.com>
    Date: 2017/06/25
"""
import dash
from dash.dependencies import Input, Output 
import dash_core_components as dcc 
import dash_html_components as html 

from pandas_datareader import data as web 
from datetime import datetime as dt 

app = dash.Dash('Semiconductor-Companies')

app.layout = html.Div([
	dcc.Dropdown(
		id = 'stock-dropdown',
		options = [
		    {'label': 'AMD', 'value': 'AMD'},
		    {'label': 'Nvidia', 'value': 'NVDA'},
		    {'label': 'Intel', 'value': 'INTC'},
		],
	    value = 'AMD'
	),
	dcc.Graph(id='stock-graph')
], style={'width': '600'})


@app.callback(Output('stock-graph', 'figure'), [Input('stock-dropdown', 'value')])
def update_graph(selected_dropdown_value):
	# read stock price data from google-finance
	df = web.DataReader(
		selected_dropdown_value, 
		'google',
		dt(2017, 1, 1),
		dt.now()
	)

	return {
	    'data': [{
	        'x': df.index, # date
	        'y': df['Close'] # close price 
	    }],
	    'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
	}

# plotly css styling sheets
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgp.css'})

if __name__ == '__main__':
	app.run_server()