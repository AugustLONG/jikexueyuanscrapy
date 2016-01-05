# -*-coding:utf8-*-

# 原作者代码中的xpath路径变了，已经不能运行，遂修改。

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''重新运行之前请删除content.txt，因为文件操作使用追加方式，会导致内容太多。'''


def towrite(contentdict):
    #f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
    #f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')


def spider(url):
    html = requests.get(url)
    #print 'html: ', html.text
    selector = etree.HTML(html.text)
    #print 'selector: ', selector
    #content_field = selector.xpath('//div[@class="l_post l_post_bright "]')
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    print 'content_field[0]:', content_field[0]
    print 'content_field[1]:', content_field
    print 'content_field len:', len(content_field)
    for each in content_field:
        print 'word'
        #reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot', ''))
        #author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
        #reply_time = reply_info['content']['date']
        print 'hello'
        print content
        # print reply_time
        # print author
        #item['user_name'] = author
        item['topic_reply_content'] = content
        #item['topic_reply_time'] = reply_time
        towrite(item)
        print 'item:', item

if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('content.txt', 'a')
    page = []
    for i in range(1, 3):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)
        print 'newpage: ', newpage
        # html1 = requests.get(newpage)
        # print 'html1:', html1.text
    print 'page: ', page

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
    print results

# # 原作者的代码
# #-*-coding:utf8-*-
# from lxml import etree
# from multiprocessing.dummy import Pool as ThreadPool
# import requests
# import json
# import sys
#
# reload(sys)
#
# sys.setdefaultencoding('utf-8')
#
# '''重新运行之前请删除content.txt，因为文件操作使用追加方式，会导致内容太多。'''
#
# def towrite(contentdict):
#     f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
#     f.writelines(u'回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
#     f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')
#
# def spider(url):
#     html = requests.get(url)
#     selector = etree.HTML(html.text)
#     content_field = selector.xpath('//div[@class="l_post l_post_bright "]')
#     item = {}
#     for each in content_field:
#         reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
#         author = reply_info['author']['user_name']
#         content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content "]/text()')[0]
#         reply_time = reply_info['content']['date']
#         print content
#         print reply_time
#         print author
#         item['user_name'] = author
#         item['topic_reply_content'] = content
#         item['topic_reply_time'] = reply_time
#         towrite(item)
#
# if __name__ == '__main__':
#     pool = ThreadPool(4)
#     f = open('content.txt','a')
#     page = []
#     for i in range(1,21):
#         newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
#         page.append(newpage)
#
#     results = pool.map(spider, page)
#     pool.close()
#     pool.join()
#     f.close()

