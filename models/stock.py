from config import db


class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dividend = db.Column(db.Boolean)

    def __init__(self, name, dividend):
        self.name = name
        self.dividend = dividend

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
