import sqlite3
import pandas as pd

# Membuat database SQLite
conn = sqlite3.connect("geoquake.db")

# Membaca CSV
admin = pd.read_csv("admin.csv")
gempa = pd.read_csv("gempa.csv")
statistik = pd.read_csv("statistik_bps.csv")

# Menyimpan ke SQLite
admin.to_sql("admin", conn, if_exists="replace", index=False)
gempa.to_sql("gempa", conn, if_exists="replace", index=False)
statistik.to_sql("statistik_bps", conn, if_exists="replace", index=False)

conn.close()

print("Selesai membuat geoquake.db")