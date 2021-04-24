from config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    portfolio_value = db.Column(db.Float)

    def __init__(self, login, password, portfolio_value=0.0):
        self.login = login
        self.password = password
        self.portfolio_value = portfolio_value

    def json(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password
        }

    @classmethod
    def search_for_user(cls, log, passw):
        return cls.query.filter_by(login=log, password=passw).first()

    @classmethod
    def get_user_value(cls, id):
        return cls.query.filter_by(id=id).first().portfolio_value

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()