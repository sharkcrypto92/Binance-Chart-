from binance.client import Client
import pandas as pd
import mplfinance as mpf
#log in binance
client = Client(api_key='', api_secret='')

tickers = client.get_all_tickers()


tickers[1]['price']


ticker_df = pd.DataFrame(tickers)


#print(ticker_df)

#print(ticker_df.head())


ticker_df.set_index('symbol', inplace=True)


float(ticker_df.loc['ETHBTC']['price'])


#DEPTH 
depth = client.get_order_book(symbol='BTCUSDT')


#print(depth)


historical = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')


#print(historical)

hist_df = pd.DataFrame(historical)

hist_df.head()


hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 
                    'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']




#print(hist_df.head())

#Preprocess Historical Data

hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit='s')
hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit='s')

#convert to Num
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']

hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)

#print(hist_df)

hist_df.set_index('Close Time').tail(100)


#plot it 
mpf.plot(hist_df.set_index('Close Time').tail(120), 
        type='candle', style='charles', 
        volume=True, 
        title='BTCUSDT Last 120 Days', 
        mav=(10,20,30))