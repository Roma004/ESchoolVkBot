# -*- coding: utf-8 -*-
from peewee import MySQLDatabase, Model, IntegerField, CharField
from app import app


db = MySQLDatabase(
    app.config['MYSQL']['db_name'], user=app.config['MYSQL']['user_name'],
    password=app.config['MYSQL']['password'],
    host=app.config['MYSQL']['host']
)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(default=0)
    position = CharField(default="", max_length=20)

    ts = IntegerField(default=0)
