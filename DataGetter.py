import csv
from datetime import datetime


class DataGetter:
    filename_format = 'resources/Environmental_Data_Deep_Moor_%d.txt'
    date_format = "%Y_%m_%d %H:%M:%S"

    def get_data(self, date_from, date_to):
        res_data = []
        for year in [2012, 2013, 2014, 2015]:
            if year < date_from.year or year > date_to.year:
                continue
            with open(self.filename_format % year, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
                next(reader, None) # skip header
                for row in reader:
                    date_row = datetime.strptime(row[0], self.date_format)
                    if date_from.timestamp() < date_row.timestamp() < date_to.timestamp():
                        res_data.append((row[0], row[2]))

        return res_data
