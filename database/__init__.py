from peewee import Model, PostgresqlDatabase, CharField, DateTimeField, AutoField, IntegrityError
from os import environ
from datetime import datetime

database = PostgresqlDatabase(environ['DB_NAME'], user=environ['DB_USER'], password=environ['DB_PASSWORD'],
                              host=environ['DB_HOST'], port=environ["DB_PORT"])


class MailList(Model):
    class Meta:
        database = database

    id = AutoField(primary_key=True)
    email = CharField(unique=True)
    topics = CharField(default="promotions;updates;features")
    created_at = DateTimeField(default=datetime.utcnow)


with database:
    database.create_tables([MailList])


def create_email(input_email: str) -> bool:
    with database.atomic():
        try:
            email = MailList(email=input_email)
            email.save()
            return True
        except IntegrityError as _:
            return False
        except Exception as e:
            print("Error", e)
            raise e
