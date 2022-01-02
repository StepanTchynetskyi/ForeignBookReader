from marshmallow import EXCLUDE
from marshmallow import validates, ValidationError

from ma import ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        unknown = EXCLUDE
        load_only = ("password",)
        dump_only = ("id",)

    @validates("username")
    def validate_username(self, value):
        if len(value) < 4:
            raise ValidationError("Too short username(min 4 symbols)")
