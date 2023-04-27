import sqlite3

con = sqlite3.connect("kütüphane1.db")


cursor = con.cursor()
def tablo_olustur1():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT, sayfasayisi INT)")
    con.commit()
tablo_olustur1()

con.close()
