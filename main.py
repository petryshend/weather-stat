from datetime import datetime
from pprint import pprint
from DataGetter import DataGetter
from GraphRenderer import GraphRenderer
import dash

if __name__ == '__main__':
    date_from = datetime(2013, 1, 1, 0, 0, 0)
    date_to = datetime(2013, 1, 1, 23, 0, 0)

    data_getter = DataGetter()
    data = data_getter.get_data(date_from, date_to)

    dates_x = [row[0] for row in data]
    values_y = [row[1] for row in data]

    graph_renderer = GraphRenderer()

    app = dash.Dash()
    app.layout = graph_renderer.getLayout(dates_x, values_y)
    
    app.run_server(debug=True)
