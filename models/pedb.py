from peewee import *
database = MySQLDatabase('esbook', **{'charset': 'utf8', 'use_unicode': True,
                                      'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Books(BaseModel):
    book_no = CharField(null=True)
    chapter = CharField(null=True)
    name = CharField(null=True)
    uid = IntegerField()

    class Meta:
        table_name = 'books'


class Mail(BaseModel):
    kindlemail = CharField(column_name='kindlEmail', null=True)
    mail = CharField(null=True)
    pwd = CharField(null=True)
    smtphost = CharField(column_name='smtpHost', null=True)
    smtpport = CharField(column_name='smtpPort', null=True)
    uid = IntegerField()

    class Meta:
        table_name = 'mail'
