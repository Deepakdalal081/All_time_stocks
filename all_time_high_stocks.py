import pandas as pd 
import numpy as np 
import yfinance as yf 
import datetime as dt  

import matplotlib.pyplot as plt 

# Data preparation
end_date = dt.date.today()
start_date = end_date  - dt.timedelta(days = 1000)


stocks = ["TEMBO.NS", 'TEGA.NS','ACI.NS','MEDPLUS.NS','MAHSCOOTER.NS']
all_time_high  = []

all_time_high_week = []

all_time_high_month = []

for stock in stocks:
    data = yf.download(stock, start=start_date, end=end_date, interval="1D")
    data = np.round(data, 3)
    

    if data["High"].iloc[-1] >= data["High"].max():
          all_time_high.append(stock)
 
    elif (data["High"].iloc[-7:] >=  data["High"].max()).any():
           all_time_high_week.append(stock)
    
    elif (data["High"].iloc[-30:] >=  data["High"].max()).any():
          all_time_high_month.append(stock)
    else:
         pass 

all_time_high_df = pd.DataFrame(all_time_high, columns=["Stock"])

all_time_high_week_df = pd.DataFrame(all_time_high_week, columns=["Stock"])    

all_time_high_month_df = pd.DataFrame(all_time_high_month, columns=["Stock"])


print("---------------------------")
print("Stocks which are all time high :")
print(all_time_high_df)        
        
print("------------------------")
print("Stocks which have gone for all time high in last 7 days ")
print(all_time_high_week_df)

print("------------------------")
print("Stocks which have gone for all time high in last 30 days ")
print(all_time_high_month_df)






