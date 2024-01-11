import pandas as pd , os
from openpyxl import load_workbook as lw ,Workbook as wk


def getLookUpTables():
    file_path = os.path.join(os.getcwd(),'Generate Sales.xlsm')
    wk =lw(file_path)
    sht_names =wk.sheetnames
    # loop through the sheets names
    print(sht_names)
    for sht in sht_names:
        if 'stores'.lower() in sht.lower():
            df_store = pd.read_excel(file_path,sheet_name = sht)
            print(df_store.shape)
        elif 'product'.lower() in sht.lower():
            df_product = pd.read_excel(file_path,sheet_name = sht)
            print(df_product.shape)
        elif 'customers'.lower() in sht.lower():
            df_customer = pd.read_excel(file_path,sheet_name = sht)
            print(df_customer.shape)
        

    df_list = [{
                 "store":df_store, 
                 "product":df_product, 
                 "customer":df_customer}
              ]

    return df_list[0]


print(getLookUpTables())