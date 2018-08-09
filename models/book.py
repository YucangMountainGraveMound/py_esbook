# coding:utf-8
import web
import peewee
import json
import models.pedb as pedb
from playhouse.shortcuts import model_to_dict
db = pedb.database


def new_book(uid, name, book_no, chapter):

    try:

        with db.atomic():
            book = pedb.Books.create(
                uid=uid, name=name, book_no=book_no, chapter=chapter)
            print('success')
            return book
    except:
        return None


def edit_book(id, name, book_no, chapter):

    try:

        with db.atomic():
            book = pedb.Books.update(
                name=name, book_no=book_no, chapter=chapter).where(pedb.Books.id == id)
            print('success')
            return model_to_dict(book)
    except:
        return None


def all_book(uid):
    res = []
    books = pedb.Books.select().where(pedb.Books.uid == uid)
    for i in books:
        res.append(model_to_dict(i))
    db.close()
    return json.dumps(res)


def del_book(id):
    try:
        b = pedb.Books.get(pedb.Books.id == id)
        b.delete_instance()
        db.close()
        return b
    except:
        return None


def get_book(id):
    try:
        res = pedb.Books.get(pedb.Books.id == id)
        db.close()
    except:
        return None
    return json.dumps(model_to_dict(res))
