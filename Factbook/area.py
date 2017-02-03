import sqlite3


conn = sqlite3.connect("factbook.db")

tot_land = conn.execute("select sum(area_land) from facts;").fetchall()
tot_water = conn.execute("select sum(area_water) from facts;").fetchall()

print("Area of land/water: " + str(tot_land[0][0]/tot_water[0][0]))

