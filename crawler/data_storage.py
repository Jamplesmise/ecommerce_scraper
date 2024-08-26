import pandas as pd
from sqlalchemy import create_engine
from config.settings import DATABASE_URI, ENGINE_OPTIONS

engine = create_engine(DATABASE_URI, **ENGINE_OPTIONS)
COLUMNS = ['dataclass', 'datasource', 'keyname', 'name', 'price', 'pCurrency', 'minValue', 'unit', 'jumpUrl',
           'location', 'category', 'fromsource', 'fullProviderName', 'createdAt']


def save_data_to_db(df):
    df.to_sql('product_summary', con=engine, if_exists='append', index=False)


def save_data_to_excel(df, file_path):
    df.to_excel(file_path, index=False)
