from peewee import *
import properties.config

props = properties.config

conn = SqliteDatabase(props.db)


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
