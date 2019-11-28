from peewee import *

db = PostgresqlDatabase('contacts', user='postgres',
                        password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact (BaseModel):
    name = CharField()
    phone = CharField()
    email = CharField()
    address = TextField()


db.create_tables([Contact])

tre = Contact(name='Tre', phone='3018025742',
              email='amack4693@gmail.com', address='3249 walters ln')
tre.save()
