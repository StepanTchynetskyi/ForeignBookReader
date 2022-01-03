from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(90), nullable=False, unique=True)
    password = db.Column(db.LargeBinary(), nullable=False)

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_user_by_id(self):
        db.session.delete(self)
        db.session.commit()

    def change_user_name(self, email):
        self.email = email
        db.session.commit()

    def change_user_password(self, password):
        self.password = password
        db.session.commit()
