from peewee import Model, CharField, IntegerField
import os
#from playhouse.sqlite_ext import SqliteExtDatabase


#db = SqliteExtDatabase('my_database.db')

# heroku run -s free -- python setup.py
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class SavedTotal(Model):
    code = CharField(max_length=255, unique=True)
    value = IntegerField(max_length=255)

    class Meta:
        database = db


# class Context(BaseModel):
#     name = CharField(max_length=255)
#
#
# class ContextTask(BaseModel):
#     context_id = IntegerField()  # foreign key into context
#     task_id = IntegerField()  # foreign key into task
#
#     class Meta:
#         primary_key = CompositeKey(
#             'context_id', 'task_id'
#         )