import pandas as pd

def load_data():
    df1 = pd.read_csv('../data/humans_dao.csv')
    df2 = pd.read_csv('../data/w3x_founders_investors.csv')
    df3 = pd.read_csv('../data/startech_networking.csv')
    return df1, df2, df3
