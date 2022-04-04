# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import re

class NewsspiderPipeline(object):
    def process_item(self, item, spider):
        # 显示或存到数据库等操作放在这里。
        print('标题：', item['title'])
        print('内容：', item['content'])
        # list类型转成string类型，以便后续处理
        title = "".join(item['title'])
        content = "".join(item['content'])
        # 按实际需求进行字符串处理。这里用正则表达式替换掉html标签
        title = re.sub(r'</?\w+[^>]*>', '', title)
        content = re.sub(r'</?\w+[^>]*>', '', content)
        # 打开数据库连接。数据库服务器ip，账号，密码，数据库名
        db = pymysql.connect("127.0.0.1", "root", "python", "news")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "INSERT INTO newsInfo(title,content) VALUES('%s', '%s')" % (title, content)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()
        return item
