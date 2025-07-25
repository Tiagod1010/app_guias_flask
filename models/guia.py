from mongoengine import Document, StringField, DateTimeField, ReferenceField
from datetime import datetime
from .instructor import Instructor

class Guia(Document):
    nombre = StringField(required=True)
    descripcion = StringField(required=True)
    programa = StringField(required=True)
    archivo = StringField(required=True)
    fecha = DateTimeField(default=datetime.utcnow)
    instructor = ReferenceField(Instructor)