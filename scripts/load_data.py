import pandas as pd

def load_data():
    df1 = pd.read_csv('../data/2024-06-28 (2mes) Web3 Founders.csv')
    df2 = pd.read_csv('../data/2024-06-28 (2mes) HUMANS_DAO.csv')
    df3 = pd.read_csv('../data/2024-06-28 (2mes) KRA_WEB_3.csv.csv')
    df4 = pd.read_csv('../data/2024-06-28 (2mes) .csv')
    df5 = pd.read_csv('../data/2024-06-28 (2mes) startech_networking.csv')
    df6 = pd.read_csv('../data/2024-06-28 (2mes) startech_networking.csv')
    return df1, df2, df3
