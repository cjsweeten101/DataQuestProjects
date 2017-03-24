import pandas as pd
from datetime import datetime

if __name__ == '__main__':
	stock = pd.read_csv('sphist.csv')
	stock['Date'] = pd.to_datetime(stock['Date'])

	stock.sort_values('Date', inplace='True')

	print(stock.head(5))