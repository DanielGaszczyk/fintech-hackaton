import csv
import os
from models import Stock, StockData
from config import db

path = '/home/szymon/Pulpit/stockdata/'


def load_file(name):
    file_reader = csv.reader(open(path + name), delimiter=',')
    stock = Stock(name.split('.')[0], True)
    stock.save_to_db()
    for idx, row in enumerate(file_reader):
        if idx == 0:
            continue
        stock_data = StockData(stock.id, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        stock_data.save_to_db()


db.create_all()
for filename in os.listdir(path):
    load_file(filename)