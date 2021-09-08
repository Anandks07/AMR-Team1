import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.graph_objects as go 
from dash.dependencies import Input, Output, State


app = dash.Dash()
dataset = pd.read_csv('NT.csv')                         # Give directory here
df = dataset[['symbol','open','high','low','close','date']]
dates = df['date']
def str_to_date(string):
	return string.split('-')
day = []
month =[]
year = []
for date in dates:
	a = str_to_date(date)
	year.append(int(a[0]))
	month.append(int(a[1]))
	day.append(int(a[2]))
df['day'] = day
df['month'] = month
df['year'] = year

fig = go.Figure(data=go.Ohlc(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']))

colors = {'background': '#00a2ff','text':'#111111'}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='OHLC DASHBOARD',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Team-1 Submission', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    
    html.Div(
    dcc.Graph(id='graph-with-all-symbols',figure=fig)
    ),
    
     html.H2(
    	children="Search the different stocks based on the symbols"),
    
    html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['symbol'].unique()],
        value='a')]),
        
    html.Div(
    children=dcc.Graph(
        id='Graph',
        figure=fig
    )),
    
    html.H2(
    	children = "Search stocks based on month and year"),
    
    html.Div(
    dcc.Dropdown(
                id='year',
                options=[{'label': i, 'value': i} for i in df['year'].unique()],
                value = 2021
            )),
    
    html.Div(
    	dcc.Dropdown(
    	id = 'month',
    	options = [{'label': i, 'value': i} for i in df['month'].unique()],
    	value = 1
    	)),
    
    html.Div(
    children=dcc.Graph(
        id='Graph-based-on-date',
        figure=fig
    )),	
    
    html.H2(
    	children='History'
    	),
    html.Div(children = '',id = 'show_history_symbol'),
    html.Div(children = '',id = 'show_history_date')
    
])

@app.callback(Output('Graph','figure'),Input('dropdown','value'))
def update_figure(symbol):
	filtered_df = df[df['symbol'] == symbol]
	fig = go.Figure(data=go.Ohlc(x=filtered_df['date'],open=filtered_df['open'],high=filtered_df['high'],low=filtered_df['low'],close=filtered_df['close']))
	fig.update_layout()
	return fig

history_symbol = []
@app.callback(Output('show_history_symbol','children'),Input('dropdown','value'))
def update_history(symbol):
	if symbol!= 'a' and symbol!=None:
		symbol = symbol + ' '
		history_symbol.insert(0,symbol)
	return history_symbol
@app.callback(Output('Graph-based-on-date','figure'),Input('year','value'),Input('month','value'))
def update_figure(year,month):
	filtered_df = df[df['year'] == year]
	filtered_df = df[df['month'] == month]
	fig = go.Figure(data=go.Ohlc(x=filtered_df['date'],open=filtered_df['open'],high=filtered_df['high'],low=filtered_df['low'],close=filtered_df['close']))
	fig.update_layout()
	return fig

history_date = []
@app.callback(Output('show_history_date','children'),Input('year','value'),Input('month','value'))
def update_history(year,month):
	date = str(month) + '-' + str(year) + ' '
	history_date.insert(0,date)
	return history_date

if __name__ == '__main__':
    app.run_server(debug=True)
