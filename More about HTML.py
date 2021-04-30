# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['htts://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

colors = {
    'background' : '#111111',
    'text' : '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]        
})

fig = px.bar(df, x = 'Fruit', y = 'Amount', color = 'City', barmode = 'group')

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)

# html.H1('Hello Dash', style={'textAlign' : 'center', 'color' : '#7FDBFF})는 <h1 style='text-align: center; color: #7FDBFF">Hello Dash</h1>와 같다.
# 진짜 HTML에서 style은 ;로 구분이 되는데, dash는 dictionary를 쓰면 된다.
# dash에서 style dictionary는 camelCased 명명법을 쓴다. 그래서 예를 들면, text-align이 textAlign으로 된다.
# HTML class 속성은 dash에선 className이다.
app.layout = html.Div(style = {'backgroundColor': colors['background']}, children = [
    html.H1(
        children = 'Hello Dash',
        style = {
            'textAlign' : 'center',
            'color' : colors['text']
        }
    ),

    html.Div(children = 'Dash : A web application framework for Python', style = {
        'textAlign' : 'center',
        'color' : colors['text']
    }),

    dcc.Graph(
        id = 'example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)