import pandas as pd , os

def getdata():
    file_path = os.path.join(os.getcwd(),"chicago_crime_dataset.csv")
    print(1)
    df = pd.read_csv(file_path)
    x=0
    cnt= 1
    while x <= df.shape[0]:
        df.loc[x:x+500].to_excel(f"dataset_{cnt}.xlsx", index= False)
        x=x+501
        cnt=cnt+1
        break


getdata()