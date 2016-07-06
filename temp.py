import sqlite3
import datetime
from time import sleep

FD = "/sys/bus/w1/devices/28-021502dacfff/driver/28-021502dacfff/w1_slave"
INTERVAL = 10 #minutes
NAME_DB = "tmp.sqlite"


def initDB():
    conn = sqlite3.connect(NAME_DB, detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE temp                                             
                 (tmp Single, time timestamp)''')
    except sqlite3.OperationalError:
        pass # Table already exists
    conn.commit()
    conn.close()


def writeDB(tmp, ts):
    conn = sqlite3.connect(NAME_DB, detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute('insert into temp values(?, ?)', (tmp, ts))
    conn.commit()
    conn.close()

while True :
    initDB()
    f = open(FD, 'r')
    tmp = f.read()[-6:-1]
    tmp = float(tmp)/1000
    writeDB(tmp, datetime.datetime.now())
    f.close()
    sleep(INTERVAL*60)
    
