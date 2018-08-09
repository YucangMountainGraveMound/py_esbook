# coding:utf-8
import web
import controllers
import datetime
import threading
import services.crawl as crawl

urls = (
    '/api/index', controllers.index,
    '/api/new_book', controllers.book_add,
    '/api/edit_book', controllers.edit_book,
    '/api/all_book/(.*)', controllers.book_list,
    '/api/book/(.*)', controllers.book_get,
    '/api/del_book/(.*)', controllers.book_del,
    '/api/new_mail', controllers.new_mail,
    '/api/edit_mail', controllers.edit_mail,
    '/api/mail/(.*)', controllers.get_mail
)


def compute_time():
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天6点时间
    next_time = datetime.datetime.strptime(str(
        next_year)+"-"+str(next_month)+"-"+str(next_day)+" 06:00:00", "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天6点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)
    timer = threading.Timer(timer_start_time, crawl.main())
    timer.start()


def customhook():
    web.header('Access-Control-Allow-Origin', '*')
    web.header('Access-Control-Allow-Headers',
               'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
    web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')


if __name__ == "__main__":
    # web.config.debug = True
    web.config.debug = False
    app = web.application(urls, globals())
    app.add_processor(web.loadhook(customhook))
    app.run()
