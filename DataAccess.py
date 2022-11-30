import sqlite3 as sql


def KayitEkleSql(sifre,uygulama):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    cursor.execute("insert into Sifreler (uygulama, sifre) values (?, ?)", (uygulama, sifre))
    conn.commit()
    cursor.close()
    conn.close()

def AnaSifreEkle(sifre):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    cursor.execute("insert into Sifreler (sifreId,uygulama, sifre) values (?,?, ?)", (1,"Ana Şifre", sifre))
    conn.commit()
    cursor.close()
    conn.close()


def IdileGuncelleSql(yeniuygulama,yenisifre,sifreId):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Sifreler SET uygulama=? ,sifre=?  WHERE sifreId=?", (yeniuygulama, yenisifre,sifreId))
    conn.commit()
    cursor.close()
    conn.close()

def IdileKayitSilSql(sifreId):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    sorgu = """DELETE from Sifreler where sifreId = ?"""
    data = (sifreId,)
    cursor.execute(sorgu, data)
    conn.commit()
    cursor.close()
    conn.close()



def KayitlariAlSql():
    conn = sql.connect("Sifreler.db")
    sorgu = "SELECT * from Sifreler"
    cursor = conn.cursor()
    cursor.execute(sorgu)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def IdileAra(sifreId):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    cursor.execute("select * from Sifreler where sifreId= ?", (sifreId,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def UygulamaileAra(value):
    conn = sql.connect("Sifreler.db")
    cursor = conn.cursor()
    cursor.execute("select * from Sifreler where uygulama like ?", ('%' + value + '%',))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows






