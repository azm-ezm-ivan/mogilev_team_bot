from peewee import *
import properties.config

props = properties.config

conn = SqliteDatabase(props.db)


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    user_id = AutoField(column_name='id')
    name = TextField(column_name='first_name', null=True)

    class Meta:
        table_name = 'user'
