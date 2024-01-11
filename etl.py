import pyodbc as py, pandas as pd,os
from sqlalchemy import create_engine as ce

server = "Olu\SQLEXPRESS"
database ="Training"
driver = 'ODBC Driver 17 for SQL Server'
database_con = f'mssql://@{server}/{database}?driver={driver}'


def doTheEl():
    # df = pd.read_csv()
    cnxn = py.connect('DRIVER={SQL Server};SERVER=Olu\SQLEXPRESS;DATABASE=Training;trusted_connection=yes')
    cursor = cnxn.cursor()
    
    for xl in os.listdir(os.getcwd()):
        if "dataset_" in xl:

            df = pd.read_excel(os.path.join(os.getcwd(),xl))
            engine = ce(database_con)
            con = engine.connect()
            df.to_sql('tbl_chicago_crime', engine, if_exists='append', index=False)
            print(f"Dataset {xl} done")

           
doTheEl()