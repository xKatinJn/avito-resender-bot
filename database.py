from peewee import SqliteDatabase, Model, IntegerField, TextField, BooleanField
from playhouse.migrate import SqliteMigrator


connection = SqliteDatabase('avito-resender-bot.sqlite')
migrator = SqliteMigrator(connection)


class BaseModel(Model):
    class Meta:
        database = connection


class Chat(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    chat_id = IntegerField(column_name='chat_id')
    is_active = BooleanField(column_name='is_active')

    @staticmethod
    def get_all_chats() -> list:
        return [chat for chat in Chat.select().dicts().execute()]


if __name__ == '__main__':
    connection.create_tables([Chat])
    print('Database successfully created')
