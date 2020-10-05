from peewee import *
from properties import config

conn = SqliteDatabase(config.db)


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    id = AutoField(column_name='id')
    first_name = TextField(column_name='first_name', null=True)
    last_name = TextField(column_name='last_name', null=True)
    birthday = DateField(column_name='birthday', null=True)

    class Meta:
        table_name = 'user'


class Project(BaseModel):
    id = AutoField(column_name='id')
    project_name = TextField(column_name='project_name', null=True)
    user_id = ForeignKeyField(User)
