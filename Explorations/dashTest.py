from dash import Dash, html
from dash_bootstrap_components.theme import BOOTSTRAP

def main():
    app = Dash()
    app.title = "Medal dashboard"
    app.layout = html.Div([
        html.H1("Test av dash!"),
        html.P("Det fungerade!")
    ])
    app.run()

if __name__ == "__main__":
    main()