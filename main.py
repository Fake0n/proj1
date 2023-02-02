import sqlite3

try:
    conn = sqlite3.connect('switches.db')
    create_table = '''CREATE TABLE switches_base (
                                switch_name TEXT NOT NULL,
                                switch_ip INTEGER NOT NULL  UNIQUE,
                                switch_mac INTEGER NOT NULL UNIQUE,
                                switch_gateway INTEGER NOT NULL,
                                ports_all INTEGER NOT NULL,
                                ports_free INTEGER NOT NULL,
                                port_mac INTEGER NOT NULL,
                                time INTEGER NOT NULL
                                );'''
    cur = conn.cursor()
    print("База данных подключена к SQLite")
    cur.execute(create_table)
    conn.commit()
    print("Таблица SQLite создана")

    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к БД SQLite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение c SQLite закрыто")
