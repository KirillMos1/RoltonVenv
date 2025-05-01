import os, sqlite3
print(os.getcwd())
db = sqlite3.connect(os.path.join(os.getcwd(), "bin", "sys", "data") + "users.db")
cursor = db.cursor()

def registr(name, passwd, workdir):
    try: cursor.execute("INSERT INTO users (name, passwd, workdir) VALUES (?, ?, ?)", (name, passwd, workdir))
    except Exception as e: return (1, e, None)
    else:
        cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
        ress = cursor.fetchall()
    db.commit()
    return (0, "", ress[0][0])

def user_data_get():
    returned = {}
    cursor.execute("SELECT id, name, passwd, workdir FROM users")
    ress = cursor.fetchall()
    for res in ress:
        returned[res[1]] = [res[0], res[1], res[2], res[3]]
    return returned

def checker():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
passwd TEXT NOT NULL,
workdir TEXT NOT NULL UNIQUE
)""")
    db.commit()
    cursor.execute("SELECT name, passwd FROM users")
    res = cursor.fetchall()
    print(res)
    if not res:
        return 0
    else:
        return user_data_get()
