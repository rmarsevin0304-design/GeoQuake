import sqlite3
import pymysql

# Koneksi ke MySQL (XAMPP)
mysql = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bps_lubuklinggau"
)

cur_mysql = mysql.cursor()

# Membuat SQLite
sqlite = sqlite3.connect("geoquake.db")
cur_sqlite = sqlite.cursor()

tables = ["admin", "gempa", "statistik_bps"]

for table in tables:
    # Ambil struktur tabel
    cur_mysql.execute(f"SHOW CREATE TABLE {table}")
    create_sql = cur_mysql.fetchone()[1]

    # Sesuaikan sintaks MySQL -> SQLite
    create_sql = create_sql.replace("AUTO_INCREMENT", "AUTOINCREMENT")
    create_sql = create_sql.replace("`", "")
    create_sql = create_sql.split("ENGINE=")[0]
    create_sql = create_sql.replace("int(", "INTEGER(")
    create_sql = create_sql.replace("double", "REAL")
    create_sql = create_sql.replace("float", "REAL")
    create_sql = create_sql.replace("datetime", "TEXT")

    try:
        cur_sqlite.execute(f"DROP TABLE IF EXISTS {table}")
        cur_sqlite.execute(create_sql)
    except Exception as e:
        print(table, e)

    # Salin data
    cur_mysql.execute(f"SELECT * FROM {table}")
    rows = cur_mysql.fetchall()

    if rows:
        placeholders = ",".join(["?"] * len(rows[0]))
        cur_sqlite.executemany(
            f"INSERT INTO {table} VALUES ({placeholders})",
            rows
        )

sqlite.commit()

mysql.close()
sqlite.close()

print("Selesai membuat geoquake.db")