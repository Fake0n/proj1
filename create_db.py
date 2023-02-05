import sqlite3
import pysnmp

try:
    conn = sqlite3.connect('switches.db')
    create_table_ports_free = '''CREATE TABLE 
                                port_base (
                                switch_name TEXT NOT NULL,
                                switch_ip TEXT NOT NULL,
                                switch_mac TEXT NOT NULL,
                                switch_gateway TEXT NOT NULL,
                                ports_all TEXT NOT NULL,
                                ports_free TEXT NOT NULL,
                                time TEXT NOT NULL
                                );'''
    create_table_ports_mac = ''' CREATE TABLE 
                                mac_base (
                                switch_ip TEXT NOT NULL ,
                                port TEXT NOT NULL,
                                port_mac TEXT NOT NULL,
                                time TEXT NOT NULL
                                );'''

    cur = conn.cursor()
    print("База данных подключена к SQLite")
    cur.execute(create_table_ports_free)
    cur.execute(create_table_ports_mac)
    conn.commit()
    #print("Таблица SQLite создана")

    cur.close()



    
except sqlite3.Error as error:
    print("Ошибка при подключении к БД SQLite", error)



finally:
    if (conn):
        conn.close()
        print("Соединение c SQLite закрыто")