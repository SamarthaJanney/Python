#import packages
import pandas as pd
import datetime as dt
from dateutil.relativedelta import *

#User Input
interest=9
amount=200000
time=60
monthly_interest=interest/12/100
start_date = dt.datetime(2020,4,1)

#Create dataframe
df = pd.DataFrame(columns=['Date','Principal Amount O/S','EMI','Extra Payment','Interest Payment','Principal Payment','Balance'])
for i in range(time):
#Finding first row
    if i<1:
                  df=df.append({'Date':start_date + relativedelta(months=+i)
                  ,'Principal Amount O/S':amount
                  ,'EMI':amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))
                  ,'Extra Payment':0
                  ,'Interest Payment':(amount*(interest/100))/12
                  ,'Principal Payment':(amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))-(amount*(interest/100))/12)
                  ,'Balance':amount-(amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))-(amount*(interest/100))/12)}
                  ,ignore_index=True)
    else:
                  df=df.append({'Date':start_date + relativedelta(months=+i)
                  ,'Principal Amount O/S':df.loc[i-1,'Balance']
                  ,'EMI':amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))
                  ,'Extra Payment':0
                  ,'Interest Payment':(df.loc[i-1,'Balance']*(interest/100))/12
                  ,'Principal Payment':amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))-(df.loc[i-1,'Balance']*(interest/100))/12
                  ,'Balance':df.loc[i-1,'Balance']-(amount*monthly_interest*((pow(monthly_interest+1,time))/(pow(monthly_interest+1,time)-1))-(df.loc[i-1,'Balance']*(interest/100))/12)}
                  ,ignore_index=True)
        
#Excel filename
# file_name = 'MarksData2.xlsx'
# # saving the excel
# df.to_excel(file_name)
# #print success message
# print('DataFrame is written to Excel File successfully.')




