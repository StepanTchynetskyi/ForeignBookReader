from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def save_user_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_user_by_id(self):
        db.session.delete(self)
        db.session.commit()

    def change_user_name(self, username):
        self.username = username
        db.session.commit()

    def change_user_password(self, password):
        self.password = password
        db.session.commit()
