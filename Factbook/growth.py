import sqlite3
import pandas as pd
import math

conn = sqlite3.connect("factbook.db")
facts = pd.read_sql_query(con=conn, sql='select * from facts;')

facts = facts.dropna(axis=0)

def popCalc(row):
	n_years = 35
	final_pop = row['population'] * math.e ** ((row['population_growth'] * .01) * n_years)
	return final_pop

facts['2050 Population'] = facts.apply(popCalc, axis=1)

facts.sort_values(by='2050 Population', ascending=False, inplace=True)

print(facts[['name', '2050 Population']].head(10))