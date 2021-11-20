from . import db, ma

# Inherits from db.Model and UserMixin
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))


class UserSchemaWithPass(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name')


user_schema = UserSchema()
user_schema_with_pass = UserSchemaWithPass()

db.create_all()   # sync database