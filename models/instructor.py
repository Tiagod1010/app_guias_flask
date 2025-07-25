from mongoengine import Document, StringField
from flask_login import UserMixin

class Instructor(Document, UserMixin):
    nombre = StringField(required=True)
    correo = StringField(required=True, unique=True)
    regional = StringField(required=True)
    usuario = StringField(required=True, unique=True)
    password = StringField(required=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)