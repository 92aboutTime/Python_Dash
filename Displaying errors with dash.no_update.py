import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import State, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.P('Enter a composite number to see its prime factors'),
    dcc.Input( id = 'num', type = 'number', debounce = True, min=1, step =1),
    html.P(id = 'err', style = {'color' : 'red'}),
    html.P(id = 'out')
])

@app.callback(
    Output('out', 'children'),
    Output('err', 'children'),
    Input('num', 'value')
)
def show_factor(num):
    if num is None:
        raise dash.exceptions.PreventUpdate
    
    factors = prime_factors(num)
    if len(factors) == 1:
        return dash.no_update, '{} is prime!'.format(num)
    
    return '{} is {}'.format(num, ' * '.join(str(n) for n in factors)), ''

def prime_factors(num):
    n, i, out = num, 2, []
    while i * i <= n:
        if n % i == 0:
            n = int(n / i)
            out.append(i)
        else:
            i += 1 if i == 2 else 2
    out.append(n)
    return out

if __name__ == '__main__':
    app.run_server(debug=True)