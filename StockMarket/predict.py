import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#Read and sort by Data
stock = pd.read_csv('sphist.csv')
stock['Date'] = pd.to_datetime(stock['Date'])

stock.sort_values('Date', inplace='True')

#Generate Indicators
stock['day_5'] = stock['Close'].rolling(center=False,window=5,min_periods=5).mean()
stock['day_5'] = stock['day_5'].shift(1)

stock['day_365'] = stock['Close'].rolling(center=False,window=365,min_periods=365).mean()
stock['day_365'] = stock['day_365'].shift(1)

stock['day_ratio'] = stock['day_5']/stock['day_365']

stock['std_365'] = stock['Close'].rolling(center=False,window=365,min_periods=365).std()

#Adding more indicators
stock['vol_5'] = stock['Volume'].rolling(center=False,window=5,min_periods=5).mean()
stock['vol_5'] = stock['vol_5'].shift(1)

stock['month'] = stock['Date'].dt.month

#Split up the data
stock = stock[stock['Date'] > datetime(year=1951, month=1, day=2)]
stock.dropna(axis=0, inplace=True)

train = stock[stock['Date'] < datetime(year=2013, month=1, day=1)]
test = stock[stock['Date'] >= datetime(year=2013, month=1, day=1)]

#Making Predictions
#Error Metric -> Mean Absolute Error
lr = LinearRegression()
columns = ['day_5','day_365','day_ratio','std_365', 'vol_5', 'month']

x_train = train[columns]
y_train = train['Close']

lr.fit(x_train, y_train)

x_test = test[columns]
predictions = lr.predict(x_test)

mae = mean_absolute_error(test['Close'], predictions)

print(mae)