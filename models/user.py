from config import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def json(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password
        }

    @classmethod
    def search_for_user(cls, log, passw):
        return cls.query.filter_by(login=log, password=passw).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()