import sqlite3 as s


con=s.connect('contacts.db')

cursur=s.Cursor(con)

cursur.execute('CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,mobile INTEGER,tel INTEGER,email TEXT)')
def contact_insert(name,mobile,tel,email):
    cursur.execute('INSERT INTO contacts VALUES(?,?,?,?,?)',(name,mobile,tel,email))
    con.commit()

def contact_delete(name):
    cursur.execute('DELETE FROM contacts WHERE name=?',(name,))
    con.commit()

def contact_list():
    cursur.execute('SELECT * FROM contacts')
    re=cursur.fetchall()
    print(re[1][1])

def contact_update(**kwargs):
    cursur.execute('UPDATE contacts SET name=? email=? mobile=? where id=?',(name,email,mob))
    con.commit()



cursur.close()
con.close()
