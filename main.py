import sqlite3
from datetime import datetime

current_datetime = datetime.now().date()
datetime_1= str(current_datetime)
try: 
    connect_to = sqlite3.connect('switches.db')
    cur = connect_to.cursor()
    print("Подключен к SQLite")
    insert_data = """INSERT INTO mac_base
                    (switch_ip, port, port_mac, time) 
                    VALUES 
                    ('switch_ip_snmp', 'port_snmp','port_mac_snmp', :datetime_1);"""
    counw = cur.execute(insert_data, {'datetime_1':datetime_1})
    connect_to.commit()
    print("Запись удалась!", cur.rowcount)
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при работе c SQLite", error)

finally:
    if  connect_to:
        connect_to.close()
        print("Соединение c SQLite закрыто")
