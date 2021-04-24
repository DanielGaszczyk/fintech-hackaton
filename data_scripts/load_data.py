import csv
import os
from models import Stock, StockData, User, BoughtStocks
from config import db

path = '/home/szymon/fintech-hackaton/csv_data/'


db.create_all()
user1 = User('user1', 'user1', 5151.5)
user2 = User('user2', 'user2', 217711.4)
user3 = User('user3', 'user3', 912.3)
user1.save_to_db()
user2.save_to_db()
user3.save_to_db()


def load_file(name):
    file_reader = csv.reader(open(path + name), delimiter=',')
    stock = Stock(name.split('.')[0], True)
    stock.save_to_db()
    bought_stocks1 = BoughtStocks(user1.id, stock.id, 1.0)
    bought_stocks2 = BoughtStocks(user2.id, stock.id, 1.0)
    bought_stocks3 = BoughtStocks(user3.id, stock.id, 1.0)
    bought_stocks1.save_to_db()
    bought_stocks2.save_to_db()
    bought_stocks3.save_to_db()
    for idx, row in enumerate(file_reader):
        if idx == 0:
            continue
        stock_data = StockData(stock.id, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        stock_data.save_to_db()


for filename in os.listdir(path):
    load_file(filename)