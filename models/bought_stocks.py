from config import db


class BoughtStocks(db.Model):
    __tablename__ = 'bought_stocks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    proportion = db.Column(db.Float)

    def __init__(self, uid, sid, prop):
        self.user_id = uid
        self.stock_id = sid
        self.proportion = prop

    @classmethod
    def get_stocks_for_user(cls, id):
        return cls.query(BoughtStocks).filter_by(user_id=id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

