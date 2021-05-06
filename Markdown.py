import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codeopen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

markdown_text = '''
### 사나이 가는 길 꽃길만 있을 수 없다!!

* 화이팅!!
* 아자아자!!

'''

app.layout = html.Div([
    dcc.Markdown(children = markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug = True)