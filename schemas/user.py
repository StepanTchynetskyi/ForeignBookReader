from marshmallow import EXCLUDE
from marshmallow import validates, ValidationError

from ma import ma
from models.user import UserModel

from constants import HAS_UPPERCASE_LETTERS, HAS_LOWERCASE_LETTERS, HAS_NUMBERS, HAS_SYMBOLS

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        unknown = EXCLUDE
        load_only = ("password",)
        dump_only = ("id",)

    @validates("email")
    def validate_email(self, value):
        if len(value) < 4:
            raise ValidationError("Too short email(min 4 symbols)")

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Too short password(min 8 symbols)")
        elif not HAS_UPPERCASE_LETTERS.search(value):
            raise ValidationError("Password should have at least one uppercase letter")
        elif not HAS_LOWERCASE_LETTERS.search(value):
            raise ValidationError("Password should have at least one lowercase letter")
        elif not HAS_NUMBERS.search(value):
            raise ValidationError("Password should have at least one number")
        elif not HAS_SYMBOLS.search(value):
            raise ValidationError("Password should have at least one special symbol")
