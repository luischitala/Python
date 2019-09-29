
from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db 
def create_and_connect():
    db.connect()
    db.create_tables([Person])

create_and_connect()