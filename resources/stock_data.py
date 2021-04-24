from flask_restful import Resource
from models import StockData as sd


class StockData(Resource):

    def get(self):
        data = sd.get_all_data()
        if data is not None:
            datas = [d.json() for d in data]
            return {'datas': datas}, 200
        else:
            return {'message': 'no stocks'}, 404
