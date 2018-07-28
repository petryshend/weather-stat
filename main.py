from datetime import datetime
from pprint import pprint
from DataGetter import DataGetter

if __name__ == '__main__':
    date_from = datetime(2011, 1, 1, 0, 5, 30)
    date_to = datetime(2016, 1, 1, 0, 30, 0)

    data_getter = DataGetter()
    res = data_getter.get_data(date_from, date_to)
    pprint(len(res))
