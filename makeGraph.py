import matplotlib.pyplot as plt
import datetime
import numpy as np
import sqlite3
import datetime

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


def readDB():
    conn = sqlite3.connect(NAME_DB, detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute('SELECT * FROM temp')
    d = c.fetchall()
    conn.commit()
    conn.close()
    return d


if __name__ == "__main__":
    initDB()
    data = readDB()
    x = []
    y = []
    for entry in data:
        x.append(entry[1])
        y.append(entry[0])

    plt.plot(x,y)
    plt.show()
