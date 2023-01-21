import sqlite3
def connect():
    connection = sqlite3.connect("database/balance.db")
    return connection

class Probabilistic:
    def __init__(self,glucose,blood,bmi,age,label):
        self.glucose = glucose
        self.blood = blood
        self.bmi = bmi
        self.age = age
        self.label = label
    def Glukosa(self):
        conn = connect()
        cr = conn.cursor()
        data = str(self.glucose),int(self.label)
        sql = "select count(*) from diabetes where Kadar_Glukosa= ? AND Hasil= ?"
        cr.execute(sql,data)
        conn.commit()
        result =cr.fetchone()[0]
        return result
    def Darah(self):
        conn = connect()
        cr = conn.cursor()
        data = str(self.blood),int(self.label)
        sql = "select count(*) from diabetes where Tekanan_Darah= ? AND Hasil= ?"
        cr.execute(sql,data)
        conn.commit()
        result =cr.fetchone()[0]
        return result
    def Berat(self):
        conn = connect()
        cr = conn.cursor()
        data = str(self.bmi),int(self.label)
        sql = "select count(*) from diabetes where Berat_Tubuh= ? AND Hasil= ?"
        cr.execute(sql,data)
        conn.commit()
        result =cr.fetchone()[0]
        return result
    def Umur(self):
        conn = connect()
        cr = conn.cursor()
        data = str(self.age),str(self.label)
        sql = "select count(*) from diabetes where Umur= ? AND Hasil= ?"
        cr.execute(sql,data)
        conn.commit()
        result =cr.fetchone()[0]
        return result
    def Label(self):
        conn = connect()
        cr = conn.cursor()
        data = str(self.label)
        sql = "select count(*) from diabetes where Hasil= ?"
        cr.execute(sql,data)
        conn.commit()
        result =cr.fetchone()[0]
        return result
