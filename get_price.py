import pandas as pd
data = pd.read_csv('Data.csv')
def get_price(size, month, day):
    price = 20000
    for i in range(1095):
        if i==20:
            print(data.iloc[i]) 
        if data.iloc[i]['HALL']==size and data.iloc[i]['MONTH']==month and data.iloc[i]['DAY']==int(day):
            price = data.iloc[i]['PRICE PER PLATE']
    return price
