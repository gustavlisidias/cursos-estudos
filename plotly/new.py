from dash import dash, html, dcc
from sympy import symbols, diff
import numpy as np

def get_vetor():
    x, y = symbols('x, y', real=True)   # criando variaveis
    f = 2*x + y                         # definindo função
    v = [diff(f, x), diff(f, y)]        # vetor
    return v

app = dash.Dash()

x = np.arange(-10, 10.5, 0.5)       # -10 à 10 pulando de 0.5
r1 = x - 1                          # primeira restrição
r2 = (12 - 3*x ) / 2                # segunda restrição
r3 = (3 - 2*x) / 3                  # terceira restrição
r4 = (9 + 2*x) / 3                  # quarta restrição

app.layout = html.Div([
    html.H1("Hello Dash"),
    html.Div("Dash - A data product development framework from plotly"),

    dcc.Graph(
        id = 'sample-graph',
        figure = {
            'data'      : [
                {'x': x, 'y': r1,'name': 'Restrição: x - y >= 1'},
                {'x': x, 'y': r2,'name': 'Restrição: 3x + 2y <= 12'},
                {'x': x, 'y': r3,'name': 'Restrição: 2x + 3y >= 3'},
                {'x': x, 'y': r4,'name': 'Restrição: -2x + 3y = 9'},
                {'x': [0, int(get_vetor()[0])], 'y': [0, int(get_vetor()[1])],'name': 'Vetor'},
            ],
            'layout'    : {'title': 'Simple Line Chart'}
        }
    )

])

if __name__ == '__main__':
    app.run_server(port=8200, debug=True)