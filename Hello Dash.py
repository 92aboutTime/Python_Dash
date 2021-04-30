# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
# dash html_components library는 HTML의 모든 component를 가지고 있다.
# html.H1(children = "asd") 는 <H1>asd</H1>과 같다.
import plotly.express as px
import pandas as pd

external_stylesheets = ['https"//codepen.io/chriddyp/pen/bWLwgP.css']
# 위의 코드를 통해 custom CSS stylesheet를 default styles of the elments로 사용할 수 있다.

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

df = pd.DataFrame({
    "Fruit" : ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount" : [4, 1, 2, 2, 4, 5],
    "City" : ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y = "Amount", color = "City", barmode = "group")

# layout은 tree of components(html.Div, dcc.Graph 등)로 구성된다.
app.layout = html.Div(children = [
    html.H1(children = 'Hello Dash'),
    # dash는 선언적(declarative) 특성을 가진다. 그런데 children은 특별하다.
    # html.H1(children = 'asd')를 html.H1('asd')로 적으면 똑같은 결과가 나타난다.
    # dash는 가장 처음에 있는 파라미터를 children으로 인식한다.
    # children의 값에는 strung, a number, a single component, or a list of components들이 올 수 있다.

    html.Div(children = '''
    Dash: A web application framewordk for Python.
    '''),

    dcc.Graph(
        id = 'example-graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)