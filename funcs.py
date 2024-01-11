import pandas as pd, os,csv, math
from pathlib import Path
import os
from datetime import datetime as dt


# def checkIfScheduleRan():
#     if os.path.exists('check.txt'):
#         os.remove('check.txt')
#     filename = Path('check.txt')
#     filename.touch(exist_ok=True)  # will create file, if it exists will do nothing
#     with  open(filename,'w', encoding='utf-8')as file:
#         file.write(f"The schedule ran at {dt.now()}")
#         file.close()

def escChar(text):
    text = str(text)
    if text.find("'") > 0 :
        new_text = text.replace("'","''")
    else :
        new_text = text

    return new_text



def removeallfiles():
    folder = os.getcwd()
    for xl in  os.listdir(folder):
        if "log_" in xl :
            os.remove(os.path.join(folder,xl))


def logJob(text,file_cnt ):
    
    file_path = os.path.join(os.getcwd(),"logs", f"log_{file_cnt}.txt")
    if os.path.exists(file_path):
        file = open(file_path,"a")
        file.write(f'\n{text}')
    else:
        file = open(file_path,"w")
        file.write(f'{text}\n')

    return True

def getData():
    file_path = os.path.join(os.getcwd(),"chicago_crime_dataset.csv")
    df = pd.read_csv(file_path)
    x=0
    cnt= 1
    while x <= df.shape[0]:
        df.loc[x:x+1000000].to_excel(f"dataset_{cnt}.xlsx", index= False)
        x=x+100001
        cnt=cnt+1
        print(cnt)

def getDataF():
    removeallfiles()
    insert_stat = """Insert into tbl_chicago_crime_data([ID],[Case_Number],[date_reported], [block_address],[crime_report_code],[primary_type],[crime_description] 
                        ,[location_description],[arrest] ,[domestic] ,[crime_spot] ,[District] ,[Ward],[Community_Area],[FBI_Code] ,[X_Coordinate] 
						,[Y_Coordinate], [year_of_crime] , [Updated_On] , [lat], [lon], [crime_location]
						) 
                        
                        values """
    file_cnt = 1
    # with open(os.path.join(os.getcwd(), 'data.csv'), "r") as csvfile:
    #     reader_variable = csv.reader(csvfile, delimiter=",")

    for xl in os.listdir(os.getcwd()):
        if "dataset_" in xl :
            df = pd.read_excel(os.path.join(os.getcwd(), xl) )
            cnt = 0
            for _ ,rw in df.iterrows():  
                print(rw)   
                
                if not rw[0]:
                    id = 'Null'
                else:
                    id =  rw[0]


                if not rw[1]:
                    case_number="Null"
                else: 
                    case_number= f"'{escChar(rw[1])}'"


                if not rw[2]:
                    date = "Null"
                else:
                    date = f"'{rw[2]}'"

                if not rw[3]:
                    block = "Null"
                else:
                    block = f"'{escChar(rw[3])}'"

                if not rw[4]:
                    iucr= "Null"
                else:
                    iucr= f"'{escChar(rw[4])}'"

                if not rw[5] :
                    pri_type= "Null"
                else:
                    pri_type= f"'{escChar(rw[5])}'"

                if not rw[6] :
                    description= 'Null'
                else :
                    description =f"'{escChar(rw[6])}'"

                if not rw[7]:
                    long_description= 'Null'
                else:
                    long_description= f"'{escChar(rw[7])}'"

                if not rw[8]:
                    arrest = 'Null'
                else:
                    arrest= f"'{escChar(rw[8])}'"
                
                if not rw[9]:
                    domestic = 'Null'
                else:
                    domestic = f"'{escChar(rw[9])}'"
                
                if not rw[10]:
                    beat = 'Null'
                else:
                    beat = f"'{escChar(rw[10])}'"
                

                if not rw[11]:
                    district= 'Null'
                else:
                    district = f"'{escChar(rw[11])}'"

                if not rw[12]:
                    ward = "Null"
                else:
                    ward = rw[12]


                if not rw[13]:
                    community_area ='Null'
                else:
                    community_area =f"'{escChar(rw[13])}'"

                if not rw[14]:
                    fbi_code = 'Null'
                else:
                    fbi_code = f"'{escChar(rw[14])}'"

                if not rw[15]:
                    x_cord ='Null'
                else:
                    x_cord = rw[15]

                if not rw[16]:
                    y_cord ="Null"
                else:
                    y_cord = f"'{escChar(rw[16])}'"

                if not rw[17]:
                    year = 'Null'
                else:
                    year = f"'{escChar(rw[17])}'"

                if not rw[18]:
                    updated_on= "Null"
                else:
                    updated_on = f"'{escChar(rw[18])}'"
                
                if not rw[19]:
                    lat = 'Null'
                else:
                    lat = f"'{escChar(rw[19])}'"

                if not rw[20]:
                    long = 'Null'
                else :
                    long = f"'{escChar(rw[20])}'"
    
                if not rw[21]:
                    location = 'Null'
                else :
                    location = f"'{escChar(rw[21])}'"
                
                if location == 'NaN':
                    location = 'Null'


                # line_text= f""" ( {id} ,'{case_number}','{date}','{block}'                      ),"""
                # line_text= f""" ( {id}, '{case_number}','{date}','{block}','{iucr}','{pri_type}','{description}','{long_description}','{arrest}', '{domestic}', '{beat}', '{district}', {ward},'{community_area}','{fbi_code}', '{x_cord}' , '{y_cord}',{year},'{updated_on}',{lat},{long},'{location}' )    """
                line_text= f""" ( {id}, {case_number},{date},{block},{iucr},{pri_type},{description},{long_description},{arrest}, {domestic}, {beat}, {district}, {ward},{community_area},{fbi_code}, {x_cord} , {y_cord},{year},{updated_on},{lat},{long},{location} )    """
                
                

                if cnt  == 1  or math.fmod(cnt,999) ==1 :
                    new_val= insert_stat  + line_text + ", "
                    
                elif math.fmod(cnt,999) ==0  and cnt > 0:
                    new_val =  line_text 
                    if new_val[-1] == ",":
                        new_val = new_val[0: len(new_val)-1]
                    
                elif cnt == 0 :
                    print("I am doing nothing")
            
                elif cnt == df.shape[1]-1:
                    new_val = line_text 
                else:
                    new_val = line_text + ","

                if cnt > 0:
                    logJob(new_val,file_cnt)  
                    print(new_val)
                    break
                # if math.fmod(cnt,700000) == 0 and cnt > 0 :  
                #     if new_val[-1] == ",":
                #         new_val = new_val[0: len(new_val)-2]
                #         logJob(new_val,file_cnt)              
                    
                #     file_cnt= file_cnt + 1
                #     cnt = 0

                # else:
                #     if cnt > 0:
                        
                #         logJob(new_val,file_cnt)
                
                
                cnt = cnt + 1
            file_cnt=file_cnt+1



getData()
