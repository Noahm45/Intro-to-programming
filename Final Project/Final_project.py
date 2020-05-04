import requests
import pandas as pd
import json
import BeautifulSoup

import alpaca_trade_api as tradeapi

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'ALPACA_API_KEY_ID' : 'PKC2WHX3Y6HPW5VG4TOO', 'ALPACA_API_SECRET_KEY' : 'cdNWY8A7TxMm5UobbIOBiiOXUOFOB2sjSAWum1fQ'}




def get_account():
    r = requests.get(account_url, headers=HEADERS)

    return json.loads(r.content)




def get_fundamental_data(df):
    for symbol in df.index:
        try:
            url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
            soup = bs(requests.get(url).content)
            for m in df.columns:
                df.loc[symbol,m] = fundamental_metric(soup,m)
        except Exception as e:
            print (symbol, 'not found')
    return df

def fundamental_metric(soup, metric):
    return soup.find(text = metric).find_next(class_='snapshot-td2').text

#below is where you put the stock you wanna calculate.
stock_list = [

]

metric = ['P/B',
'P/E',
'Forward P/E',
'PEG',
'Debt/Eq',
'EPS (ttm)',
'Dividend %',
'ROE',
'ROI',
'EPS Q/Q',
'Insider Own'
]

df = pd.DataFrame(index=stock_list,columns=metric)
df = get_fundamental_data(df)
print df.head()

df = df[(df['P/E'].astype(float)<15) & (df['P/B'].astype(float) < 1.5)]

df['EPS Q/Q'] = df['EPS Q/Q'].map(lambda x: x[:-1])
df = df[df['EPS Q/Q'].astype(float) > 10]

df['ROE'] = df['ROE'].map(lambda x: x[:-1])
df = df[(df['Debt/Eq'].astype(float) < 1) & (df['ROE'].astype(float) > 8)]

df['Insider Own'] = df['Insider Own'].map(lambda x: x[:-1])
df = df[df['Insider Own'].astype(float) > 25]

print df.head()






#this is where you make your paper investment.
def create_order (symbol, qty, side, type, time_in_force):
        data ={
        'Symbol': symbol,
        'qty': qty,
        'type': type,
        'time_in_force': time_in_force,
        }
#type = buy or sell,

        r = requests.post(ORDERS_URL json=data, headers=HEADERS)

        return json.loads(r.content)

response = create_order('',,'','','')

print(response)
