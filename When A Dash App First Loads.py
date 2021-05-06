import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import State, Input, Output


app = dash.Dash()

app.layout = html.Div([
    html.Button(id = 'button-1', children = 'EXCUTE CALLBACK'),
    html.Div(id = 'first_output_1', children = 'callback not excuted'),
    html.Div(id = 'second_output_1', children = 'callback not excuted')
])

@app.callback(
    Output('first_output_1', 'children'),
    Output('second_output_1', 'children'),
    Input('button-1', 'n_clicks')
)
def change_text(n_clicks):
    return 'n_clicks is ' + str(n_clicks), 'n_clicks is ' + str(n_clicks)

if __name__ == '__main__':
    app.run_server(debug = True)