import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("Enter Your Name:"),
    dcc.Input(id='input-name', type='text', placeholder='Enter your name'),
    html.Div(id='output-hello')
])

# Define callback to update the output div with the greeting message
@app.callback(
    Output('output-hello', 'children'),
    [Input('input-name', 'value')]
)
def update_output(name):
    if name is None:
        return html.Div("Hello")
    else:
        return html.Div(f"Hello {name}")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
