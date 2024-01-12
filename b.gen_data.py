import pandas as pd , os
from openpyxl import load_workbook as lw ,Workbook as wk
from datetime import date as dt
from datetime import datetime, date as dt
from dateutil.relativedelta import relativedelta
import random as rd


no_days = 2
result_folder = r"C:\Users\edata\project\01.salesdata\Report"

def getDate(x):
    today = dt.today()
    past_date =today- relativedelta(days = x)

    return past_date

def getPID(df):
    min_pid = df["Product_id"].min()
    max_pid = df["Product_id"].max()
    val = rd.randint(min_pid, max_pid)
    #this gets the price
    filt = df[df["Product_id"] == val]
    price = filt["Price"].iloc[0]
    
    return [val, price]

def getCusId(df):
    min_pid = df["Product_id"].min()
    max_pid = df["Product_id"].max()
    val = rd.randint(min_pid, max_pid)
    #this gets the price
    filt = df[df["Product_id"] == val]
    price = filt["Price"].iloc[0]
    
    return [val, price]


def getLookUpTables():
    file_path = os.path.join(os.getcwd(),'Generate Sales.xlsm')
    wk =lw(file_path)
    sht_names =wk.sheetnames
    # loop through the sheets names
    for sht in sht_names:
        if 'stores'.lower() in sht.lower():
            df_store = pd.read_excel(file_path,sheet_name = sht)
        elif 'product'.lower() in sht.lower():
            df_product = pd.read_excel(file_path,sheet_name = sht)
        elif 'customers'.lower() in sht.lower():
            df_customer = pd.read_excel(file_path,sheet_name = sht)

    df_list = [{
                 "store":df_store, 
                 "product":df_product, 
                 "customer":df_customer}
              ]

    return df_list[0]


def generateData():
    days = no_days
    lkup_tables = getLookUpTables()

    for day in range(1,days+1):
        transaction_id_list= []
        transaction_date_list =[]
        str_id_list = []
        product_id_list = []
        price_list = []
        qty_list = []
        total_list = []
        cus_id_list = []

        d_date = getDate(day)
        day_of_week = d_date.strftime("%A")
        
        df_store = lkup_tables["store"]
        df_product = lkup_tables["product"]
        # loop through each store
        for _,str in df_store.iterrows():
            store_id = str[0]
            str_transaction_val = str[5]
            day_of_week_transaction_percent =str[day_of_week]
            max_transaction_vol = round(day_of_week_transaction_percent * str_transaction_val )
            min_cus_id =str[13]
            max_cus_id =str[14]
            
            # generate number of transactions 
            for no_tra in range(1,max_transaction_vol+1):
                transaction_id = no_tra
                transaction_date = d_date
                str_id = store_id
                product_details = getPID(df_product)
                product_id = product_details[0]
                price = product_details[1]
                qty = rd.randint(1, 10)
                total = price * qty
                cus_id = rd.randint(min_cus_id,max_cus_id)

            # append the values to a list which will be added to a dataframe
                transaction_id_list.append(transaction_id)
                transaction_date_list.append(transaction_date)
                str_id_list.append(str_id )
                product_id_list.append(product_id)
                price_list.append(price)
                qty_list.append(qty )
                total_list.append(total)
                cus_id_list.append(cus_id)

        # put result into a data frame and export to excel
        # df = pd.DataFrame([transaction_id_list, transaction_date_list, str_id_list, product_id_list, price_list, qty_list, total_list, cus_id_list]
        #                   ,columns = ['transaction_id' , 'Transaction_Date' , 'Store_Id', 'product_id' , 'price' , 'qty' , 'total_sales' ,'cust_id'])
        # df = pd.DataFrame([[1, 2], [3, 4]], columns = ["col1", "col2"])
        
        df = pd.DataFrame(
                            {'transaction_id':transaction_id_list,
                            'Transaction_Date':transaction_date_list,
                            'Store_Id':str_id_list,
                            'product_id': product_id_list,
                            'price' : price_list,
                            'qty' : qty_list,
                            'total_sales' : total_list,
                            'cust_id': cus_id_list                    
                            }
                          )
        # # get folder path by date
        dateFolder = d_date.strftime("%Y%m%d")
        # print(dateFolder)
        fol_path = os.path.join(result_folder,dateFolder)
        if os.path.isdir(fol_path):
            file_path = os.path.join(fol_path,f'{dateFolder}.xlsx')
            df.to_excel(file_path , index = False)
            print("Newly Done")
        else:
            os.makedirs(fol_path)
            file_path = os.path.join(fol_path,f'{dateFolder}.xlsx')
            df.to_excel(file_path , index = False)
            print("done")



print(generateData())