# coding:utf-8
import web
import json
import models.book as book
import models.mail as mail


class index:
    def GET(self):
        return "Hello, world!"


class book_add:
    def OPTIONS(self):
        pass

    def POST(self):
        data = eval(web.data())
        print(data['uid'], data['name'], data['book_no'], data['chapter'])
        res = book.new_book(
            data['uid'], data['name'], data['book_no'], data['chapter'])
        if not res:
            return json.dumps([{'msg': 'success'}])
        return json.dumps([{'msg': 'fail'}])


class edit_book:
    def OPTIONS(self):
        pass

    def POST(self):
        data = eval(web.data())
        print(data['id'], data['name'], data['book_no'], data['chapter'])
        res = book.edit_book(
            data['id'], data['name'], data['book_no'], data['chapter'])
        if not res:
            return json.dumps([{'msg': 'success'}])
        return json.dumps([{'msg': 'fail'}])


class book_list:
    def GET(self, uid):
        return book.all_book(uid)


class book_get:
    def GET(self, id):
        return book.get_book(id)


class book_del:
    def GET(self, id):
        return book.del_book(id)


class new_mail:
    def OPTIONS(self):
        pass

    def POST(self):
        data = eval(web.data())
        print(data)
        res = mail.new_mail(data['uid'], data['smtpHost'], data['smtpPort'],
                            data['mail'], data['pwd'], data['kindlEmail'])
        if not res:
            return json.dumps([{'msg': 'success'}])
        return json.dumps([{'msg': 'fail'}])


class edit_mail:
    def OPTIONS(self):
        pass

    def POST(self):
        data = eval(web.data())
        res = mail.edit_mail(data['uid'], data['smtpHost'], data['smtpPort'],
                             data['mail'], data['pwd'], data['kindlEmail'])
        if not res:
            return json.dumps([{'msg': 'success'}])
        return json.dumps([{'msg': 'fail'}])


class get_mail:
    def GET(self, id):
        return mail.get_mail(id)
