import pandas as pd

FILE_NAME_STOCK_DATA = 'stocks_data.xlsx'
FILE_NAME_TEMP_FII_AND_BDR_DATA = 'fiis_and_bdrs_data.xlsx'


def load_assets_data():
    df_stock_data = load_stock_data()
    df_fii_and_bdr_data = TEMP_load_fii_and_bdr_data()

    #TODO: juntar os dois dfs
    df_assets_data = pd.concat([df_stock_data, df_fii_and_bdr_data])
    df_assets_data.reset_index(drop=True, inplace=True)

    return df_assets_data

def load_stock_data():
    df_stock_data = pd.read_excel(FILE_NAME_STOCK_DATA)

    return df_stock_data

def TEMP_load_fii_and_bdr_data():
    df_fii_and_bdr_data = pd.read_excel(FILE_NAME_TEMP_FII_AND_BDR_DATA)

    df_fii_and_bdr_data = df_fii_and_bdr_data.loc[df_fii_and_bdr_data['class'] != 'Stock', :]

    return df_fii_and_bdr_data