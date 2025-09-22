from .models import Referral
from Gear.db import db
from Gear.models import User

def add_referral(inviter_id: int, invited_id: int, bonus: int):
    db.connect()
    inviter = User.get_or_none(User.id == inviter_id)
    invited = User.get_or_none(User.id == invited_id)
    if inviter and invited:
        Referral.create(inviter=inviter, invited=invited, bonus=bonus)
        inviter.balance += bonus
        inviter.save()
    db.close()
