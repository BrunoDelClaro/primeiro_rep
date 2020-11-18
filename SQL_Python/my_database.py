import sqlite3



class MyDb:
    def __init__(self,db_to_connect):
        self.db_to_connect = db_to_connect


    def colocar_valor(self,nome,last_nome,age):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("INSERT INTO customers VALUES(?,?,?)",(nome,last_nome,age))
        conn.commit()
        conn.close()

    def colocar_muitos(self,stuff):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.executemany("INSERT INTO customers VALUES(?,?,?)",stuff)
        conn.commit()
        conn.close()

    def show(self):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM customers")
        print(c.fetchall())
        conn.commit()
        conn.close()

    def show_name(self,name):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("SELECT * FROM customers WHERE first_name = ?",(name,))
        print(c.fetchall())
        conn.commit()
        conn.close()
    def show_last_name(self,name):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("SELECT * FROM customers WHERE last_name = ?",(name,))
        print(c.fetchall())
        conn.commit()
        conn.close()

    def delete(self,name,last_name):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("DELETE FROM customers WHERE first_name = ? AND last_name = ?",(name,last_name))
        conn.commit()
        conn.close()

    def update(self,name,last_name,novo_nome,novo_last_name):
        conn = sqlite3.connect(self.db_to_connect)
        c = conn.cursor()

        c.execute("UPDATE customers SET first_name = ?, last_name = ? WHERE first_name = ? AND last_name = ?",(novo_nome,novo_last_name,name,last_name))
        conn.commit()
        conn.close()