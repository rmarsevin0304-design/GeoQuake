import sqlite3
import pymysql

# ======================
# Koneksi SQLite
# ======================
sqlite_conn = sqlite3.connect("geoquake.db")
sqlite_cursor = sqlite_conn.cursor()

# ======================
# Koneksi MySQL Railway
# ======================
mysql_conn = pymysql.connect(
    host="altaria.proxy.rlwy.net",
    port=29438,
    user="root",
    password="IkYGxVgTdKzhUpdouQLJsYPseIheDHbg",
    database="railway"
)

mysql_cursor = mysql_conn.cursor()

# ======================
# Tabel admin
# ======================
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
)
""")

sqlite_cursor.execute("SELECT * FROM admin")

for row in sqlite_cursor.fetchall():
    mysql_cursor.execute(
        "INSERT INTO admin VALUES (%s,%s,%s)",
        row
    )

# ======================
# Tabel gempa
# ======================
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS gempa (
    id INT PRIMARY KEY,
    tanggal VARCHAR(50),
    jam VARCHAR(30),
    magnitude FLOAT,
    kedalaman VARCHAR(30),
    wilayah VARCHAR(200),
    potensi VARCHAR(200),
    koordinat VARCHAR(100)
)
""")

sqlite_cursor.execute("SELECT * FROM gempa")

for row in sqlite_cursor.fetchall():
    mysql_cursor.execute(
        "INSERT INTO gempa VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        row
    )

# ======================
# Tabel statistik_bps
# ======================
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS statistik_bps (
    id INT PRIMARY KEY,
    provinsi VARCHAR(100),
    kepadatan FLOAT
)
""")

sqlite_cursor.execute("SELECT * FROM statistik_bps")

for row in sqlite_cursor.fetchall():
    mysql_cursor.execute(
        "INSERT INTO statistik_bps VALUES (%s,%s,%s)",
        row
    )

mysql_conn.commit()

print("Migrasi selesai.")

sqlite_conn.close()
mysql_conn.close()