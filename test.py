import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('sqlite:///csv_test.db')

csv_file_path = "export/egrid2020_data.xlsx"
data_df = pd.read_excel(csv_file_path, sheet_name='PLNT20')
new_header = data_df.iloc[0]
data_df = data_df[1:]
data_df.columns = new_header.str.lower()
data_df.to_sql('e_grid_plant', con=engine, index=True, index_label='id', if_exists='replace')
