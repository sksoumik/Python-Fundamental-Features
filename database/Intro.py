import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

connection = sqlite3.connect('intro.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS  stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES (465413, '08-03-2018', 'Kabir', 10.25)")
    connection.commit()
    c.close()
    connection.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))
    keyword = 'Soumik'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword,  value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    connection.commit()

# read from db
def read_from_db():
    c.execute("SELECT datestamp FROM stuffToPlot WHERE value > 3 AND unix > 1520594405")
    # data  = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row)


def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    data  = c.fetchall()

    dates = []
    values  = []

    for row in data:
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def up_and_delete():
    c.execute('SELECT * FROM stuffToPlot ')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 0')
    connection.commit()
    c.execute('SELECT * FROM stuffToPlot ')
    [print(row) for row in c.fetchall()]


# create_table()
# # data_entry()
#
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

# graph_data()
up_and_delete()
c.close()
connection.close()
