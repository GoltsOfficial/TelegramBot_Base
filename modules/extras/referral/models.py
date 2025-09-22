from peewee import Model, ForeignKeyField, IntegerField
from Gear.db import db
from Gear.models import User

class Referral(Model):
    inviter = ForeignKeyField(User, backref='referrals')
    invited = ForeignKeyField(User, backref='invited_by')
    bonus = IntegerField(default=0)

    class Meta:
        database = db
