import pandas as pd
from sqlalchemy import create_engine


class Export:
    def __init__(self):
        self.csv_file_path = "egrid2020_data.xlsx"
        self.engine = create_engine('sqlite:///../app/csv_test.db')

    def convert_to_percent_string(self, value):
        return '{}%'.format(value * 100)

    def export(self):
        convertor = {
            'PLGSPR': self.convert_to_percent_string,
            'PLNCPR': self.convert_to_percent_string,
            'PLCYPR': self.convert_to_percent_string,
            'PLCNPR': self.convert_to_percent_string,
        }
        data_df = pd.read_excel(self.csv_file_path, skiprows=1, sheet_name='PLNT20', converters=convertor)
        data_df.fillna(0, inplace=True)
        data_df.to_sql('e_grid_plant', con=self.engine, index=False, if_exists='replace')

    def export_region(self):
        data_df = pd.read_excel(self.csv_file_path, sheet_name='NRL20')
        new_header = data_df.iloc[0]
        data_df = data_df[1:]
        data_df.columns = new_header.str.lower()
        data_df.fillna(0, inplace=True)
        data_df.to_sql('nerc_region', con=self.engine, index=False, if_exists='replace')

    def alter(self):
        with self.engine.connect() as con:
            con.execute("ALTER TABLE e_grid_plant ADD PRIMARYKEY seqplt20")

        return True


if __name__ == '__main__':
    exp = Export()
    exp.export()
    # exp.alter()
