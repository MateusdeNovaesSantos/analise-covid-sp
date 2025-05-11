import pandas as pd
import sqlite3

csv_file = "../data/covid_data.csv"
sqlite_file = "../data/covid_data.db"
table_name = "covid_data"

df = pd.read_csv(csv_file)

conn = sqlite3.connect(sqlite_file)
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()

print(f"Arquivo SQLite salvo como {sqlite_file}")