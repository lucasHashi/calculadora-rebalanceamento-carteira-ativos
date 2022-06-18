import pandas as pd

FILE_NAME_IN_EXCEL_TEMP_FIIS_AND_BDRS = 'fiis_and_bdrs_original_data.xlsx'
FILE_NAME_OUT_EXCEL_TEMP_FIIS_AND_BDRS = 'fiis_and_bdrs_temp.xlsx'


def main():
    df_fiis_and_bdrs = get_excel_data()

    df_fiis_and_bdrs.to_excel(FILE_NAME_OUT_EXCEL_TEMP_FIIS_AND_BDRS)


def get_excel_data():
    df_fiis_and_bdrs = pd.read_excel(FILE_NAME_IN_EXCEL_TEMP_FIIS_AND_BDRS)


if __name__ == "__main__":
    main()