import sqlite3

# koneksi db
con = sqlite3.connect("rs.db")
cur = con.cursor()
# buat table rs
# if con:
cur.execute(
    f"""CREATE TABLE IF NOT EXISTS rujukan (
        kode_rs INTEGER PRIMARY KEY AUTOINCREMENT,
        kamar INTEGER,
        telepon text,
        lat FLOAT,
        lon FLOAT,
        alamat text,
        wilayah text,
        provinsi text)"""
)
cur.execute(
    f"""INSERT INTO rujukan
    (kamar,telepon,lat,lon,alamat,wilayah,provinsi)
    VALUES 
    (01,'0852-5223-4242',-6.108679,106.899865,'JALAN DELI NO. 4 TANJUNG PRIOK JAKARTA 14220','JAKARTA UTARA, DKI JAKARTA','DKI JAKARTA')"""
)
cur.execute("SELECT * FROM rujukan")
# cur.execute(f"INSERT INTO rujukan VALUES() ")
rows = cur.fetchall()

for row in rows:
    print(row)


con.commit()
con.close()

"""

buat table
CREATE IF NOT EXIST nama_table 
(nama_kolom, tipe data )
- PRIMARY KEY
- AUTO INCEREMENT
- tipe data= (real, integer,text dll.)
hapus table
DROP TABLE nama_table
menambahkan data
INSERT INTO nama_table () VALUES () 
menghapus semua data
DELETE FROM nama_table WHERE kondisi

"""
