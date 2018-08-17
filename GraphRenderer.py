import dash_core_components as dcc
import dash_html_components as html

class GraphRenderer:

    def __init__(self):
        self.colors = {
            'background': '#ffffff',
            'text': '#210042'
        }

    def getLayout(self, x_values, y_values):
        return html.Div(
            children=[self.getHeading(), self.getExplanationDiv(), self.getGraph(x_values, y_values)],
            style = {
                'backgroundColor': self.colors['background']
            }
        )

    def getHeading(self):
        return html.H1(
            children='Code Clinic 1: Weather Stats',
            style = {
                'textAlign': 'center',
                'color': self.colors['text']    
            }
        )

    def getExplanationDiv(self):
        return html.Div(
            children='Some div with text',
            style = {
                'textAlign': 'center',
                'color': self.colors['text']
            }
        )

    def getGraph(self, x_values, y_values):
        return dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'SF'},
                    # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Graph Heading',
                    'plot_bgcolor': self.colors['background'],
                    'paper_bgcolor': self.colors['background'],
                    'font': {
                        'color': self.colors['text']
                    }
                }
            }
        )