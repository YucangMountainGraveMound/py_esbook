import web
import peewee
import json
import models.pedb as pedb
from playhouse.shortcuts import model_to_dict
db = pedb.database


def new_mail(uid, smtpHost, smtpPort, mail, pwd, kindlEmail):

    try:

        with db.atomic():
            umail = pedb.Mail.create(
                uid=uid, smtphost=smtpHost, smtpport=smtpPort, mail=mail, pwd=pwd, kindlemail=kindlEmail)
            print('success')
            return umail
    except:
        return None


def edit_mail(uid, smtpHost, smtpPort, mail, pwd, kindlEmail):

    try:

        with db.atomic():
            umail = pedb.Mail.update(
                smtpHost=smtpHost, smtpPort=smtpPort, mail=mail, pwd=pwd, kindlEmail=kindlEmail).where(pedb.Mail.uid == uid)
            print('success')
            return umail
    except:
        return None


def get_mail(uid):
    try:
        res = pedb.Mail.get(pedb.Mail.uid == uid)
        db.close()
    except:
        return None
    return json.dumps(model_to_dict(res))
