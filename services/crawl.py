# coding:utf-8
from urllib import request
from datetime import date
from bs4 import BeautifulSoup
import re
import os
import datetime
import threading

# 请求头字典
req_header = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
req_url_base = 'https://www.xxbiquge.com'  # 小说主地址

# 获取文章章节


def search_chapter(dl, chapter):
    for k in range(len(dl)):
        if chapter in dl[k].string and len(dl) > (k+1):
            return dl[k+1:]
    return []


def get_chapter(book_id, book_name, chapter):
    req_url = req_url_base+"/"+book_id+"/"  # 单独一本小说地址
    req = request.Request(req_url, headers=req_header)
    html = request.urlopen(req).read()
    result = html.decode('utf-8', 'ignore')  # 用某种编码方式解释网页
    soup = BeautifulSoup(result, 'lxml')
    dl = soup.find('dl')
    dd = search_chapter(dl.contents, chapter)
    for i in dd:
        if i != '\n' and "正文" not in i.string:
            print(i)
            get_content(i.string,
                        req_url_base + i.a["href"], book_name)
    # get_content(dl.contents[2967].string,
        # req_url_base + dl.contents[2967].a["href"], book_name)

# 获取文章内容


def get_content(title, text_url, book_name):
    chapter_req = request.Request(text_url, headers=req_header)
    html = request.urlopen(chapter_req).read()
    result = html.decode('utf-8', 'ignore')
    soup = BeautifulSoup(result, "lxml")
    div_content = soup.find(attrs={"id": "content"})  # 找到小说正文部分的元素
    # print(re.sub('[\xa0]+', "\r\n\r\n", div_content.text))
    if book_name not in os.listdir("../books"):
        os.makedirs("../books/" + book_name)
    today = date.today()
    today = today.strftime('%Y%m%d')
    with open("../books/"+book_name+"/" + today +
              ".txt", "a", encoding='utf-8') as txt_file:  # 打开文件，不存在则建
        txt_file.writelines(title)
        lines = re.sub('[\xa0]+', "\r\n\r\n",
                       div_content.text)  # 将'\xa0'替换为换行符
        # lines = lines[:re.search(";?\[[笔趣看]?", lines).span()[0]]  # 去掉文章末尾不需要的内容
        txt_file.writelines(lines+'\n')  # 写数据到文件


def main():
    # TODO: // 循环书籍执行搜书
    # TODO://循环邮箱推送今天的搜索结果
    timer = threading.Timer(86400, main())
    timer.start()
    

if __name__ == '__main__':
    get_chapter('8_8109','帝霸','第3189章最惊艳的真帝')
